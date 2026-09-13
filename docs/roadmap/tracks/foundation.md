# FND — Foundation track

This track establishes executable contracts, not only design documents. All other tracks are blocked by FND-10. Foundation has its own tests and does not depend on VER. Follow the [completion policy](../completion-policy.md) and [performance profiles](../../performance.md). Every checkbox below is implementation work, initially uncompleted.

The compiler-independent core acceptance rules in [ADR-0001](../../adr/0001-rust-core-external-compiler-boundary.md) are part of FND-01, FND-09 and FND-10. They apply to application dependencies, not the implementation of approved Rust/platform build utilities.

- [ ] **FND-01 — Workspace, ownership and progress discipline**
  - **Depends on:** none.
  - **Capability / modules:** Build a minimal Rust CLI; establish ownership and `eda-contracts` plus `apps/cli`, maintenance tools and ADRs.
  - **Budget / non-goals:** B0; no empty future-crate forest, GUI, MLIR/CIRCT compiler-framework dependency or CAD algorithm implementation.
  - [ ] **FND-01.1** Establish Cargo workspace, pinned toolchain, application lockfile, formatting/lint policy and a minimal version/help command.
  - [ ] **FND-01.2** Ratify the architecture ownership table and ADR-0001 dependency rules; identify interface owners in nodal-hdl and nodal-fpga without asserting their unverified capabilities.
  - [ ] **FND-01.3** Implement documentation checks for unique increment/child IDs, task nesting, valid dependencies, cycles and closed parents with open descendants; ignore fenced examples.
  - [ ] **FND-01.4** Add tests proving partial child completion is accepted while premature parent closure and invalid dependencies fail; define the evidence-record format.
  - [ ] **FND-01.5** Document development, contribution, dependency/license review and no-main-write conventions; add architecture-boundary tests that inspect core dependency/features and build/link/load paths, rejecting an intentional in-process compiler-library dependency without banning approved host build utilities.
  - [ ] **FND-01.6** Demonstrate clean core build/help without separately installed LLVM/MLIR/CIRCT SDKs, Nodal-HDL or JVM, plus successful/failed roadmap-check fixtures; record source/tree, allowed host dependencies, commands and B0 measurements before closing.

- [ ] **FND-02 — Versioned contracts and compatibility semantics**
  - **Depends on:** FND-01.
  - **Capability / modules:** Typed, language-neutral messages in `eda-contracts` and `schemas/`; explicit IDs, units and version errors.
  - **Budget / non-goals:** B0; no unbounded JSON control payloads, raw Rust-struct ABI or duplicated compiler IR.
  - [ ] **FND-02.1** Define ArtifactRef, Diagnostic, RunId, ActionId and schema envelopes with required/optional fields, bounded sizes and unknown-feature handling.
  - [ ] **FND-02.2** Specify digest algorithms, canonical encoding, numeric units, checked offsets, ID scope and JavaScript-safe interchange for wide identifiers.
  - [ ] **FND-02.3** Implement validation and capability/version negotiation with actionable unsupported-major and missing-required-feature errors.
  - [ ] **FND-02.4** Add independent valid/invalid golden documents, serialization round-trips and old-reader/new-writer compatibility fixtures.
  - [ ] **FND-02.5** Document migration policy and separate schema version from product/tool/device versions; require source provenance on generated artifacts.
  - [ ] **FND-02.6** Demonstrate cross-language fixture consumption and malformed/oversized rejection; archive B0, compatibility and test evidence.

- [ ] **FND-03 — Adapter protocol and executable fake tool**
  - **Depends on:** FND-02.
  - **Capability / modules:** Invoke a tool with a discoverable contract; `eda-adapters`, adapter schemas and fake-tool fixtures.
  - **Budget / non-goals:** B0/B2; no in-process third-party plugin ABI or mandatory daemon.
  - [ ] **FND-03.1** Specify ToolCapabilities, ActionSpec, StageResult and event envelopes with artifact references, schema negotiation and declared operation support.
  - [ ] **FND-03.2** Implement stdio request/result/event framing with size limits, backpressure, timeouts and explicit separation of protocol messages from raw logs.
  - [ ] **FND-03.3** Build a controllable fake tool for success, failure, malformed output, missing artifact, hang, process-child creation and log flooding.
  - [ ] **FND-03.4** Define one technology-mapping owner per flow and adapter acceptance of opaque engine checkpoints without treating them as universal netlists.
  - [ ] **FND-03.5** Test incompatible protocol, truncated frame, unexpected exit and duplicate terminal event handling against independent expected results.
  - [ ] **FND-03.6** Demonstrate adapter discovery and one fake operation end-to-end; attach protocol, B2 and negative-test evidence.

