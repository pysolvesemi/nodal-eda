#!/usr/bin/env python3
"""Audit the reviewed bootstrap dependency, build and native-load boundary.

This is a conservative repository policy check plus Cargo/ELF inspection, not
an adversarial-code sandbox or a proof for future unreviewed source changes.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys
import tomllib

NATIVE = re.compile(r'\b(?:unsafe|dlopen|LoadLibrary[A-Z]*|libloading)\b|#\s*\[\s*(?:link|link_name)|extern\s*"(?:C|system)"|\binclude!\s*\(')


def manifest(path: Path) -> dict:
    return tomllib.loads(path.read_text(encoding="utf-8"))


def dependency_tables(data: dict):
    for name in ("dependencies", "build-dependencies", "dev-dependencies"):
        yield name, data.get(name, {})
    for target, target_data in data.get("target", {}).items():
        for name in ("dependencies", "build-dependencies", "dev-dependencies"):
            yield f"target.{target}.{name}", target_data.get(name, {})


def check(root: Path, cargo_metadata: dict | None = None) -> list[str]:
    root = root.resolve()
    errors = []
    try:
        policy = manifest(root / "policy/architecture.toml")
        workspace_doc = manifest(root / "Cargo.toml")
        workspace = workspace_doc["workspace"]
        packages = policy["packages"]
        members = workspace["members"]
        if policy.get("schema_version") != 1:
            errors.append("unsupported architecture-policy version")
        if sorted(members) != sorted(policy["workspace_members"]) or sorted(members) != sorted(packages.values()):
            errors.append("workspace differs from the reviewed package inventory")
        if workspace.get("exclude"):
            errors.append("workspace exclusions require explicit architecture review")
        if any(key in workspace_doc for key in ("patch", "replace", "package")):
            errors.append("root package/patch/replace bypasses the declared workspace boundary")
        toolchain = manifest(root / "rust-toolchain.toml")["toolchain"]
        if toolchain["channel"] != policy["rust_toolchain"]:
            errors.append("toolchain and reviewed inventory disagree")
        if workspace.get("lints", {}).get("rust", {}).get("unsafe_code") != "forbid":
            errors.append("workspace must forbid unsafe application code")
        allowed_paths = {root / "Cargo.toml"}
        shared = workspace.get("dependencies", {})
        for dep, value in shared.items():
            if not isinstance(value, dict) or dep not in packages or value.get("path") != packages[dep]:
                errors.append(f"workspace dependency {dep} is not an approved local package")
            if isinstance(value, dict) and any(k in value for k in ("git", "registry", "registry-index")):
                errors.append(f"workspace dependency {dep} uses an external source")
        for package, relative in packages.items():
            directory = (root / relative).resolve()
            if not directory.is_relative_to(root):
                errors.append(f"{package}: package escapes the repository")
                continue
            path = directory / "Cargo.toml"
            allowed_paths.add(path)
            data = manifest(path)
            spec = data["package"]
            if spec["name"] != package:
                errors.append(f"{relative}: package name differs from policy")
            if spec.get("links") or spec.get("build") not in (None, False) or (directory / "build.rs").exists():
                errors.append(f"{package}: native links/build scripts are not approved")
            if data.get("lints", {}).get("workspace") is not True:
                errors.append(f"{package}: must inherit the workspace unsafe-code boundary")
            for table_name, dependencies in dependency_tables(data):
                for alias, declaration in dependencies.items():
                    if not isinstance(declaration, dict):
                        errors.append(f"{package}: external dependency {alias} in {table_name}")
                        continue
                    actual = declaration.get("package", alias)
                    if declaration.get("workspace"):
                        declaration = shared.get(alias, {}) | {k: v for k, v in declaration.items() if k != "workspace"}
                        base = root
                        actual = declaration.get("package", alias)
                    else:
                        base = directory
                    location = (base / declaration.get("path", "")).resolve()
                    if actual not in packages or location != (root / packages.get(actual, "")).resolve():
                        errors.append(f"{package}: unapproved dependency {alias} in {table_name}")
                    if any(k in declaration for k in ("git", "registry", "registry-index")) or "path" not in declaration:
                        errors.append(f"{package}: nonlocal dependency source for {alias}")
            # Scan only application sources. Host utility names/implementation do not count.
            for source in directory.rglob("*.rs"):
                if "tests" in source.relative_to(directory).parts:
                    continue
                if not source.resolve().is_relative_to(root):
                    errors.append(f"{source}: source escapes the repository")
                    continue
                for number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
                    if line.lstrip().startswith("//"):
                        continue
                    if NATIVE.search(line):
                        errors.append(f"{source.relative_to(root)}:{number}: unreviewed unsafe/native-load/include seam")
        for path in root.rglob("Cargo.toml"):
            if any(part in ("target", ".git", "out") for part in path.relative_to(root).parts):
                continue
            if path.resolve() not in allowed_paths:
                errors.append(f"{path.relative_to(root)}: unreviewed Cargo package")
        for path in (root / ".cargo/config", root / ".cargo/config.toml"):
            if path.exists():
                errors.append("Cargo config requires explicit build/link policy review")
        lock = manifest(root / "Cargo.lock")
        lock_packages = lock.get("package", [])
        if {p["name"] for p in lock_packages} != set(packages) or len(lock_packages) != len(packages):
            errors.append("lockfile package closure differs from the reviewed inventory")
        if any(p.get("source") or p.get("checksum") for p in lock_packages):
            errors.append("lockfile contains unapproved registry/git dependencies")
        if cargo_metadata is not None:
            resolved = cargo_metadata.get("packages", [])
            if len(resolved) != len(packages) or {p["name"] for p in resolved} != set(packages):
                errors.append("all-feature Cargo metadata has an unapproved transitive package")
            for package in resolved:
                name = package["name"]
                expected = (root / packages.get(name, "") / "Cargo.toml").resolve()
                if package.get("source") or Path(package["manifest_path"]).resolve() != expected:
                    errors.append(f"{name}: resolved package source differs from the reviewed inventory")
                if any("custom-build" in target["kind"] for target in package["targets"]):
                    errors.append(f"{name}: resolved native build target is forbidden")
    except (KeyError, TypeError, ValueError, OSError) as error:
        errors.append(f"invalid architecture input: {error}")
    return sorted(set(errors))


def binary_dependencies(binary: Path) -> tuple[list[str], list[str]]:
    result = subprocess.run(["readelf", "-d", str(binary)], capture_output=True, text=True, check=True)
    needed = re.findall(r"\(NEEDED\).*?\[(.*?)\]", result.stdout)
    allowed = {"libgcc_s.so.1", "libc.so.6", "libm.so.6", "libpthread.so.0", "libdl.so.2", "librt.so.1", "ld-linux-x86-64.so.2"}
    return needed, [f"unapproved runtime library: {name}" for name in needed if name not in allowed]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--cargo-metadata", action="store_true")
    parser.add_argument("--binary", type=Path)
    args = parser.parse_args()
    metadata = None
    try:
        if args.cargo_metadata:
            result = subprocess.run(["cargo", "metadata", "--format-version", "1", "--all-features", "--locked", "--offline"], cwd=args.root, capture_output=True, text=True, check=True)
            metadata = json.loads(result.stdout)
        errors = check(args.root, metadata)
        if args.binary:
            needed, link_errors = binary_dependencies(args.binary)
            errors.extend(link_errors)
            print("Runtime libraries: " + ", ".join(needed))
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"architecture inspection failed: {error}", file=sys.stderr)
        return 1
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Architecture valid: approved local packages only; no unreviewed build/link/load seam.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
