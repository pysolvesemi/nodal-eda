# FND-01 — Workspace, ownership and progress discipline

## Readiness audit — 2026-09-26

Historical readiness phase: implementation preparation; no implementation or CI pass was claimed at this audit.
Repository: pysolvesemi/nodal-eda.
Integration target: dev at fc512e72cfdf49f672ff799d73c29789e36efd75.
Target tree: 97dbe634db70bf368a25061174f219032496de58.
Increment branch: increment/fnd-01-bootstrap.
At readiness, the parent and all children remained open.

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

The implementation below was qualified on its exact candidate and integrated
through PR #1. The acceptance section records the actual execution and merge.

| Obligation | Delivered source and evidence owner |
| --- | --- |
| FND-01.1 | Root Cargo/toolchain/lock files, crates/eda-contracts, apps/cli; four binary-level integration tests exercise help/version, invalid commands and non-Unicode arguments. |
| FND-01.2 | docs/development/fnd-01.md, CONTRIBUTING.md and policy/architecture.toml ratify ownership and the two-package, zero-third-party application closure. |
| FND-01.3 | tools/check_roadmap.py validates task ancestry, prerequisites/cycles, Foundation gates and checked-task evidence locators without writing status. |
| FND-01.4 | tests/test_roadmap.py contains independent miniature roadmaps; docs/evidence/template.md specifies durable evidence and truthful source/merge identity. |
| FND-01.5 | CONTRIBUTING.md, architecture checker/mutants and the scoped .github/workflows/fnd-01.yml provide executable repository boundaries and the bootstrap route. |
| FND-01.6 | tools/dev.py and tools/qualify.py retain exact runtime source identities, clean builds, linked libraries, actual CLI output and B0 observations. Actual remote qualification/review/integration is recorded below. |

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
negative regression cases are included. Published-head self-review is recorded below.

## Acceptance

The implementation was accepted through [PR #1](https://github.com/pysolvesemi/nodal-eda/pull/1).

- Tested source: `d2b27088c40c96d8e61559e0d43e69ac72cf9770`.
- Tested tree: `e1daa082b12abe05f602beb58bd5bfb492976413`.
- Workflow: `.github/workflows/fnd-01.yml`, ID `367536711`, definition blob `9b8cff5531bdbcdfb56e3ecabc9a54231d33043b`.
- Actual [run 36224808624](https://github.com/pysolvesemi/nodal-eda/actions/runs/36224808624), attempt 1, event `push`, branch `increment/fnd-01-bootstrap`.
- Targeted job `108356651326` succeeded: formatting/lint, four Rust tests, 33 Python tests, roadmap/architecture and diff checks. No applicable job or test was skipped.
- Full job `108356689990` started after targeted success and passed the clean release, all-feature dependency/native-load and B0 requirements.
- Both downloaded artifact digests, clean checkout identity, tree and all 45 source-file hashes were independently compared with the Git commit.
- Targeted artifact `10899914232`: SHA256 `b3d3608451ffa954df8c4b4b6567478b3f0fa4bdc43483e1dda545712b96a7cb`.
- Full artifact `10900630956`: SHA256 `0a4b0704a20a252be9a4f97089efd240657edd6734206199fdc36f2ab14b4fc0`.
- Demonstrated binary SHA256: `2e86f5c4bd099bd7d5287cddd8874ff9a45cf4ffc78d3e4d5081d122bbe71a54`.

The remote host was Linux x86-64, kernel 6.17.0-1022-azure, glibc 2.39,
4 logical CPUs (AMD EPYC 9V74), 16,373,452 KiB RAM, Python 3.12.3 and Rust 1.90.0.
This is the actual declared CI profile, not a claim to have measured the future
8-CPU/32-GiB reference-host calibration. The application has two local packages
and no registry/git package dependency. ELF runtime libraries were libc.so.6
and libgcc_s.so.1. The fresh, offline build used no Nodal/JVM/compiler SDK.

| Actual command | Warm samples | p50 | p95 | B0 limit |
| --- | --- | --- | --- | --- |
| `nodal-eda --help` | 50 | 0.764627 ms | 0.865221 ms | 250 ms |
| `nodal-eda --version` | 50 | 0.794386 ms | 0.891280 ms | 250 ms |

The product-child wait4 peak was 20,480 KiB including process launch effects.
The optimization review found no justified additional startup/graph optimization.
The fixture suites retain malformed-input and dependency/build/load rejection
controls. Broader document/engine/device/performance profiles remain with their
existing owners; they are not counted as executed here.

Actual CLI output retained in the full artifact:

```text
$ nodal-eda --version
nodal-eda 0.1.0

$ nodal-eda --help
Nodal-EDA — FPGA development workflow

Usage: nodal-eda [--help | --version]

Options:
-h, --help       Show this help
-V, --version    Show the product version

This bootstrap provides help and version commands.
```

Review kind: agent self-review of the complete exact-head diff, ownership,
negative controls, real logs/artifacts, dependencies, trigger/permission scope,
measurement limits and demonstrations. No independent human approval is claimed.
The live repository had no required review rules or unresolved review requests;
both actual check contexts passed before integration.

Actual implementation merge: `17cd9902f44a832f81cd7df52bd8cc488ac8d3bb`.
Its ordered parents were `fc512e72cfdf49f672ff799d73c29789e36efd75` and the
qualified source `d2b27088c40c96d8e61559e0d43e69ac72cf9770`. GitHub's merged flag,
commit message, final dev ref and identical tree were verified after the merge.
The merge message contains `[skip ci]`; zero runs were found for its actual SHA.
`post_merge_ci: skipped`, reason: `qualified-identical-tree-merge`.
Those are merge/suppression facts, not invented post-merge test execution.

## Evidence and checklist closure

All fifteen FND-01 leaf obligations have their implementation and applicable
execution evidence above; the six child groups retain every original obligation.
The evidence/checklist publication uses the same increment branch after the
verified implementation merge. Its checked state becomes authoritative only
when that documentation candidate passes its applicable targeting/full checks,
review and verified identical-tree merge into dev. The follow-up closure PR,
linked from PR #1, records its own actual run/head/merge identities; preceding
head results are not relabeled as execution on the closure head.

No later increment or dependent track is started. The hourly continuation is
kept enabled through evidence integration and the completion demonstration, then
paused after closure. This record keeps actual implementation merge facts and
uses the PR/run records for subsequent publication facts without a self-referential
commit hash or fabricated future receipt.

This increment does not affect generated Verilog (Verilog-*).
It establishes Rust product and repository infrastructure.
