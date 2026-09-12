# FLOW — Build and execution track

Hard gate: FND-10. The product owns orchestration, not synthesis/P&R algorithms. Follow the [completion policy](../completion-policy.md), [architecture](../../architecture.md) and [budget profiles](../../performance.md).

- [ ] **FLOW-01 — Deterministic DAG planner and resource scheduler**
  - **Depends on:** FND-10.
  - **Capability / modules:** `build --plan` explains actions; `eda-flow`, ActionSpec/DAG schemas and scheduling policy.
  - **Budget / non-goals:** B1/B6; no general-purpose build language, cluster scheduler or native CAD engines.
  - [ ] **FLOW-01.1** Lower validated project/flow profiles to explicit action DAGs with input/output contracts and deterministic stage ordering.
  - [ ] **FLOW-01.2** Reject cycles, missing producers, duplicate output ownership and incompatible artifact media/schema types before tool execution.
  - [ ] **FLOW-01.3** Schedule by CPU, RAM, scratch disk and license tokens; set external-tool thread limits to prevent nested oversubscription.
  - [ ] **FLOW-01.4** Show why an action runs, is cached or is blocked, including dependency and capability diagnostics.
  - [ ] **FLOW-01.5** Compare random small DAG execution with a separately implemented reference scheduler; test cancellation and resource starvation.
  - [ ] **FLOW-01.6** Demonstrate the 10,000-action fixture and documented scheduling policy; attach B1/B6 and correctness evidence.

- [ ] **FLOW-02 — Real headless project-to-bitstream workflow**
  - **Depends on:** FND-10, FLOW-01, TOOL-02, CON-01.
  - **Capability / modules:** `build --locked --offline` for one qualified open device; flow profiles and StageResult/RunManifest integration.
  - **Budget / non-goals:** B2/B3/B6; build never programs hardware and does not imply timing signoff.
  - [ ] **FLOW-02.1** Connect synthesis, implementation, device packer and report stages using the qualified TOOL-02 tuple and explicit target identity.
  - [ ] **FLOW-02.2** Deliver every required constraint and track its accepted/unsupported/unmatched disposition; block unsupported required intent.
  - [ ] **FLOW-02.3** Verify actual expected artifacts and stage-specific success evidence instead of trusting an exit code or log keyword alone.
  - [ ] **FLOW-02.4** Publish a reproducible run manifest and CLI status/result summaries; preserve raw engine logs and implementation artifacts.
  - [ ] **FLOW-02.5** Test syntax error, unroutable design, wrong device, ignored constraint, missing output and interrupted packer with no false success.
  - [ ] **FLOW-02.6** Demonstrate at least combinational, sequential and memory-supported fixtures; record B6 overhead and full pinned E2E evidence.

- [ ] **FLOW-03 — Incremental replay, checkpoints and support reproduction**
  - **Depends on:** FND-10, FLOW-02, VER-02.
  - **Capability / modules:** `run resume` and explainable reuse; `eda-flow`, `eda-artifacts`, resume/support manifests.
  - **Budget / non-goals:** B1-B3/B6; cached stages are not advertised as native incremental P&R.
  - [ ] **FLOW-03.1** Reuse stage artifacts only when complete action keys and engine compatibility identities match; report every invalidation reason.
  - [ ] **FLOW-03.2** Implement crash-safe resume, leases and garbage collection with simultaneous projects and duplicate requests.
  - [ ] **FLOW-03.3** Preserve engine checkpoints as opaque artifacts and resume them only when the adapter explicitly supports that version/profile.
  - [ ] **FLOW-03.4** Generate a local, inspectable/redacted replay bundle with exact commands and artifact hashes, excluding secrets by default.
  - [ ] **FLOW-03.5** Mutate includes, defines, constraints, seeds, thread counts, tool libraries and device timing models; require correct invalidation versus a clean build.
  - [ ] **FLOW-03.6** Demonstrate warm reuse and interrupted-run recovery against direct-tool results; retain B3/B6 and support-replay evidence.

- [ ] **FLOW-04 — Optional authenticated remote execution**
  - **Depends on:** FND-10, FLOW-03, SEC-02, PERF-02.
  - **Capability / modules:** Select local or remote execution without changing project meaning; `eda-exec` providers, worker/lease contracts.
  - **Budget / non-goals:** B3/B6; no mandatory cloud, unrestricted shared cache or replacement distributed build platform.
  - [ ] **FLOW-04.1** Evaluate existing remote-execution/CAS protocols and implement the smallest provider interface compatible with immutable ActionSpec/ArtifactRef contracts.
  - [ ] **FLOW-04.2** Authenticate workers and bind results to exact inputs/toolchains; enforce per-tenant cache and artifact authorization.
  - [ ] **FLOW-04.3** Add bounded uploads/downloads, resource/license leases, deduplication and worker-loss reconciliation with idempotent publication.
  - [ ] **FLOW-04.4** Restrict hardware writes, secret-dependent tasks and non-hermetic tools to explicitly allowed execution profiles; preserve offline local builds.
  - [ ] **FLOW-04.5** Inject network partitions, duplicate completion, lost leases, malicious results and cancellation races; compare valid remote/local semantics.
  - [ ] **FLOW-04.6** Demonstrate one qualified remote provider and record transfer costs separately from execution; close only with trust, recovery and B3/B6 evidence.

- [ ] **FLOW-05 — Engine-supported hierarchical and professional flows**
  - **Depends on:** FND-10, FLOW-04, TOOL-05, CON-05.
  - **Capability / modules:** Reproducible regional/OOC/configuration-set builds; advanced flow profiles and boundary/checkpoint manifests.
  - **Budget / non-goals:** B1/B3/B6; no promise of partial reconfiguration, multi-die or incremental P&R without engine support.
  - [ ] **FLOW-05.1** Define partition interfaces, reusable compilation units and boundary constraints using actual nodal-fpga engine capability contracts.
  - [ ] **FLOW-05.2** Track interface/timing/device/configuration identities for out-of-context and regional reuse; invalidate downstream work on boundary changes.
  - [ ] **FLOW-05.3** Orchestrate multi-corner/multi-configuration jobs and approved seed sweeps without changing constraints or cherry-picking away failures.
  - [ ] **FLOW-05.4** Preserve cross-region/cross-die constraints and aggregate completeness evidence; reject unsupported reconfiguration combinations.
  - [ ] **FLOW-05.5** Compare incremental/regional results with qualified full builds under documented semantic and timing tolerances; inject stale boundary checkpoints.
  - [ ] **FLOW-05.6** Demonstrate supported advanced-device fixtures, measured reuse and honest unsupported-feature failures; retain integrated budget and qualification evidence.
