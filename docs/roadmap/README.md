# Nodal-EDA incremental roadmap

## Objective and status

Build a high-performance, commercial-grade FPGA development product, beginning with a reproducible headless workflow and growing toward an integrated professional environment. Commercial grade is a release qualification outcome, not a consequence of choosing Rust or drawing a scalable architecture.

This roadmap is an implementation plan. All increment and subtask checkboxes start open. Follow the [completion policy](completion-policy.md): a completed subtask may be checked while its parent stays open until every required subtask and closure gate is satisfied.

The architectural baseline is the [ownership/directory plan](../architecture.md), [verification strategy](../verification.md), [stage-by-stage verification contract](../verification-pipeline.md), and [performance contract](../performance.md). External precedents and their limits are recorded in [research sources](../research-sources.md) and the verification contract's primary references. Commands and future schemas in these documents are proposed interfaces, not currently implemented commands.

## Rust and compiler-framework boundary

[ADR-0001](../adr/0001-rust-core-external-compiler-boundary.md) makes the long-term decision explicit: Nodal-EDA has a Rust core/CLI, with no required in-process LLVM/MLIR/CIRCT compiler infrastructure and no new Scala frontend. Nodal-HDL retains its MLIR-based compilation; Nodal-EDA invokes qualified compiler engines through versioned adapters and consumes artifacts, diagnostics and provenance. This remains the boundary for commercial and high-end profiles, not only the MVP.

Foundation must build and run core/fake-tool checks without separately installed compiler-framework SDKs or the Nodal compiler stack. TOOL-02/VER-02 qualify a traditional HDL path independently; TOOL-04 qualifies the actual Nodal compiler dependency and failure/upgrade isolation. VER-05/VER-06 repeat these gates for releases. Ordinary Rust/platform build utilities are not banned, and selected external compiler packages may contain MLIR/CIRCT. See the ADR's acceptance matrix for exact existing child-task ownership. These clarifications do not complete tasks or add an MLIR implementation track.

## Verification is part of the first real-device milestone

[verification-pipeline.md](../verification-pipeline.md) defines required stage artifacts, independent checkers, cycle/event semantics, timing distinctions and final-bitstream checks. Foundation's existing FND-02/FND-03/FND-06/FND-09/FND-10 children must establish its schema, capability, cache and mock-evidence contracts before real engines are integrated. These are mandatory acceptance details of those children, not optional later documentation or a new compiler dependency.

VER-02 validates direct versus orchestrated execution. VER-03 additionally checks original RTL against mapped behavior, independent packing/route legality, route-aware behavior and behavior reconstructed from the exact final binary. These are different guarantees. M1 now requires VER-03, which no longer depends on Nodal integration; TOOL-04 applies that qualified harness to actual Nodal exports afterward. Prefer a qualified Yosys/nextpnr/IceStorm iCE40 subset for the first bitstream-to-Verilog lane, without assuming every device or primitive is supported.

TOOL-05 requires simulated own-fabric configuration loading before boards are available. VER-04/HW-03 retain full integrated hardware and silicon gates. The task split prevents HDL/compiler or board availability from delaying the earliest reference-flow checks. All implementation checkboxes remain open; no documentation update is verification evidence.

## Track registry

