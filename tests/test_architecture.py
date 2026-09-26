"""Mutate a real bootstrap copy; none of these fixtures imports an SDK."""

from pathlib import Path
import shutil
import tempfile
import unittest

from tools.check_architecture import check

ROOT = Path(__file__).resolve().parents[1]


class ArchitectureTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ("Cargo.toml", "Cargo.lock", "rust-toolchain.toml"):
            shutil.copy2(ROOT / name, self.root / name)
        for name in ("apps", "crates", "policy"):
            shutil.copytree(ROOT / name, self.root / name)

    def append(self, path, text):
        with (self.root / path).open("a") as stream:
            stream.write(text)

    def test_unmodified_application_boundary(self):
        self.assertEqual(check(self.root), [])

    def test_optional_compiler_library_cannot_hide_behind_feature(self):
        self.append("apps/cli/Cargo.toml", '\n[dependencies.mlir-sys]\nversion = "0.1"\noptional = true\n\n[features]\ncompiler = ["dep:mlir-sys"]\n')
        errors = check(self.root)
        self.assertTrue(any("unapproved dependency mlir-sys" in e for e in errors), errors)

    def test_renamed_compiler_dependency(self):
        self.append("apps/cli/Cargo.toml", '\n[dependencies.bridge]\npackage = "llvm-sys"\nversion = "190"\n')
        self.assertTrue(any("unapproved dependency bridge" in e for e in check(self.root)))

    def test_target_specific_build_dependency(self):
        self.append("apps/cli/Cargo.toml", '\n[target.\'cfg(unix)\'.build-dependencies]\ncc = "1"\n')
        self.assertTrue(any("external dependency cc" in e for e in check(self.root)))

    def test_cargo_override_is_rejected(self):
        self.append("Cargo.toml", '\n[patch.crates-io]\nbridge = { path = "vendor/bridge" }\n')
        self.assertTrue(any("patch/replace" in e for e in check(self.root)))

    def test_automatic_build_script_is_rejected(self):
        (self.root / "apps/cli/build.rs").write_text('fn main() { println!("cargo:rustc-link-lib=MLIR"); }\n')
        self.assertTrue(any("build scripts" in e for e in check(self.root)))

    def test_native_link_and_runtime_loading_are_rejected(self):
        source = self.root / "crates/eda-contracts/src/lib.rs"
        original = source.read_text()
        for seam in ['#[link(name = "MLIR")]\nunsafe extern "C" {}\n', 'fn load() { dlopen(); }\n', 'include!("generated.rs");\n']:
            with self.subTest(seam=seam):
                source.write_text(original + seam)
                self.assertTrue(any("native-load/include seam" in e for e in check(self.root)))

    def test_cargo_linker_override_is_rejected(self):
        (self.root / ".cargo").mkdir()
        (self.root / ".cargo/config.toml").write_text('[build]\nrustflags = ["-lMLIR"]\n')
        self.assertTrue(any("build/link policy review" in e for e in check(self.root)))

    def test_unreviewed_transitive_package_metadata(self):
        metadata = {"packages": [{"name": name, "source": None, "manifest_path": str(self.root / path / "Cargo.toml"), "targets": []} for name, path in [("eda-contracts", "crates/eda-contracts"), ("nodal-eda-cli", "apps/cli")]]}
        metadata["packages"].append({"name": "compiler-bridge", "source": "registry+test", "manifest_path": "/external/compiler/Cargo.toml", "targets": []})
        self.assertTrue(any("transitive package" in e for e in check(self.root, metadata)))

    def test_missing_lock_or_weakened_lints_is_rejected(self):
        path = self.root / "Cargo.toml"
        path.write_text(path.read_text().replace('unsafe_code = "forbid"', 'unsafe_code = "allow"'))
        self.assertTrue(any("forbid unsafe" in e for e in check(self.root)))
        (self.root / "Cargo.lock").unlink()
        self.assertTrue(any("invalid architecture input" in e for e in check(self.root)))

    def test_approved_host_utilities_do_not_become_application_dependencies(self):
        (self.root / "tools").mkdir()
        (self.root / "tools/llvm-host-notes.txt").write_text("rustc uses LLVM; cc/clang and coverage utilities are host tools.\n")
        self.assertEqual(check(self.root), [])


if __name__ == "__main__":
    unittest.main()
