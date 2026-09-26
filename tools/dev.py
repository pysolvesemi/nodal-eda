#!/usr/bin/env python3
"""Run the same bounded bootstrap checks locally and in CI."""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


def identity():
    def git(*args):
        return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()
    files = subprocess.check_output(["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=ROOT).decode().split("\0")
    hashes = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in sorted(set(files)) if name and (ROOT / name).is_file()}
    return {"commit": git("rev-parse", "HEAD"), "tree": git("rev-parse", "HEAD^{tree}"), "dirty": bool(git("status", "--porcelain")), "files_sha256": hashes}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase", choices=["targeted"])
    args = parser.parse_args()
    output = ROOT / "out"
    output.mkdir(exist_ok=True)
    results = {"phase": args.phase, "source": identity(), "commands": [], "outcome": "fail"}
    commands = [
        ["cargo", "fmt", "--all", "--", "--check"],
        ["cargo", "clippy", "--workspace", "--all-targets", "--all-features", "--locked", "--offline", "--", "-D", "warnings"],
        ["cargo", "test", "--workspace", "--all-features", "--locked", "--offline"],
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        [sys.executable, "tools/check_roadmap.py"],
        [sys.executable, "tools/check_architecture.py", "--cargo-metadata"],
        ["git", "diff", "--check"],
    ]
    try:
        with (output / "targeted.log").open("w") as log:
            for command in commands:
                print("+ " + " ".join(command), flush=True)
                start = time.perf_counter()
                run = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
                log.write("+ " + " ".join(command) + "\n" + run.stdout + run.stderr)
                log.flush()
                print(run.stdout + run.stderr, end="", flush=True)
                results["commands"].append({"argv": command, "exit_code": run.returncode, "elapsed_seconds": time.perf_counter() - start})
                if run.returncode:
                    return 1
            first = subprocess.check_output([sys.executable, "tools/check_roadmap.py"], cwd=ROOT)
            second = subprocess.check_output([sys.executable, "tools/check_roadmap.py"], cwd=ROOT)
            if first != second:
                raise ValueError("roadmap diagnostics are not deterministic")
            results["deterministic_roadmap_output"] = first.decode().strip()
            results["outcome"] = "pass"
            return 0
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        results["error"] = str(error)
        print(str(error), file=sys.stderr)
        return 1
    finally:
        (output / "targeted.json").write_text(json.dumps(results, indent=2) + "\n")


if __name__ == "__main__":
    raise SystemExit(main())