| Track | File | Increments | Entry gate | Purpose |
| --- | --- | --- | --- | --- |
| FND | [Foundation](tracks/foundation.md) | FND-01..FND-10 | None | Contracts, executable skeleton, isolation, artifacts, reproducibility, bootstrap tests. |
| FLOW | [Build and execution](tracks/build-flow.md) | FLOW-01..FLOW-05 | FND-10 | Planning, orchestration, recovery, optional remote and hierarchical flows. |
| TOOL | [Toolchain and devices](tracks/toolchain.md) | TOOL-01..TOOL-05 | FND-10 | Qualified external flows, Nodal adapters, device packages, bring-up integration. |
| CON | [Constraints and analysis](tracks/constraints.md) | CON-01..CON-05 | FND-10 | Constraint semantics, honest reports, corners, power, advanced design planning. |
| HW | [Programming and hardware](tracks/hardware.md) | HW-01..HW-04 | FND-10 | Safe programmer, lab access, bring-up and production operations. |
| DBG | [Debug and traceability](tracks/debug.md) | DBG-01..DBG-04 | FND-10 | Source provenance, ILA orchestration, capture, advanced debug. |
| IP | [IP and generators](tracks/ip.md) | IP-01..IP-04 | FND-10 | Reproducible IP packages and qualified generators. |
| UX | [CLI and desktop experience](tracks/user-experience.md) | UX-01..UX-04 | FND-10 | Shared headless APIs and scalable optional desktop views. |
| REL | [Distribution and qualification](tracks/release.md) | REL-01..REL-05 | FND-10 | Installability, device releases, support, professional product qualification. |
| PERF | [Performance and scalability](tracks/performance.md) | PERF-01..PERF-04 | FND-10 | Measured overhead, bounded queries, concurrency, large workloads. |
| SEC | [Security and trust](tracks/security.md) | SEC-01..SEC-04 | FND-10 | Untrusted inputs, signed delivery, multi-user isolation, audit. |
| VER | [Verification and quality](tracks/verification.md) | VER-01..VER-06 | FND-10 | Independent oracles, synthesis/route/bitstream checks, differential/formal testing, fault injection and release evidence. |

There are **12 tracks, 60 parent increments, 360 immediate child tasks and 18 further nested verification subtasks**. Each parent has six named immediate children; VER-03's children have individually checkable descendants. Additional dependencies appear in the individual increment; the table is not a substitute for those dependencies.

## Foundation gate and concurrency

```text
FND-01 -> FND-02 -> ... -> FND-09 -> FND-10
                                             |
             +----------+----------+---------+---------+
             |          |          |         |         |
           FLOW        TOOL       CON       VER      SEC
             |          |          |         |         |
             +----- dependencies listed per increment -+
             |          |          |         |         |
            HW         DBG         IP        UX      PERF
                                             |
                                            REL
```

Every non-foundation implementation increment is blocked until **all foundation work through FND-10 is complete**. This does not postpone testing: foundation contains real mock-tool, schema, fault, and determinism tests. Subsequent tracks may run in parallel only when their additional predecessors and external capability contracts are satisfied.

TOOL-03 is an optional FABulous reference integration, not a mandatory predecessor of own-device or commercial qualification. Mandatory independent configuration, behavior and flow verification remains in VER-01 through VER-06 even when that optional adapter is unavailable. VTR/OpenFPGA are optional methodological or qualified same-architecture references, not additional universal dependencies.

## Product stages

| Stage | Exit gate | Demonstration and boundary |
| --- | --- | --- |
| M0: executable foundation | FND-10 | Validated project -> fake-tool actions -> durable artifacts, failure recovery and reproducible replay; stage-evidence contracts and negative fixtures. No real device support claimed. |
| M1: headless open-device MVP | FLOW-03, TOOL-02, CON-02, VER-02, VER-03 | Qualified reference synthesis/P&R/packer flow with direct-tool comparison, mapped equivalence, route legality and actual-final-bitstream behavior checks. Timing completeness is separate. No Nodal compiler or physical board prerequisite for these checks. |
| M2: own-fabric bring-up/tapeout support | TOOL-05, VER-04, HW-03, REL-01 | Same pinned user-design corpus through own-fabric actual-loader simulation/emulation and safe hardware workflows. Silicon results are required before calling silicon bring-up complete. This product does not perform foundry signoff. |
| M3: first commercial device/tool release | REL-03 | Qualified device/package/OS matrix, offline installation, secure programming, support bundle, documented language/constraint support and release evidence. GUI features are optional unless advertised. |
| M4: mid-range/team scale | REL-04 | Resource-bounded parallel builds, controlled remote execution, shared-cache trust, QoR and compatibility baselines. |
| M5: high-end professional profile | REL-05 | Only engine-supported hierarchical/multi-die/partial-reconfiguration workflows; large-query UI, secure fleet operation, independent qualification and silicon correlation. |

