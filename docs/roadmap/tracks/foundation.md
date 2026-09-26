# FND — Foundation track

This track establishes executable contracts, not only design documents. All other tracks are blocked by FND-10. Foundation has its own tests and does not depend on VER. Follow the [completion policy](../completion-policy.md) and [performance profiles](../../performance.md). Checkboxes record evidenced implementation progress; unfinished work remains open.

The compiler-independent core acceptance rules in [ADR-0001](../../adr/0001-rust-core-external-compiler-boundary.md) are part of FND-01, FND-09 and FND-10. They apply to application dependencies, not the implementation of approved Rust/platform build utilities.

## Foundation checklist structure and acceptance

This structure follows Nodal's independently evidenced parent/child approach,
adapted to a Rust EDA product. Preserve the ten increment IDs and all existing
`FND-NN.1` through `FND-NN.6` identities and requirements. Numeric grandchildren
such as `FND-03.2.1` split their compound deliverables; they do not renumber them.
The existing child text remains part of acceptance even after it is split.

A leaf may be checked when its own deliverable and applicable evidence exist.
Its ancestors remain open until every required descendant and the complete
[closure predicate](../completion-policy.md#parent-closure-predicate) are
satisfied, including dependencies, review, demonstration, verified integration
and any required evidence closure. Progress is measured at required leaves;
formatting, applicability review and a successful build alone do not complete
implementation or independent qualification.

Before starting each increment, apply the
[readiness gate](../../../AGENTS.md#pre-implementation-increment-readiness-gate).
Retain the selected feature/profile, applicability decisions, actual validation
owners, rejected cases and scope limits in its evidence record. Do not silently
remove, waive or check required work to close a parent. The checklist migration itself asserted no implementation or executed tests;
subsequent checked work must cite its own actual evidence.

### Review perspectives

These perspectives carry Nodal's A-G intent without replacing the existing
numeric IDs or creating a second editable status list. Their actual deliverables
are assigned to the feature-specific children below.

| Perspective | Foundation application |
| --- | --- |
| A: architecture, scope and extensibility | Reuse typed contracts and existing modules; respect product/engine ownership, actual prerequisites and supported profile limits. |
| B: implementation and integration | Deliver the owning Rust contracts, CLI, adapter, execution, cache or run-state behavior; keep prototypes distinct from end-to-end capability. |
| C: correctness, rejection and predecessor regression | Check positive/boundary/malformed cases and real predecessor interactions; retain fault or mutation controls for critical guards. |
| D: independent validation and applicability | Use separately authored fixtures, independent consumers and reference state machines. Distinguish a schema round-trip, successful process, validated artifact and semantic proof; required unavailable execution stays blocked. |
| E: optimization review and output quality | Review startup, repeated scans/parsing, copying, allocation, buffers and diagnostic/artifact quality. A justified no-new-optimization result is valid; preserve correctness and trust checks. |
| F: scale, determinism and compatibility | Measure the applicable existing B0-B3 contracts on a declared host, with representative source/action/artifact/event sizes, reproducible output and schema compatibility. |
| G: evidence, documentation and acceptance | Keep exact commands, source/tree and artifact identities, actual CLI/API demonstrations, qualification, review and verified integration under the shared completion policy. |

Independent HDL simulation, synthesis, route/bitstream checks and numerical
analog validation apply only to their real-tool owners. Foundation uses fake
tools and independently specified contract/fault fixtures; it neither requires
generated Verilog nor claims real device or compiler qualification. If a later
change genuinely affects generated RTL, apply the actual source/output
demonstration rule in AGENTS.md.

### Validation staging without dependency cycles

FND-01 establishes the minimal self-contained remote build/help, documentation
and architecture-boundary lane. FND-02 through FND-08 extend that lane with their
own applicable tests and measured budgets. FND-09 consolidates the harness and
fault/compatibility/performance coverage; it is not a reverse prerequisite for
earlier increments. FND-10 qualifies the integrated Foundation.

Follow the centralized
[targeted-first CI policy](../../../AGENTS.md#targeted-ci-before-full-ci),
[hourly continuation](../../../AGENTS.md#hourly-continuation-through-closure)
and [verified-merge policy](../../../AGENTS.md#verified-merge-with-post-merge-ci-suppressed).
At an early increment, the full applicable suite means all requirements of the
implemented scope and its predecessors, not unimplemented future tracks.

Foundation depends on neither Nodal nor Nodal-FPGA implementation completion and
must not acquire a cycle through VER. Retain later execution owners:
TOOL-02/VER-02/VER-03 for the real conventional-HDL flow, TOOL-04 for the actual
Nodal compiler adapter, TOOL-05/VER-04 for own-fabric integration and DBG-05 for
Nodal/own-fabric debug. Those references are future consumers, not Foundation
prerequisites; fake qualification never grants them test credit.

## Increment checklist

- [x] **FND-01 — Workspace, ownership and progress discipline** Evidence: [FND-01 acceptance](../../evidence/FND-01.md#acceptance)
  - **Depends on:** none.
  - **Capability / modules:** Build a minimal Rust CLI; establish ownership and `eda-contracts` plus `apps/cli`, maintenance tools and ADRs.
  - **Budget / non-goals:** B0; no empty future-crate forest, GUI, MLIR/CIRCT compiler-framework dependency or CAD algorithm implementation.
  - [x] **FND-01.1** Establish Cargo workspace, pinned toolchain, application lockfile, formatting/lint policy and a minimal version/help command. Evidence: [FND-01 acceptance](../../evidence/FND-01.md#acceptance)
    - [x] **FND-01.1.1** Create the minimal Cargo workspace, pinned Rust toolchain and application lockfile; keep only the contracts and CLI modules needed for this increment. Evidence: [FND-01 acceptance](../../evidence/FND-01.md#acceptance)
    - [x] **FND-01.1.2** Implement version/help and the formatting/lint entry points; demonstrate a clean build and usable CLI without creating empty future crates. Evidence: [FND-01 acceptance](../../evidence/FND-01.md#acceptance)
  - [x] **FND-01.2** Ratify the architecture ownership table and ADR-0001 dependency rules; identify interface owners in nodal-hdl and nodal-fpga without asserting their unverified capabilities. Evidence: [FND-01 acceptance](../../evidence/FND-01.md#acceptance)
    - [x] **FND-01.2.1** Review the product/engine ownership table and record the Nodal-HDL and Nodal-FPGA interface owners, unknown capabilities and future integration owners. Evidence: [FND-01 acceptance](../../evidence/FND-01.md#acceptance)
    - [x] **FND-01.2.2** Ratify ADR-0001 across direct/transitive dependencies, Cargo features and build/link/load paths; distinguish application compiler libraries from approved host utilities. Evidence: [FND-01 acceptance](../../evidence/FND-01.md#acceptance)
  - [x] **FND-01.3** Implement documentation checks for unique increment/child IDs, task nesting, valid dependencies, cycles and closed parents with open descendants; ignore fenced examples. Evidence: [FND-01 acceptance](../../evidence/FND-01.md#acceptance)
    - [x] **FND-01.3.1** Parse Markdown task nesting and stable IDs, ignoring fenced examples; reject duplicate IDs, malformed nesting and missing parents. Evidence: [FND-01 acceptance](../../evidence/FND-01.md#acceptance)
    - [x] **FND-01.3.2** Validate dependency references and detect actual prerequisite cycles; distinguish a later consumer reference from a dependency edge. Evidence: [FND-01 acceptance](../../evidence/FND-01.md#acceptance)
    - [x] **FND-01.3.3** Reject closed tasks with required open descendants or missing evidence; accept legitimate partial child progress without automatically closing ancestors. Evidence: [FND-01 acceptance](../../evidence/FND-01.md#acceptance)
  - [x] **FND-01.4** Add tests proving partial child completion is accepted while premature parent closure and invalid dependencies fail; define the evidence-record format. Evidence: [FND-01 acceptance](../../evidence/FND-01.md#acceptance)
    - [x] **FND-01.4.1** Add independently authored valid/invalid roadmap fixtures covering partial progress, premature closure, missing evidence, invalid dependencies and fenced examples. Evidence: [FND-01 acceptance](../../evidence/FND-01.md#acceptance)
    - [x] **FND-01.4.2** Define the durable evidence/checkpoint format with task IDs, scope decisions, source/tree identity, commands, outcomes, limits and integration state. Evidence: [FND-01 acceptance](../../evidence/FND-01.md#acceptance)
  - [x] **FND-01.5** Document development, contribution, dependency/license review and no-main-write conventions; add architecture-boundary tests that inspect core dependency/features and build/link/load paths, rejecting an intentional in-process compiler-library dependency without banning approved host build utilities. Evidence: [FND-01 acceptance](../../evidence/FND-01.md#acceptance)
    - [x] **FND-01.5.1** Document contribution, branch/publication, dependency/license review and no-main-write conventions, including the pre-implementation readiness audit. Evidence: [FND-01 acceptance](../../evidence/FND-01.md#acceptance)
    - [x] **FND-01.5.2** Implement architecture-boundary checks and a deliberate forbidden compiler-library dependency/feature mutant; retain a passing approved-host-utility control. Evidence: [FND-01 acceptance](../../evidence/FND-01.md#acceptance)
    - [x] **FND-01.5.3** Introduce the minimal remote build/help, roadmap and boundary-check lane with a reviewed dispatch or isolated bootstrap trigger under AGENTS.md; retain FND-09 as the owner of consolidated coverage. Evidence: [FND-01 acceptance](../../evidence/FND-01.md#acceptance)
  - [x] **FND-01.6** Demonstrate clean core build/help without separately installed LLVM/MLIR/CIRCT SDKs, Nodal-HDL or JVM, plus successful/failed roadmap-check fixtures; record source/tree, allowed host dependencies, commands and B0 measurements before closing. Evidence: [FND-01 acceptance](../../evidence/FND-01.md#acceptance)
    - [x] **FND-01.6.1** Demonstrate compiler-independent clean build/help and positive/negative roadmap checks; record allowed host dependencies and applicable B0 startup measurements. Evidence: [FND-01 acceptance](../../evidence/FND-01.md#acceptance)
    - [x] **FND-01.6.2** Review startup work, dependency growth and deterministic checker output; record any justified no-new-optimization result and preserve required validation. Evidence: [FND-01 acceptance](../../evidence/FND-01.md#acceptance)
    - [x] **FND-01.6.3** Retain exact candidate qualification, review, verified integration and CLI evidence under the shared closure policy; keep all FND-01 obligations open until evidenced. Evidence: [FND-01 acceptance](../../evidence/FND-01.md#acceptance)

- [ ] **FND-02 — Versioned contracts and compatibility semantics**
  - **Depends on:** FND-01.
  - **Capability / modules:** Typed, language-neutral messages in `eda-contracts` and `schemas/`; explicit IDs, units and version errors.
  - **Budget / non-goals:** B0; no unbounded JSON control payloads, raw Rust-struct ABI or duplicated compiler IR.
  - [ ] **FND-02.1** Define ArtifactRef, Diagnostic, RunId, ActionId and schema envelopes with required/optional fields, bounded sizes and unknown-feature handling.
    - [ ] **FND-02.1.1** Implement ArtifactRef, Diagnostic, RunId, ActionId and bounded schema envelopes with explicit required/optional fields and unknown-feature semantics.
    - [ ] **FND-02.1.2** Define the stage roles, SemanticContract/model/assumption identities and VerificationResult/EvidenceManifest references required by the stage-by-stage verification contract; scope IDs to immutable artifacts.
  - [ ] **FND-02.2** Specify digest algorithms, canonical encoding, numeric units, checked offsets, ID scope and JavaScript-safe interchange for wide identifiers.
    - [ ] **FND-02.2.1** Specify digest algorithms and canonical encoding with independently authored byte/digest examples; make units and canonicalization rules explicit.
    - [ ] **FND-02.2.2** Implement checked offsets and ID scope, including wide identifiers that survive JavaScript interchange without precision loss.
  - [ ] **FND-02.3** Implement validation and capability/version negotiation with actionable unsupported-major and missing-required-feature errors.
    - [ ] **FND-02.3.1** Validate message shape, field requirements, numeric/size bounds and unsupported values with actionable diagnostics.
    - [ ] **FND-02.3.2** Implement major-version and required-capability negotiation; reject incompatible versions and missing required features without silent fallback.
  - [ ] **FND-02.4** Add independent valid/invalid golden documents, serialization round-trips and old-reader/new-writer compatibility fixtures.
    - [ ] **FND-02.4.1** Maintain independently authored valid/invalid golden documents and serialization round-trips; expected results must not come solely from the production serializer.
    - [ ] **FND-02.4.2** Exercise old-reader/new-writer compatibility, optional-field handling and explicit rejection of unsupported required semantics.
  - [ ] **FND-02.5** Document migration policy and separate schema version from product/tool/device versions; require source provenance on generated artifacts.
    - [ ] **FND-02.5.1** Document schema migration and compatibility independently of product, tool and device version numbering.
    - [ ] **FND-02.5.2** Require generated-artifact source provenance and exact semantic/model/evidence references; document how unavailable or mismatched provenance is reported.
  - [ ] **FND-02.6** Demonstrate cross-language fixture consumption and malformed/oversized rejection; archive B0, compatibility and test evidence.
    - [ ] **FND-02.6.1** Demonstrate consumption by an independent language implementation plus malformed/oversized rejection and applicable B0 measurements.
    - [ ] **FND-02.6.2** Review repeated parsing, allocations, canonical determinism and wide-ID compatibility; record improvements or a justified no-new-optimization result.
    - [ ] **FND-02.6.3** Archive contract, compatibility, rejection and candidate qualification evidence with the actual API/CLI demonstration and shared closure records.

- [ ] **FND-03 — Adapter protocol and executable fake tool**
  - **Depends on:** FND-02.
  - **Capability / modules:** Invoke a tool with a discoverable contract; `eda-adapters`, adapter schemas and fake-tool fixtures.
  - **Budget / non-goals:** B0/B2; no in-process third-party plugin ABI or mandatory daemon.
  - [ ] **FND-03.1** Specify ToolCapabilities, ActionSpec, StageResult and event envelopes with artifact references, schema negotiation and declared operation support.
    - [ ] **FND-03.1.1** Define ToolCapabilities, ActionSpec, StageResult and bounded event envelopes with version negotiation, declared operations and artifact references.
    - [ ] **FND-03.1.2** Represent checkable mapped-netlist, route, feature-map, final-image decode, simulation-model and timing exports as capabilities; fake declarations make no real-engine support claim.
  - [ ] **FND-03.2** Implement stdio request/result/event framing with size limits, backpressure, timeouts and explicit separation of protocol messages from raw logs.
    - [ ] **FND-03.2.1** Implement stdio request/result/event framing and size bounds; transport large outputs by artifact reference.
    - [ ] **FND-03.2.2** Implement backpressure and timeouts while keeping raw logs separate from protocol messages; define cancellation and terminal-message behavior.
  - [ ] **FND-03.3** Build a controllable fake tool for success, failure, malformed output, missing artifact, hang, process-child creation and log flooding.
    - [ ] **FND-03.3.1** Provide deterministic fake-tool controls for success, explicit failure, malformed output and missing artifacts.
    - [ ] **FND-03.3.2** Provide controlled hangs and owned child-process creation for supervision tests, with reproducible termination behavior.
    - [ ] **FND-03.3.3** Provide configurable log/event flooding so bounded buffering and protocol/log separation can be measured independently.
  - [ ] **FND-03.4** Define one technology-mapping owner per flow and adapter acceptance of opaque engine checkpoints without treating them as universal netlists.
    - [ ] **FND-03.4.1** Declare one technology-mapping owner per flow and carry supported/unsupported export identities through capability negotiation.
    - [ ] **FND-03.4.2** Accept engine checkpoints as opaque versioned artifacts; reject attempts to treat them as universal netlists or independently verified semantic results.
  - [ ] **FND-03.5** Test incompatible protocol, truncated frame, unexpected exit and duplicate terminal event handling against independent expected results.
    - [ ] **FND-03.5.1** Test incompatible protocols, malformed/truncated frames and missing required exports against independently specified expectations.
    - [ ] **FND-03.5.2** Test unexpected exits, duplicate terminal events and missing artifacts; ensure none can yield a successful operation.
  - [ ] **FND-03.6** Demonstrate adapter discovery and one fake operation end-to-end; attach protocol, B2 and negative-test evidence.
    - [ ] **FND-03.6.1** Demonstrate discovery and a complete fake operation with actual protocol/artifacts, B2 measurements and negative-case outcomes.
    - [ ] **FND-03.6.2** Review protocol copies, message allocation and bounded event queues under log volume; verify deterministic results and compatibility without weakening validation.
    - [ ] **FND-03.6.3** Archive candidate qualification, protocol evidence, limits and the actual CLI/API demonstration under the shared closure policy.

- [ ] **FND-04 — Project manifest and locked source closure**
  - **Depends on:** FND-03.
  - **Capability / modules:** `project check` validates an explicit project without executing arbitrary build scripts; `eda-project`, project/lock schemas.
  - **Budget / non-goals:** B0/B1; no full HDL parser or new Scala project language.
  - [ ] **FND-04.1** Implement declarative manifest fields for top, source dialect, ordered files/includes/defines, parameters, target and build profiles.
    - [ ] **FND-04.1.1** Implement manifest fields for top, dialect, ordered sources/includes/defines and parameters with explicit validation.
    - [ ] **FND-04.1.2** Implement target and build-profile selection without executing arbitrary project build scripts or introducing a new HDL/Scala parser.
  - [ ] **FND-04.2** Define exact tool/runtime/plugin/device/IP locking and source-content identity; record transitive includes or mark discovery incomplete.
    - [ ] **FND-04.2.1** Lock exact tools, runtimes, plugins, devices and IP with immutable identity and declared capability/schema requirements.
    - [ ] **FND-04.2.2** Compute source-content closure, including transitive includes when known; explicitly mark incomplete discovery so it cannot qualify a reusable complete input set.
  - [ ] **FND-04.3** Validate paths, case collisions, symlinks, missing/duplicate sources, environment substitution and deterministic glob expansion across supported hosts.
    - [ ] **FND-04.3.1** Validate missing/duplicate sources, path/case collisions and symlink behavior for each declared host profile.
    - [ ] **FND-04.3.2** Constrain environment substitution and make glob expansion and source ordering deterministic; retain tests for ordering-sensitive inputs.
  - [ ] **FND-04.4** Separate portable project intent from machine-local credentials/paths and generated run state; implement explicit migrations with backups.
    - [ ] **FND-04.4.1** Separate portable project intent from machine-local paths/credentials and generated run state; reject unintended secret capture.
    - [ ] **FND-04.4.2** Implement explicit manifest/lock migrations with backups and compatibility diagnostics; retain independently authored before/after examples.
  - [ ] **FND-04.5** Test ordering-sensitive inputs, changed include contents, stale locks, unknown language subset and offline missing dependencies.
    - [ ] **FND-04.5.1** Test changed include contents, stale locks, reordered sources and unknown language subsets with expected diagnostics and identity changes.
    - [ ] **FND-04.5.2** Test missing offline dependencies and incomplete source closure; missing dependencies must not trigger silent downloads or false validation success.
  - [ ] **FND-04.6** Demonstrate a valid project and actionable rejection cases; record stable manifests, B0/B1 fixture results and compatibility evidence.
    - [ ] **FND-04.6.1** Demonstrate project validation and rejection cases with stable manifests, applicable B0/B1 fixtures and compatibility results.
    - [ ] **FND-04.6.2** Review repeated directory/include scans, deterministic expansion and manifest allocation at representative source counts; retain a bounded product-layer design.
    - [ ] **FND-04.6.3** Archive source-closure, migration and exact candidate qualification evidence with the actual project-check demonstration and shared closure records.

- [ ] **FND-05 — Supervised process execution and bounded I/O**
  - **Depends on:** FND-04.
  - **Capability / modules:** Run/cancel a task safely; `eda-exec`, execution-policy contracts and scratch directories.
  - **Budget / non-goals:** B2; subprocess isolation is not a claimed security sandbox, and hardware writes are excluded.
  - [ ] **FND-05.1** Execute explicit argv without shell interpolation, with a controlled working directory/environment and owned per-action scratch space.
    - [ ] **FND-05.1.1** Execute explicit argument arrays without shell interpolation, using a controlled working directory and declared environment.
    - [ ] **FND-05.1.2** Create owned per-action scratch space and prevent actions from claiming another action's workspace or unrelated processes.
  - [ ] **FND-05.2** Stream stdout/stderr to artifacts with bounded buffers and progress events; prevent log floods from exhausting RAM or suppressing terminal errors.
    - [ ] **FND-05.2.1** Stream stdout/stderr to retained artifacts with bounded buffers and explicit byte/encoding handling.
    - [ ] **FND-05.2.2** Deliver bounded progress and terminal events under log floods without losing terminal failures or exhausting memory.
  - [ ] **FND-05.3** Implement process-tree ownership, timeout, graceful cancellation, escalation and cleanup with platform-specific behavior clearly reported.
    - [ ] **FND-05.3.1** Implement owned process-tree tracking and timeout detection for the declared platform profile.
    - [ ] **FND-05.3.2** Implement graceful cancellation, bounded escalation and cleanup; distinguish acknowledgement from actual owned-process termination.
    - [ ] **FND-05.3.3** Document and test platform-specific limitations and unsupported behavior instead of claiming universal cancellation guarantees.
  - [ ] **FND-05.4** Represent CPU, RAM, scratch-disk and license-token requests; do not silently oversubscribe nested tool threads.
    - [ ] **FND-05.4.1** Represent CPU, RAM, scratch-disk and license-token requirements explicitly in action/execution contracts.
    - [ ] **FND-05.4.2** Account for nested tool threads and validate resource requests without silently oversubscribing the declared execution budget.
  - [ ] **FND-05.5** Inject child crashes, hangs, invalid UTF-8, disk-full and interrupted writes; verify no orphaned owned processes or false-success outputs.
    - [ ] **FND-05.5.1** Inject child crashes, hangs and invalid UTF-8; check retained diagnostics, process cleanup and truthful terminal status.
    - [ ] **FND-05.5.2** Inject disk-full and interrupted writes; verify that incomplete artifacts cannot be promoted as successful outputs.
  - [ ] **FND-05.6** Demonstrate B2 log-stream and cancellation targets on the declared host; retain platform limits and fault-test results.
    - [ ] **FND-05.6.1** Measure B2 log streaming, cancellation acknowledgement and process termination on the declared host, including unsupported platform cases.
    - [ ] **FND-05.6.2** Review buffering, polling and process supervision at representative child/log counts; preserve terminal-event ordering and resource bounds.
    - [ ] **FND-05.6.3** Archive fault controls, measurements and exact candidate qualification with the actual execution/cancellation demonstration and shared closure records.

- [ ] **FND-06 — Content-addressed artifacts and safe publication**
  - **Depends on:** FND-05.
  - **Capability / modules:** Inspect immutable outputs and reuse only verified results; `eda-artifacts`, ArtifactRef and action-cache records.
  - **Budget / non-goals:** B3; no network cache, hardware-operation caching or timestamp-only keys.
  - [ ] **FND-06.1** Implement streaming content hashing, checked file lengths and an immutable blob store separated from the action-result index.
    - [ ] **FND-06.1.1** Implement streaming content hashing and checked file lengths without deserializing or loading entire large artifacts.
    - [ ] **FND-06.1.2** Separate immutable blob storage from the action-result index; verify content identity before an artifact is trusted.
  - [ ] **FND-06.2** Define action keys covering transitive inputs, effective constraints/options, exact tools/runtime/device models, seed/thread profile and relevant environment.
    - [ ] **FND-06.2.1** Define keys for transitive inputs, effective constraints/options, exact tools/runtimes/device models and relevant environment.
    - [ ] **FND-06.2.2** Include seed/thread profiles and verification checker, solver, model and SemanticContract versions with their exact input artifacts.
    - [ ] **FND-06.2.3** Demonstrate expected key changes with independent fixtures; do not equate successful tool execution with verified semantic success.
  - [ ] **FND-06.3** Publish validated outputs atomically before committing successful result metadata; forbid failed, cancelled or incomplete results from cache hits.
    - [ ] **FND-06.3.1** Validate outputs and publish immutable artifacts atomically before committing successful result metadata.
    - [ ] **FND-06.3.2** Reject failed, cancelled, incomplete or unverified-required results as successful cache entries; preserve execution and verification outcome distinctions.
  - [ ] **FND-06.4** Add artifact leases, disk quotas and garbage-collection safety; detect concurrent input modification before a result is published.
    - [ ] **FND-06.4.1** Implement artifact leases, disk quotas and garbage collection that preserves referenced/in-use content.
    - [ ] **FND-06.4.2** Detect concurrent input modification before publication and retain a failed/unknown outcome instead of a stale success.
  - [ ] **FND-06.5** Test truncated/corrupt blobs, key collisions in test doubles, duplicate writers, partial publication, stale source closure and missing referenced artifacts.
    - [ ] **FND-06.5.1** Test truncated/corrupt blobs, forced hash collisions in test doubles and missing referenced artifacts against independent expectations.
    - [ ] **FND-06.5.2** Test duplicate writers, interrupted publication and stale source closure; verify recovery never exposes partial successful results.
  - [ ] **FND-06.6** Demonstrate large-file streaming and safe cached replay with zero fake-tool executions on a hit; record B3 and corruption-test evidence.
    - [ ] **FND-06.6.1** Demonstrate large-file streaming and integrity-checked replay with zero fake-tool invocations on a cache hit; retain B3 measurements.
    - [ ] **FND-06.6.2** Review duplicate hashing/copying, index access and deterministic action identity; keep integrity validation intact when optimizing.
    - [ ] **FND-06.6.3** Archive corruption/publication controls, measured limits and exact candidate qualification with the actual cache demonstration and shared closure records.

- [ ] **FND-07 — Durable run state, diagnostics and recovery**
  - **Depends on:** FND-06.
  - **Capability / modules:** Inspect an interrupted run without guessing its state; `eda-flow`, journal/index and report/event contracts.
  - **Budget / non-goals:** B1/B2; no engine-specific incremental implementation claims or distributed database.
  - [ ] **FND-07.1** Define planned/running/completed/failed/cancelled/unknown states, attempt identity and legal transitions with one terminal result per attempt.
    - [ ] **FND-07.1.1** Specify planned/running/completed/failed/cancelled/unknown states and stable run/action/attempt identity.
    - [ ] **FND-07.1.2** Implement legal transitions with one terminal result per attempt; reject duplicates and preserve unknown outcomes explicitly.
  - [ ] **FND-07.2** Implement a transactional local journal/index with serialized writes and immutable RunManifest references to published artifacts.
    - [ ] **FND-07.2.1** Implement a transactional local journal/index with serialized writes and defined commit/recovery boundaries.
    - [ ] **FND-07.2.2** Bind RunManifest records to immutable published artifacts so recovered successes cannot point to unfinished or missing outputs.
  - [ ] **FND-07.3** Preserve ordered diagnostic/event sequences, source locations and exact tool errors while separating nondeterministic timestamps from semantic outputs.
    - [ ] **FND-07.3.1** Retain ordered diagnostics/events, source locations and exact tool-error details with immutable artifact references.
    - [ ] **FND-07.3.2** Separate nondeterministic timestamps from semantic outputs and retain reproducible ordering/replay behavior.
  - [ ] **FND-07.4** Implement restart reconciliation and explicit retry policy; ambiguous external effects remain unknown rather than automatically replayed.
    - [ ] **FND-07.4.1** Reconcile running/interrupted attempts after restart using durable state and artifact identity.
    - [ ] **FND-07.4.2** Define explicit retry classes; ambiguous external effects stay unknown until reconciled instead of being blindly replayed.
  - [ ] **FND-07.5** Crash at every publication/state boundary and compare recovered state with an independent state-machine fixture; test schema migrations.
    - [ ] **FND-07.5.1** Inject crashes at every publication/state boundary and compare recovery against an independently specified state machine.
    - [ ] **FND-07.5.2** Test journal/schema migrations and invalid transition sequences without losing existing successful artifacts or historical attempts.
  - [ ] **FND-07.6** Demonstrate interruption/restart with no lost successful artifacts or fabricated success; attach B1/B2 and recovery evidence.
    - [ ] **FND-07.6.1** Demonstrate interruption/restart with retained successes, truthful unknowns and applicable B1/B2 measurements.
    - [ ] **FND-07.6.2** Review journal scans, write amplification and replay determinism at representative run/event counts; preserve transactional semantics.
    - [ ] **FND-07.6.3** Archive recovery/migration controls and exact candidate qualification with the actual resume demonstration and shared closure records.

- [ ] **FND-08 — Initial trust and package-validation boundary**
  - **Depends on:** FND-07.
  - **Capability / modules:** Reject untrusted or incompatible inputs before execution; trust policy in `eda-contracts`, `eda-packages` and `eda-exec`.
  - **Budget / non-goals:** B0/B3; no hosted untrusted execution, automatic downloads or custom cryptography.
  - [ ] **FND-08.1** Threat-model project scripts, tool output, packages, archives, caches, GUI IPC and physical-device operations; classify effects explicitly.
    - [ ] **FND-08.1.1** Document trust boundaries for project scripts, tool output, plugins/packages, archives and cache artifacts with named effects and owners.
    - [ ] **FND-08.1.2** Classify future GUI IPC and physical-device effects without implementing those later tracks or implying subprocesses provide a security sandbox.
  - [ ] **FND-08.2** Implement safe archive/path handling, content-integrity checks, size limits and deny-by-default tool execution from newly discovered packages.
    - [ ] **FND-08.2.1** Implement bounded archive/path validation for traversal, symlinks and decompression size before extraction/publication.
    - [ ] **FND-08.2.2** Verify package content identity and supported schema/capabilities before use.
    - [ ] **FND-08.2.3** Reject execution of newly discovered package tools by default until an explicit trust decision exists.
  - [ ] **FND-08.3** Separate declarative metadata from executable adapters and require explicit trust decisions; expose actual sandbox capability rather than assuming it exists.
    - [ ] **FND-08.3.1** Separate declarative package metadata from executable adapters and record trust decisions with their scope.
    - [ ] **FND-08.3.2** Expose actual supported isolation capabilities and limitations; deny a requested unavailable mandatory isolation mode.
  - [ ] **FND-08.4** Default telemetry/network access to off and define local redaction; ensure secrets and customer sources are excluded from routine logs.
    - [ ] **FND-08.4.1** Default telemetry/network behavior to off and implement local redaction with explicit input/output boundaries.
    - [ ] **FND-08.4.2** Ensure routine logs and exported records do not contain test credentials, private paths or customer-source fixtures.
  - [ ] **FND-08.5** Test traversal, symlink escape, decompression bombs, unsupported package schema and untrusted executable rejection using recoverable fixtures.
    - [ ] **FND-08.5.1** Exercise traversal, symlink escape, decompression-bomb and unsupported-schema fixtures with independently specified rejection results.
    - [ ] **FND-08.5.2** Exercise untrusted executable and redaction-leak fixtures; keep faults recoverable and verify that denied execution causes no tool side effect.
  - [ ] **FND-08.6** Demonstrate locked/offline fake-tool execution and hostile-input rejection; attach the threat model and B0/B3/security evidence.
    - [ ] **FND-08.6.1** Demonstrate locked/offline fake-tool execution and hostile-input rejection; retain threat-model, B0/B3 and security results.
    - [ ] **FND-08.6.2** Review repeated package reads, bounded extraction and trust-decision compatibility; preserve full integrity/security checks when optimizing.
    - [ ] **FND-08.6.3** Archive security controls and exact candidate qualification with the actual package-validation demonstration and shared closure records.

- [ ] **FND-09 — Bootstrap verification and performance harness**
  - **Depends on:** FND-08.
  - **Capability / modules:** Repeatable local/CI quality gates; `tests/`, `benchmarks/`, maintenance checks and deliberate workflow definitions.
  - **Budget / non-goals:** B0-B3; no hardware or secrets required on untrusted PR runners.
  - [ ] **FND-09.1** Add unit/property, contract, fake-tool, cache-invalidation, fault-recovery and documentation-check suites for all foundation components.
    - [ ] **FND-09.1.1** Consolidate unit/property and contract suites for the implemented Foundation components, including partial/invalid nested-checklist states.
    - [ ] **FND-09.1.2** Integrate fake-tool, cache-invalidation and crash/recovery suites without making earlier increments depend on this consolidation.
    - [ ] **FND-09.1.3** Add stage-evidence negatives for missing checkable artifacts, wrong hashes/models, mock semantic mismatches and false-success results before FND-10.
  - [ ] **FND-09.2** Register deterministic fixture generators and independent expected outcomes; preserve random seeds and minimized failures.
    - [ ] **FND-09.2.1** Register deterministic fixture generators with immutable identities, seeds, workload limits and retained minimized failures.
    - [ ] **FND-09.2.2** Maintain independent expected outcomes/oracles; prevent production outputs from becoming their own sole correctness reference.
  - [ ] **FND-09.3** Define pinned CI lanes and test result schemas, including a compiler-independent core lane and separate capability-qualified engine lanes; apply ADR-0001 dependency checks and fail/unknown/skipped distinctions so absent tools never look like passes.
    - [ ] **FND-09.3.1** Extend the FND-01 bootstrap lane into pinned CI/result schemas with compiler-independent core coverage and separately capability-qualified engine lanes.
    - [ ] **FND-09.3.2** Apply ADR-0001 dependency checks and explicit fail/unknown/unavailable/skipped outcomes; engine-lane definitions do not qualify absent real tools or block core-only acceptance.
  - [ ] **FND-09.4** Record the reference host and pilot B0-B3 measurements, including parent/child resources and cold/warm differences; review any budget revision explicitly.
    - [ ] **FND-09.4.1** Record the exact reference host/toolchain and pilot applicable B0-B3 measurements, including parent/child resources and cold/warm cases.
    - [ ] **FND-09.4.2** Retain benchmark baselines and review any budget change with rationale and history; do not replace missed targets with invented results.
  - [ ] **FND-09.5** Verify same-input replay under a declared deterministic profile and expected invalidation for every key component; test clean offline execution.
    - [ ] **FND-09.5.1** Verify same-input replay under the declared deterministic profile and expected invalidation for each key component.
    - [ ] **FND-09.5.2** Exercise clean offline execution and compatibility fixtures with explicit allowed host dependencies and unavailable-tool outcomes.
  - [ ] **FND-09.6** Publish reproducible bootstrap commands and candidate-head evidence; show that intentional faults make the appropriate checks fail.
    - [ ] **FND-09.6.1** Publish reproducible bootstrap commands and demonstrate that intentional faults fail the correct checks, including evidence-identity failures.
    - [ ] **FND-09.6.2** Review harness runtime, fixture growth and memory use at representative scales; select predecessor interactions by risk rather than an unbounded Cartesian product.
    - [ ] **FND-09.6.3** Archive exact candidate qualification, fault outcomes and performance results with the actual harness demonstration and shared closure records.

- [ ] **FND-10 — Foundation acceptance and dependent-track unlock**
  - **Depends on:** FND-09 and all earlier FND increments.
  - **Capability / modules:** One coherent headless fake-tool pipeline with approved stable boundaries; acceptance fixtures and interface ADRs.
  - **Budget / non-goals:** B0-B3; no claim of real synthesis, FPGA support or commercial qualification.
  - [ ] **FND-10.1** Run validated project -> planned actions -> supervised fake tools -> verified artifacts -> structured report with exact provenance.
    - [ ] **FND-10.1.1** Execute one validated project through planned actions and supervised fake tools with immutable source/tool identity.
    - [ ] **FND-10.1.2** Verify resulting artifacts and produce the structured report with complete stage, result and provenance references.
  - [ ] **FND-10.2** Demonstrate cache replay, changed-input invalidation, cancellation, crash recovery and offline behavior in the integrated pipeline.
    - [ ] **FND-10.2.1** Demonstrate cache replay and changed-input invalidation without rerunning fake tools on valid hits.
    - [ ] **FND-10.2.2** Demonstrate cancellation, crash recovery and offline replay together without lost successes or fabricated completion.
  - [ ] **FND-10.3** Complete ownership/schema/adapter reviews and ADR-0001 acceptance: bounded artifact contracts, no in-process LLVM/MLIR/CIRCT dependency, and help/project/stored-report/fake-tool operations without the Nodal compiler stack. Real traditional-HDL independence is separately qualified by TOOL-02/VER-02, not claimed from mocks.
    - [ ] **FND-10.3.1** Complete ownership/schema/adapter reviews and ADR-0001 build/link/load checks against the integrated candidate.
    - [ ] **FND-10.3.2** Demonstrate bounded artifact contracts and help/project/stored-report/fake-tool operations without the Nodal compiler stack or either upstream repository.
    - [ ] **FND-10.3.3** Reject mock missing-artifact, wrong-model/hash and false-success evidence; retain real traditional-HDL independence under TOOL-02/VER-02 rather than claiming it from mocks.
  - [ ] **FND-10.4** Pass all applicable foundation tests and budgets on the reviewed source; enumerate unsupported hosts and trust limitations.
    - [ ] **FND-10.4.1** Pass all applicable integrated Foundation correctness, compatibility, security, determinism and performance requirements on the reviewed source.
    - [ ] **FND-10.4.2** Record supported/unsupported hosts and trust limits with honest execution outcomes; review integrated overhead without weakening any gate.
  - [ ] **FND-10.5** Confirm every foundation child is implemented with evidence and the dependency graph has no circular gate through VER or other tracks.
    - [ ] **FND-10.5.1** Audit every Foundation leaf/child evidence link and all internal/external dependency dispositions; required blocked work prevents closure.
    - [ ] **FND-10.5.2** Verify the dependency graph has no reverse gate through FND-09, VER, Nodal-HDL or Nodal-FPGA and that later real-tool qualification remains assigned.
  - [ ] **FND-10.6** Record final integrated acceptance evidence and a real CLI demonstration; only then mark this parent complete and unlock dependent tracks.
    - [ ] **FND-10.6.1** Retain the actual integrated CLI demonstration, reproducible commands, accepted capability limits and generated-Verilog applicability statement.
    - [ ] **FND-10.6.2** Complete exact-final-head targeted/full qualification, review, verified integration and required evidence publication under AGENTS.md.
    - [ ] **FND-10.6.3** Reconcile all Foundation task/evidence state, then close FND-10 and unlock dependent tracks; finish the completion report before disabling its hourly continuation.
