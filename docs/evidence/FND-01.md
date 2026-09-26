# FND-01 — Workspace, ownership and progress discipline

## Readiness audit — 2026-09-26

Phase: implementation preparation; no implementation or CI pass claimed.
Repository: pysolvesemi/nodal-eda.
Integration target: dev at fc512e72cfdf49f672ff799d73c29789e36efd75.
Target tree: 97dbe634db70bf368a25061174f219032496de58.
Increment branch: increment/fnd-01-bootstrap.
Parent and all children remain open.

Read the live AGENTS.md, full FND-01 checklist, roadmap index, completion policy,
architecture, ADR-0001, performance contract and stage-verification ownership.
At audit time the repository contains 23 documentation files, no implementation
workspace, no workflow files, no existing PR and no competing increment branch.
There are no predecessor increments. No checklist correction is needed.

## Obligation dispositions

All fifteen existing leaves are required now. This table records applicability
and planned validation; it is not a second progress ledger.

| IDs | Disposition and owning implementation/validation |
| --- | --- |
| FND-01.1.1, FND-01.1.2 | Required: two-member Cargo workspace, pinned toolchain/lock, product identity and CLI help/version; binary-level CLI tests, formatting and lint checks. |
| FND-01.2.1, FND-01.2.2 | Required: documented repository/interface ownership and ADR-0001 ratification; inspect manifests, features, full Cargo dependency metadata, native link/load paths and actual binary dependencies. |
| FND-01.3.1, FND-01.3.2, FND-01.3.3 | Required: roadmap checker for nesting/IDs, explicit and Foundation-gate dependencies, cycles, descendant status and evidence links; independent positive/negative fixtures. |
| FND-01.4.1, FND-01.4.2 | Required: fixture corpus and documented durable evidence format; partial-progress, malformed/missing evidence, cycle and fenced-example cases. |
| FND-01.5.1, FND-01.5.2, FND-01.5.3 | Required: contribution/dependency guidance, architecture checks with forbidden-dependency and native-load mutants plus approved host-utility controls, and minimal remote bootstrap workflow. |
| FND-01.6.1, FND-01.6.2, FND-01.6.3 | Required: clean compiler-independent build, measured B0 CLI startup, deterministic checks and optimization review, exact-source remote qualification, review, verified integration and actual CLI report. |

No required obligation is optional, waived, transferred or marked complete.
FND-01 has no project/control-document parser: B0's 10 MiB control-document
validation belongs to FND-02 and later owning increments. FND-01 retains the
applicable help/version p95 <= 250 ms requirement on a declared Linux x86-64 host.
Other host profiles are not claimed. Product schemas, tool execution, caching,
real HDL compilation, FPGA integration and generated Verilog remain with their
existing later owners; none is claimed by this bootstrap.

## Implementation and dependency boundary

Create only crates/eda-contracts and apps/cli. The first shared contract is
product identity; do not preimplement FND-02 schemas. Use Rust 1.90.0, edition
2024, and zero third-party Cargo dependencies. Python 3.11+ standard-library
maintenance checks are host utilities, not product runtime dependencies.

Nodal-HDL owns compilation/export/provenance and is integrated by TOOL-04.
Nodal-FPGA owns device/CAD/configuration contracts and is integrated by TOOL-05.
No API capability from either is presumed available or required by FND-01.
Use interfaces and artifacts rather than in-process compiler infrastructure.

## Qualification route and evidence rules

The sole planned workflow is .github/workflows/fnd-01.yml, with a push trigger
restricted to increment/fnd-01-bootstrap and relevant bootstrap paths.
workflow_dispatch will also be defined for when GitHub registration permits it.
No default-branch or main update is needed. Use contents: read only.

A targeted job runs formatting/lint, Rust CLI tests, independent maintenance
fixtures and repository checks. A dependent full-qualification job starts only
after targeting succeeds, performing the clean release build, all-feature
dependency/native-link audit, actual CLI demonstration and B0 measurements.
The final applicable inventory includes both jobs; no duplicate successful
same-head checks are needed. Retain exact checkout commit/tree and actual logs.
An unavailable/failed job keeps FND-01 open.

