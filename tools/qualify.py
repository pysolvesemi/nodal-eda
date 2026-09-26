#!/usr/bin/env python3
"""Clean offline release build, native dependency inspection and B0 CLI evidence."""

import hashlib
import json
import math
import os
from pathlib import Path
import platform
import resource
import shutil
import statistics
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.check_architecture import binary_dependencies, check  # noqa: E402
from tools.dev import identity  # noqa: E402


def command(argv, **kwargs):
    print("+ " + " ".join(map(str, argv)), flush=True)
    result = subprocess.run(argv, capture_output=True, text=True, **kwargs)
    print(result.stdout + result.stderr, end="", flush=True)
    result.check_returncode()
    return result.stdout


def main():
    output = ROOT / "out"
    output.mkdir(exist_ok=True)
    report = {"phase": "full", "source": identity(), "outcome": "fail"}
    try:
        if platform.system() != "Linux" or platform.machine() != "x86_64":
            raise ValueError("FND-01 qualification currently supports Linux x86-64 only")
        report["host"] = {"platform": platform.platform(), "cpu_count": os.cpu_count(), "cpu_model": next((line.split(":", 1)[1].strip() for line in Path("/proc/cpuinfo").read_text().splitlines() if line.startswith("model name")), "unknown"), "memory_kib": int(Path("/proc/meminfo").read_text().splitlines()[0].split()[1]), "python": platform.python_version()}
        report["rustc"] = command(["rustc", "--version", "--verbose"], cwd=ROOT)
        report["cargo"] = command(["cargo", "--version"], cwd=ROOT).strip()
        with tempfile.TemporaryDirectory(prefix="nodal-eda-clean-") as directory:
            scratch = Path(directory)
            bin_dir = scratch / "bin"
            bin_dir.mkdir()
            # Explicit build utilities only. No JVM, Nodal, LLVM SDK discovery tool or CAD engine.
            utilities = ["cargo", "rustc", "rustup", "cc", "gcc", "as", "ld", "ar"]
            paths = {}
            for name in utilities:
                resolved = shutil.which(name)
                if resolved is None:
                    raise ValueError(f"required host build utility is absent: {name}")
                (bin_dir / name).symlink_to(resolved)
                paths[name] = resolved
            report["allowed_build_utilities"] = paths
            rustup_home = os.environ.get("RUSTUP_HOME", str(Path.home() / ".rustup"))
            environment = {"PATH": str(bin_dir), "RUSTUP_HOME": rustup_home, "RUSTUP_TOOLCHAIN": "1.90.0", "CARGO_HOME": str(scratch / "cargo"), "CARGO_TARGET_DIR": str(scratch / "target"), "LANG": "C.UTF-8"}
            report["clean_build"] = {"fresh_target": True, "fresh_cargo_home": True, "offline": True, "all_features": True, "unavailable_commands": ["java", "javac", "nodal", "nodalc", "llvm-config", "mlir-opt", "circt-opt", "yosys", "nextpnr"]}
            for name in report["clean_build"]["unavailable_commands"]:
                if shutil.which(name, path=str(bin_dir)):
                    raise ValueError(f"unexpected external engine in clean path: {name}")
            command(["cargo", "build", "--workspace", "--release", "--all-features", "--locked", "--offline"], cwd=ROOT, env=environment)
            metadata_text = command(["cargo", "metadata", "--format-version", "1", "--all-features", "--locked", "--offline"], cwd=ROOT, env=environment)
            metadata = json.loads(metadata_text)
            errors = check(ROOT, metadata)
            if errors:
                raise ValueError("; ".join(errors))
            report["package_inventory"] = [{"name": p["name"], "version": p["version"], "source": p["source"]} for p in metadata["packages"]]
            binary = scratch / "target/release/nodal-eda"
            report["binary_sha256"] = hashlib.sha256(binary.read_bytes()).hexdigest()
            needed, errors = binary_dependencies(binary)
            report["runtime_libraries"] = needed
            if errors:
                raise ValueError("; ".join(errors))
            measurements = {}
            for argument in ["--help", "--version"]:
                samples = []
                before = resource.getrusage(resource.RUSAGE_CHILDREN)
                expected = None
                for index in range(56):
                    start = time.perf_counter_ns()
                    result = subprocess.run([str(binary), argument], env={}, capture_output=True, check=True)
                    duration_ms = (time.perf_counter_ns() - start) / 1_000_000
                    if result.stderr:
                        raise ValueError("CLI wrote unexpected stderr")
                    if expected is None:
                        expected = result.stdout
                        cold_ms = duration_ms
                    if result.stdout != expected:
                        raise ValueError("CLI output changed across identical invocations")
                    if index >= 6:
                        samples.append(duration_ms)
                after = resource.getrusage(resource.RUSAGE_CHILDREN)
                ordered = sorted(samples)
                p95 = ordered[math.ceil(0.95 * len(ordered)) - 1]
                measurements[argument] = {"cold_first_ms": cold_ms, "warmup_invocations": 6, "repetitions": len(samples), "p50_ms": statistics.median(samples), "p95_ms": p95, "samples_ms": samples, "user_cpu_seconds": after.ru_utime - before.ru_utime, "system_cpu_seconds": after.ru_stime - before.ru_stime, "output": expected.decode(), "p95_limit_ms": 250, "outcome": "pass" if p95 <= 250 else "fail"}
                if argument == "--version" and expected != b"nodal-eda 0.1.0\n":
                    raise ValueError("unexpected product version")
                if p95 > 250:
                    raise ValueError(f"{argument}: B0 p95 {p95:.3f} ms exceeds 250 ms")
            report["b0_cli"] = measurements
            # wait4 reports this product child's resources, excluding compiler/helper RSS.
            pid = os.posix_spawn(str(binary), [str(binary), "--help"], {}, file_actions=[
                (os.POSIX_SPAWN_OPEN, 1, os.devnull, os.O_WRONLY, 0),
                (os.POSIX_SPAWN_OPEN, 2, os.devnull, os.O_WRONLY, 0),
            ])
            _, status, usage = os.wait4(pid, 0)
            if os.waitstatus_to_exitcode(status) != 0:
                raise ValueError("RSS sample CLI invocation failed")
            report["help_peak_rss_kib"] = usage.ru_maxrss if usage.ru_maxrss > 0 else None
            report["rss_method"] = "Linux wait4 for a separate posix_spawn CLI child; null means the kernel supplied no positive sample"
            report["b0_control_document"] = {"outcome": "not_applicable", "reason": "FND-01 has no control-document parser; owned by FND-02 and later profile owners"}
            # Keep the demonstrated executable with its content identity in the CI artifact.
            shutil.copy2(binary, output / "nodal-eda")
        report["optimization_review"] = "Two local packages, no third-party graph, no tool startup, fixed help/version output; no new optimization required. Product schemas and scale workloads remain with their owning increments."
        report["outcome"] = "pass"
        print("Full FND-01 qualification passed.")
        return 0
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        report["error"] = str(error)
        print(str(error), file=sys.stderr)
        return 1
    finally:
        (output / "qualification.json").write_text(json.dumps(report, indent=2) + "\n")


if __name__ == "__main__":
    raise SystemExit(main())