- [ ] **FND-04 — Project manifest and locked source closure**
  - **Depends on:** FND-03.
  - **Capability / modules:** `project check` validates an explicit project without executing arbitrary build scripts; `eda-project`, project/lock schemas.
  - **Budget / non-goals:** B0/B1; no full HDL parser or new Scala project language.
  - [ ] **FND-04.1** Implement declarative manifest fields for top, source dialect, ordered files/includes/defines, parameters, target and build profiles.
  - [ ] **FND-04.2** Define exact tool/runtime/plugin/device/IP locking and source-content identity; record transitive includes or mark discovery incomplete.
  - [ ] **FND-04.3** Validate paths, case collisions, symlinks, missing/duplicate sources, environment substitution and deterministic glob expansion across supported hosts.
  - [ ] **FND-04.4** Separate portable project intent from machine-local credentials/paths and generated run state; implement explicit migrations with backups.
  - [ ] **FND-04.5** Test ordering-sensitive inputs, changed include contents, stale locks, unknown language subset and offline missing dependencies.
  - [ ] **FND-04.6** Demonstrate a valid project and actionable rejection cases; record stable manifests, B0/B1 fixture results and compatibility evidence.

- [ ] **FND-05 — Supervised process execution and bounded I/O**
  - **Depends on:** FND-04.
  - **Capability / modules:** Run/cancel a task safely; `eda-exec`, execution-policy contracts and scratch directories.
  - **Budget / non-goals:** B2; subprocess isolation is not a claimed security sandbox, and hardware writes are excluded.
  - [ ] **FND-05.1** Execute explicit argv without shell interpolation, with a controlled working directory/environment and owned per-action scratch space.
  - [ ] **FND-05.2** Stream stdout/stderr to artifacts with bounded buffers and progress events; prevent log floods from exhausting RAM or suppressing terminal errors.
  - [ ] **FND-05.3** Implement process-tree ownership, timeout, graceful cancellation, escalation and cleanup with platform-specific behavior clearly reported.
  - [ ] **FND-05.4** Represent CPU, RAM, scratch-disk and license-token requests; do not silently oversubscribe nested tool threads.
  - [ ] **FND-05.5** Inject child crashes, hangs, invalid UTF-8, disk-full and interrupted writes; verify no orphaned owned processes or false-success outputs.
  - [ ] **FND-05.6** Demonstrate B2 log-stream and cancellation targets on the declared host; retain platform limits and fault-test results.

- [ ] **FND-06 — Content-addressed artifacts and safe publication**
  - **Depends on:** FND-05.
  - **Capability / modules:** Inspect immutable outputs and reuse only verified results; `eda-artifacts`, ArtifactRef and action-cache records.
  - **Budget / non-goals:** B3; no network cache, hardware-operation caching or timestamp-only keys.
  - [ ] **FND-06.1** Implement streaming content hashing, checked file lengths and an immutable blob store separated from the action-result index.
  - [ ] **FND-06.2** Define action keys covering transitive inputs, effective constraints/options, exact tools/runtime/device models, seed/thread profile and relevant environment.
  - [ ] **FND-06.3** Publish validated outputs atomically before committing successful result metadata; forbid failed, cancelled or incomplete results from cache hits.
  - [ ] **FND-06.4** Add artifact leases, disk quotas and garbage-collection safety; detect concurrent input modification before a result is published.
  - [ ] **FND-06.5** Test truncated/corrupt blobs, key collisions in test doubles, duplicate writers, partial publication, stale source closure and missing referenced artifacts.
  - [ ] **FND-06.6** Demonstrate large-file streaming and safe cached replay with zero fake-tool executions on a hit; record B3 and corruption-test evidence.

- [ ] **FND-07 — Durable run state, diagnostics and recovery**
  - **Depends on:** FND-06.
  - **Capability / modules:** Inspect an interrupted run without guessing its state; `eda-flow`, journal/index and report/event contracts.
  - **Budget / non-goals:** B1/B2; no engine-specific incremental implementation claims or distributed database.
  - [ ] **FND-07.1** Define planned/running/completed/failed/cancelled/unknown states, attempt identity and legal transitions with one terminal result per attempt.
  - [ ] **FND-07.2** Implement a transactional local journal/index with serialized writes and immutable RunManifest references to published artifacts.
  - [ ] **FND-07.3** Preserve ordered diagnostic/event sequences, source locations and exact tool errors while separating nondeterministic timestamps from semantic outputs.
  - [ ] **FND-07.4** Implement restart reconciliation and explicit retry policy; ambiguous external effects remain unknown rather than automatically replayed.
  - [ ] **FND-07.5** Crash at every publication/state boundary and compare recovered state with an independent state-machine fixture; test schema migrations.
  - [ ] **FND-07.6** Demonstrate interruption/restart with no lost successful artifacts or fabricated success; attach B1/B2 and recovery evidence.

