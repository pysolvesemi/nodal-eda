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

## Current checkpoint

No source implementation, remote qualification or merge has happened yet.
Next safe action: implement the bounded bootstrap and run its local checks.
The active worker owns this implementation; continuations must avoid competing
writes while the current session is publishing.

This increment does not affect generated Verilog (Verilog-*).
It establishes Rust product and repository infrastructure.