Gate predecessors are transitive. External simulator, compiler, bitstream encoder, device, board, or signoff deliverables must actually exist and be qualified. Absence leaves the relevant subtask open; use the mock/reference backend to continue unrelated product development.

## Prioritized first twenty increments

Execute these in order for a small team; eligible independent work can be parallelized later.

| Order | ID | Result |
| --- | --- | --- |
| 1 | FND-01 | Scope, ownership, repository skeleton and roadmap checker. |
| 2 | FND-02 | Versioned contract types, semantic/evidence identities and compatibility rules. |
| 3 | FND-03 | Tool adapter handshake, checkable-artifact capabilities and executable fake tool. |
| 4 | FND-04 | Validated project and dependency lock model. |
| 5 | FND-05 | Process runner with safe cancellation and bounded I/O. |
| 6 | FND-06 | Content-addressed artifacts and safe cache publication, including proof identity. |
| 7 | FND-07 | Durable events, diagnostics and restart state. |
| 8 | FND-08 | Initial trust policy and package validation. |
| 9 | FND-09 | Bootstrap CI, stage-evidence negative fixtures and performance harness. |
| 10 | FND-10 | Foundation acceptance closes the common gate. |
| 11 | VER-01 | Independent oracle, SemanticContract corpus and evidence harness. |
| 12 | TOOL-01 | Pinned toolchain/device-package capability resolution. |
| 13 | CON-01 | Constraint subset and coverage accounting. |
| 14 | FLOW-01 | DAG planner and resource-aware scheduler. |
| 15 | TOOL-02 | One checkable open-device synthesis/P&R/packer adapter. |
| 16 | FLOW-02 | Real headless project-to-bitstream workflow. |
| 17 | VER-02 | Direct-tool differential validation. |
| 18 | FLOW-03 | Safe cache reuse, resume and support reproduction. |
| 19 | CON-02 | Structured reports and timing-completeness gate. |
| 20 | VER-03 | Original RTL -> mapped -> routed -> final binary -> reconstructed-behavior qualification. |

After these, prioritize SEC-01, PERF-01/PERF-02, TOOL-04, HW-01/HW-02 and REL-01 according to device availability. TOOL-03 remains an optional FABulous reference and may run when its prerequisites and qualified fabric are available; it is moved out of the first twenty to prioritize mandatory semantic verification, not deleted or marked complete. Do not fabricate a pass to preserve the numerical schedule.

## What not to build initially

Do not create a new synthesizer, router, STA engine, FPGA fabric generator, SPICE simulator, GDS engine, general-purpose distributed build system, mandatory daemon, custom editor, or new Scala DSL here. Independent validation/test-oracle code checks outputs rather than duplicating implementation algorithms. Do not make the GUI or a cloud account a prerequisite for CLI builds. Do not promise universal SystemVerilog/VHDL, SDC, timing signoff, high-end-device support, or byte-identical outputs across arbitrary external-tool versions.

## Required evidence per increment

Each increment specifies its user capability, module/schema boundary, dependencies, tests, performance profile, non-goals and exit. Its last child covers integrated qualification and evidence. The named budget profiles are in [performance.md](../performance.md); they are initial acceptance targets, not measured results. Keep workload definitions stable and revise budgets explicitly rather than weakening them to conceal regressions.

Apply the stage-by-stage contract's owner table as required acceptance detail of existing Foundation, Toolchain, Constraints and Verification children. Successful tool execution, cycle-correct behavior, legal routing, timing closure and actual silicon qualification are separate results. A child with open grandchildren stays open; a parent with any required open descendant stays open.

Completion reports include actual CLI/API examples. Include actual Nodal source/generated Verilog when the increment affects that path; otherwise explicitly state that the increment does not affect generated Verilog (Verilog-*).