- [ ] **FND-08 — Initial trust and package-validation boundary**
  - **Depends on:** FND-07.
  - **Capability / modules:** Reject untrusted or incompatible inputs before execution; trust policy in `eda-contracts`, `eda-packages` and `eda-exec`.
  - **Budget / non-goals:** B0/B3; no hosted untrusted execution, automatic downloads or custom cryptography.
  - [ ] **FND-08.1** Threat-model project scripts, tool output, packages, archives, caches, GUI IPC and physical-device operations; classify effects explicitly.
  - [ ] **FND-08.2** Implement safe archive/path handling, content-integrity checks, size limits and deny-by-default tool execution from newly discovered packages.
  - [ ] **FND-08.3** Separate declarative metadata from executable adapters and require explicit trust decisions; expose actual sandbox capability rather than assuming it exists.
  - [ ] **FND-08.4** Default telemetry/network access to off and define local redaction; ensure secrets and customer sources are excluded from routine logs.
  - [ ] **FND-08.5** Test traversal, symlink escape, decompression bombs, unsupported package schema and untrusted executable rejection using recoverable fixtures.
  - [ ] **FND-08.6** Demonstrate locked/offline fake-tool execution and hostile-input rejection; attach the threat model and B0/B3/security evidence.

- [ ] **FND-09 — Bootstrap verification and performance harness**
  - **Depends on:** FND-08.
  - **Capability / modules:** Repeatable local/CI quality gates; `tests/`, `benchmarks/`, maintenance checks and deliberate workflow definitions.
  - **Budget / non-goals:** B0-B3; no hardware or secrets required on untrusted PR runners.
  - [ ] **FND-09.1** Add unit/property, contract, fake-tool, cache-invalidation, fault-recovery and documentation-check suites for all foundation components.
  - [ ] **FND-09.2** Register deterministic fixture generators and independent expected outcomes; preserve random seeds and minimized failures.
  - [ ] **FND-09.3** Define pinned CI lanes and test result schemas, including a compiler-independent core lane and separate capability-qualified engine lanes; apply ADR-0001 dependency checks and fail/unknown/skipped distinctions so absent tools never look like passes.
  - [ ] **FND-09.4** Record the reference host and pilot B0-B3 measurements, including parent/child resources and cold/warm differences; review any budget revision explicitly.
  - [ ] **FND-09.5** Verify same-input replay under a declared deterministic profile and expected invalidation for every key component; test clean offline execution.
  - [ ] **FND-09.6** Publish reproducible bootstrap commands and candidate-head evidence; show that intentional faults make the appropriate checks fail.

- [ ] **FND-10 — Foundation acceptance and dependent-track unlock**
  - **Depends on:** FND-09 and all earlier FND increments.
  - **Capability / modules:** One coherent headless fake-tool pipeline with approved stable boundaries; acceptance fixtures and interface ADRs.
  - **Budget / non-goals:** B0-B3; no claim of real synthesis, FPGA support or commercial qualification.
  - [ ] **FND-10.1** Run validated project -> planned actions -> supervised fake tools -> verified artifacts -> structured report with exact provenance.
  - [ ] **FND-10.2** Demonstrate cache replay, changed-input invalidation, cancellation, crash recovery and offline behavior in the integrated pipeline.
  - [ ] **FND-10.3** Complete ownership/schema/adapter reviews and ADR-0001 acceptance: bounded artifact contracts, no in-process LLVM/MLIR/CIRCT dependency, and help/project/stored-report/fake-tool operations without the Nodal compiler stack. Real traditional-HDL independence is separately qualified by TOOL-02/VER-02, not claimed from mocks.
  - [ ] **FND-10.4** Pass all applicable foundation tests and budgets on the reviewed source; enumerate unsupported hosts and trust limitations.
  - [ ] **FND-10.5** Confirm every foundation child is implemented with evidence and the dependency graph has no circular gate through VER or other tracks.
  - [ ] **FND-10.6** Record final integrated acceptance evidence and a real CLI demonstration; only then mark this parent complete and unlock dependent tracks.
