# FND-01 bootstrap design and supported profile

## Product and ownership

The product now starts as a two-package Rust workspace. `eda-contracts` owns
the immutable product identity. `apps/cli` owns the `nodal-eda` help/version
entry point and rejects all other commands. It starts no engine, GUI, daemon or
JVM and reads no project files. Unknown arguments return exit status 2 without
panicking on non-Unicode input. No FND-02 protocol schema is preimplemented.

| Boundary | Owner and integration point | FND-01 acceptance |
| --- | --- | --- |
| Product identity and CLI | nodal-eda, contracts and CLI packages | Real build and binary-level behavior tests. |
| Language compilation and source provenance | Nodal-HDL; TOOL-04 owns the future adapter | Interface ownership recorded; no CLI/export/source-map support presumed. |
| Device/CAD/configuration models | Nodal-FPGA; TOOL-05 owns the future adapter | Interface ownership recorded; no DeviceDB, mapping or bitstream capability presumed. |
| Conventional HDL synthesis/P&R | Qualified external engines; TOOL-02 and VER-02/VER-03 | No integration or real-device claim in FND-01. |
| Repository maintenance and CI | nodal-eda Python host utilities and bootstrap workflow | Executable policy checks and actual candidate qualification. |

This ratifies [ADR-0001](../adr/0001-rust-core-external-compiler-boundary.md).
Nodal-EDA consumes versioned files/results from future external providers; it
does not own compiler IR, synthesis, routing, timing or fabric-generation code.
The reviewed current graph is `nodal-eda-cli -> eda-contracts`, with no external
Cargo packages. A new package/feature/native seam needs explicit review.

## Roadmap checker

`tools/check_roadmap.py` reads every Markdown track under `docs/roadmap/tracks`.
It validates stable IDs, numeric ancestry and indentation, duplicate/malformed
tasks, declared prerequisites, the implicit non-Foundation FND-10 gate, cycles,
closed ancestors with open descendants, and evidence file/heading references.
Backtick and tilde fences are ignored with their actual closing length. Later
consumer references in ordinary prose are not prerequisite edges.

The accepted dependency grammar is comma-separated increment IDs with optional
`and`, `none`, or `all earlier <TRACK> increments`. Missing, duplicated or
unknown dependency declarations fail. Graph traversal is iterative; a long DAG
does not depend on Python's recursion limit. Checked leaf progress never writes
or automatically checks its parent. Empty tracks fail rather than passing vacuously.

The independent fixtures include partial and fully closed trees, cycles,
premature closure, orphan/duplicate IDs, missing evidence/anchors, external or
escaping evidence paths and malformed fences. Link checks are structural;
actual test results and closure evidence still require review.

## Architecture checker

`tools/check_architecture.py` compares manifests, all dependency tables,
toolchain, lockfile and all-feature Cargo metadata against the reviewed policy.
It rejects unapproved optional/transitive packages, workspace overrides,
automatic build scripts, Cargo linker configuration and unreviewed unsafe/native
link/load/include seams. Actual ELF `NEEDED` libraries must be in the declared
Linux system-runtime set. It checks application sources rather than banning
LLVM-based host compilers or ordinary maintenance tools.

Mutants exercise optional/renamed compiler dependencies, target-specific build
dependencies, automatic linker scripts, Cargo overrides, dynamic loading,
transitive metadata and weakened lint configuration. Positive controls preserve
the real application graph and permitted host-tool notes. These are policy
tests, not execution of a real MLIR SDK or a sandbox for adversarial Rust code.
Static seam checks complement complete source review and a compiler-independent
clean build; they do not prove arbitrary future code safe.

## Measurement and extension limits

FND-01 supports Linux x86-64. `qualify.py` records the actual host, compiler,
source/tree and source-file hashes, clean build environment, package inventory,
binary digest, ELF libraries, first-invocation and 50 warmed samples per command,
p50/p95, CPU time, product RSS and exact CLI output. The B0 gate is p95 <= 250 ms
for help and version. First-invocation timing is recorded separately and is not
a claim that the OS page cache was flushed.

There is no control-document parser yet, so B0's 10 MiB document case belongs
to FND-02 and later owners. Broader B1-B8 or other host profiles are not claimed.
FND-09 will consolidate the already executable suites; it is not a prerequisite
for this increment. No additional optimization is currently warranted for fixed
help/version text and a two-package graph; retain the measured evidence before
expanding startup work or dependency closure.

The workflow uses pinned checkout/upload-artifact revisions and read-only
repository permissions. The targeted job runs the affected bootstrap suite;
the full job starts afterward and adds clean release/native-load/B0 checks.
They share the same exact candidate identity. The branch-specific bootstrap
trigger deliberately does not add a broad default-branch CI dependency.

This increment does not affect generated Verilog (Verilog-*).
