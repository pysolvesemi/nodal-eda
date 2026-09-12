# DBG — Debug and source traceability track

Hard gate: FND-10. Compiler instrumentation and device debug primitives remain with nodal-hdl/nodal-fpga or qualified IP. Nodal-EDA owns requesting, coordinating and presenting debug evidence. Follow the [completion policy](../completion-policy.md) and [verification strategy](../../verification.md).

- [ ] **DBG-01 — Source-to-artifact provenance and debug-off contract**
  - **Depends on:** FND-10, TOOL-04.
  - **Capability / modules:** Trace a source object to implementation evidence; `eda-debug`, ProvenanceMap and scoped stable identities.
  - **Budget / non-goals:** B3/B4/B6; no guaranteed one-to-one source/net mapping and no MLIR object dependency.
  - [ ] **DBG-01.1** Consume compiler source locations and export identities plus engine cell/net/resource mappings as separate immutable provenance layers.
  - [ ] **DBG-01.2** Represent merged, cloned, optimized-away, renamed and unavailable objects explicitly; bind every lookup to source/build/device hashes.
  - [ ] **DBG-01.3** Provide bounded CLI queries from source to timing/resource evidence and reverse lookup without loading the full device graph.
  - [ ] **DBG-01.4** Define debug-off behavior and avoid instrumentation or unnecessary large trace generation when disabled; distinguish metadata from probing hardware.
  - [ ] **DBG-01.5** Test renamed hierarchy, duplicate display names, stale maps and optimization transformations with independently reviewed reference mappings.
  - [ ] **DBG-01.6** Demonstrate actual source/generated-Verilog/physical evidence where available and measured debug-off overhead; record B3/B4/B6 and mapping limits.

- [ ] **DBG-02 — Qualified ILA insertion and capture session**
  - **Depends on:** FND-10, DBG-01, TOOL-05, HW-02, IP-02.
  - **Capability / modules:** Request probes, build and capture with an actual supported analyzer; probe/trigger/session contracts and `eda-debug`.
  - **Budget / non-goals:** B3/B5/B6; no claim that an arbitrary signal is observable or that instrumentation has zero timing/resource cost.
  - [ ] **DBG-02.1** Integrate a qualified analyzer IP/compiler insertion capability with explicit clocks, probes, trigger limits, capture depth and resource cost.
  - [ ] **DBG-02.2** Bind debug symbols and probe routing to the exact instrumented bitstream digest and target revision; reject stale maps before acquisition.
  - [ ] **DBG-02.3** Orchestrate engine rebuild/timing checks and authorized programming, keeping normal and instrumented artifacts separate.
  - [ ] **DBG-02.4** Acquire captures through a bounded hardware session and export supported waveform/metadata artifacts with timebase and clock-domain information.
  - [ ] **DBG-02.5** Check generated instrumentation semantics by qualified formal/simulation fixtures; test clock loss, overflow, disconnect and mismatched bitstreams.
  - [ ] **DBG-02.6** Demonstrate an actual trigger/capture and source correlation on a supported target; retain B5/B6, generated-RTL evidence and limitations.

- [ ] **DBG-03 — Large waveform indexing and replay**
  - **Depends on:** FND-10, DBG-02, PERF-02.
  - **Capability / modules:** Query large captures without loading them whole; waveform indexes, capture windows and replay contracts.
  - **Budget / non-goals:** B3/B4; no proprietary simulator replacement or unsupported waveform-format promise.
  - [ ] **DBG-03.1** Integrate qualified waveform readers/exporters with streaming ingestion, checked offsets, exact time units and signal-type metadata.
  - [ ] **DBG-03.2** Build persistent time/signal indexes and paged query APIs with bounded caches and resumable ingestion.
  - [ ] **DBG-03.3** Preserve dropped-sample, overflow, unknown/X and incomplete-capture semantics; never interpolate a missing digital event as fact.
  - [ ] **DBG-03.4** Support offline replay and source navigation from immutable capture/build identities independently of a live board.
  - [ ] **DBG-03.5** Cross-check supported waveform samples against independent readers/synthetic traces, including >4 GiB offsets, time overflow and corrupt files.
  - [ ] **DBG-03.6** Demonstrate B3/B4 on large trace fixtures and capture recovery; archive exactness, index compatibility and memory evidence.

- [ ] **DBG-04 — Advanced regional and multi-clock debug**
  - **Depends on:** FND-10, DBG-03, CON-05, FLOW-05.
  - **Capability / modules:** Debug advanced engine-supported configurations; cross-domain correlation and configuration-set debug manifests.
  - **Budget / non-goals:** B4/B5/B8; no implied synchrony across clocks or support for unqualified partial reconfiguration.
  - [ ] **DBG-04.1** Model per-domain timebase, synchronization markers and explicit uncertainty for cross-clock or cross-device observations.
  - [ ] **DBG-04.2** Track probe availability and symbol validity across supported regional/reconfiguration transitions using engine legality contracts.
  - [ ] **DBG-04.3** Integrate permitted debug access and security/lifecycle restrictions without exposing protected data through cached sessions.
  - [ ] **DBG-04.4** Provide bounded causal/navigation queries and audit all configuration/session transitions.
  - [ ] **DBG-04.5** Test stale region maps, reset races, desynchronized captures, access revocation and unsupported debug configurations.
  - [ ] **DBG-04.6** Demonstrate qualified multi-domain/regional scenarios and honest uncertainty; attach B4/B5/B8 and cross-layer evidence.