Local checks precede publication. Publish the initial readiness record with
[skip ci], open one draft PR, and enable one hourly continuation as instructed.
The implementation trigger commit will intentionally omit a skip annotation
after inspecting live matching workflows. Preserve failures and repair only
affected requirements on a new head. Merge only after qualification and review,
then verify the identical tree and record suppressed duplicate post-merge CI.

## Implementation evidence

Implementation is prepared in the FND-01 branch. Remote qualification and
verified integration remain required; the authoritative checklist is still open.

| Obligation | Delivered source and evidence owner |
| --- | --- |
| FND-01.1 | Root Cargo/toolchain/lock files, crates/eda-contracts, apps/cli; four binary-level integration tests exercise help/version, invalid commands and non-Unicode arguments. |
| FND-01.2 | docs/development/fnd-01.md, CONTRIBUTING.md and policy/architecture.toml ratify ownership and the two-package, zero-third-party application closure. |
| FND-01.3 | tools/check_roadmap.py validates task ancestry, prerequisites/cycles, Foundation gates and checked-task evidence locators without writing status. |
| FND-01.4 | tests/test_roadmap.py contains independent miniature roadmaps; docs/evidence/template.md specifies durable evidence and truthful source/merge identity. |
| FND-01.5 | CONTRIBUTING.md, architecture checker/mutants and the scoped .github/workflows/fnd-01.yml provide executable repository boundaries and the bootstrap route. |
| FND-01.6 | tools/dev.py and tools/qualify.py retain exact runtime source identities, clean builds, linked libraries, actual CLI output and B0 observations. Final remote qualification/review/integration is pending. |

Local pre-publication checks passed: rustfmt, Clippy with warnings denied,
four Rust binary-level tests, 33 Python maintenance tests, live roadmap and
all-feature architecture checks. These are dirty-worktree repair evidence, not
qualification of a published candidate. Local reports/logs are in ignored out/;
remote jobs will generate their own exact-head records and immutable artifacts.

The Linux x86-64 clean release build used Rust 1.90.0, an empty Cargo home and
fresh target directory, --locked --offline --all-features, and an explicit PATH
containing only approved build tools. Java, Nodal, llvm-config, mlir-opt,
circt-opt, Yosys and nextpnr were absent from that PATH. Actual ELF dependencies
were libgcc_s.so.1 and libc.so.6. The Rust compiler's own LLVM implementation is
an allowed host utility and is not an application runtime dependency.

A local 50-sample warm run measured help p95 1.087 ms and version p95 0.860 ms
against the unchanged 250 ms B0 limit. Full distributions, exact host and CPU
observations are emitted by qualify.py; these local observations are not the
final remote benchmark. The wait4 RSS sample is a process-lifetime peak and may
include launch effects, not an isolated allocator measurement.

Preserved local failure: the first clean-build measurement attempt completed
compilation and CLI timing but failed because /usr/bin/time was unavailable.
It was not counted as a full pass. The revised harness uses posix_spawn/wait4
for the actual child resource sample without adding that helper dependency;
subsequent local qualification passed. No budget or correctness gate was removed.

Review so far: explicit self-review of the workspace, CLI, parser/graph logic,
fixtures, dependency/feature/build/load coverage and exact-branch workflow
permissions. This is not an independent human approval. The parser review found
and repaired an empty-track vacuous pass and malformed-root handling; their
negative regression cases are included. Final published-head review is pending.

## Current checkpoint

Phase: local implementation complete; ready for exact-head remote targeting.
Draft PR: https://github.com/pysolvesemi/nodal-eda/pull/1.
One hourly continuation is enabled for this increment.
Next safe action: publish the reviewed implementation without a skip annotation
so the isolated bootstrap push trigger runs. The full job is gated by targeted
success. Re-read live refs and matching workflows immediately before publication.
The active worker owns this implementation; continuations must avoid competing
writes while the current session is publishing.

This increment does not affect generated Verilog (Verilog-*).
It establishes Rust product and repository infrastructure.
