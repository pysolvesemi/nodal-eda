# DBG — Debug and source traceability track

Hard gate: FND-10. Compiler instrumentation and device debug primitives remain with nodal-hdl/nodal-fpga or qualified IP. Nodal-EDA owns requesting, coordinating and presenting debug evidence. Follow the [completion policy](../completion-policy.md), [verification strategy](../../verification.md) and [stage-by-stage contract](../../verification-pipeline.md). See [REF-14..REF-19](../../reference-implementations.md#soft-logic-analyzer-and-waveform-references) for concrete implementation references.

## Scope, ownership and dependency migration

The portable analyzer RTL/generator is initially a qualified external IP package managed by IP-01/IP-02, not hardware implemented inside the Rust product core. Nodal-HDL owns source identities and compiler-assisted insertion. Nodal-FPGA or the selected device provider owns RAM/clock mapping, device debug access and fabric configuration. Nodal-EDA owns probe intent, artifact/session identity, orchestration, acquisition, indexing and presentation. Record exact provider capabilities before implementation; this update does not modify either upstream repository.

DBG-01 now qualifies generic source/provenance contracts on the TOOL-02 reference flow. DBG-02 qualifies conventional-HDL analyzer integration on that reference device without requiring TOOL-04/TOOL-05. The Nodal-specific requirements previously implicit in DBG-01.1/.6, DBG-02.1/.6 and IP-02.4 are retained explicitly in DBG-05. No existing stable task IDs are deleted or marked complete. Reference-only success cannot close DBG-05 or advertise Nodal-source/own-fabric debug.

DBG-03 no longer waits for live capture: it uses independent trace fixtures after its own prerequisites. Real capture/export checks remain mandatory in DBG-02.6, and live-capture indexing is required in DBG-05.5 and UX-03. DBG-04 explicitly retains live-debug and Nodal/own-fabric predecessors after that decoupling; SEC-04 retains DBG-02 and REL-03 adds DBG-05 to preserve downstream qualification. Programming, timing, security and final-bitstream checks are not waived.

- [ ] **DBG-01 — Source-to-artifact provenance and debug-off contract**
  - **Depends on:** FND-10, TOOL-02, CON-02, VER-03.
  - **Capability / modules:** Trace supported reference-HDL objects to implementation evidence; `eda-debug`, ProvenanceMap and scoped stable identities.
  - **Budget / non-goals:** B3/B4/B6; no guaranteed one-to-one source/net mapping and no MLIR object dependency.
  - [ ] **DBG-01.1** Consume qualified frontend source locations/export identities and engine cell/net/resource mappings as separate immutable layers; test generic contracts without a Nodal compiler. Actual Nodal export qualification is retained in DBG-05.1.
  - [ ] **DBG-01.2** Represent merged, cloned, optimized-away, renamed and unavailable objects explicitly; bind every lookup to source/build/device hashes. Keep stable scoped identities separate from display names.
  - [ ] **DBG-01.3** Provide bounded CLI queries from source to timing/resource evidence and reverse lookup without loading the full device graph; never reconstruct a lost source name by guessing.
  - [ ] **DBG-01.4** Define debug-off behavior and avoid instrumentation or unnecessary large trace generation when disabled; distinguish metadata from probing hardware and preserve only specifically selected probes when supported.
  - [ ] **DBG-01.5** Test renamed hierarchy, duplicate display names, stale maps and optimization transformations with independently reviewed reference mappings.
  - [ ] **DBG-01.6** Demonstrate actual reference source/mapped-Verilog/physical evidence and measured debug-off overhead; record B3/B4/B6 and mapping limits. Nodal Scala/generated-Verilog evidence remains required by DBG-05.6.

- [ ] **DBG-02 — Qualified reference-device soft ILA insertion and capture session**
  - **Depends on:** FND-10, DBG-01, TOOL-02, HW-02, IP-02, VER-03, CON-02.
  - **Capability / modules:** Request probes, build and capture with an actual supported analyzer; probe/trigger/session contracts and `eda-debug`.
  - **Budget / non-goals:** B3/B5/B6; no arbitrary-signal visibility, zero timing/resource cost, mandatory GUI, proprietary GAO compatibility, active stimulus or own-silicon prerequisite.
  - [ ] **DBG-02.1** Integrate one qualified analyzer IP and insertion/wrapper flow with explicit resource and capability limits.
    - [ ] **DBG-02.1.1** Evaluate LiteScope first and record the adoption decision, exact core/generator/host/bridge versions and license/dependency review under IP-02; retain Manta, wbscope and Raptor as separately classified references.
    - [ ] **DBG-02.1.2** Qualify one capture clock, bounded probe widths/depth, BRAM storage and a documented basic trigger subset; define the sampling edge, input pipeline latency, capture enable and pre/post-trigger sample convention.
    - [ ] **DBG-02.1.3** Separate compile-time probe wiring/depth/trigger resources from runtime settings actually supported by the core. Require rebuild for structural changes; reject unsupported trigger operators, excess resources and unavailable probes instead of silently truncating.
  - [ ] **DBG-02.2** Bind probe routing and symbols to the exact instrumented artifacts and the actual programmed design.
    - [ ] **DBG-02.2.1** Define a versioned debug manifest with original/instrumented source hashes, probe bit ordering/widths/names, clock, core parameters, device revision, tool identities and final bitstream digest.
    - [ ] **DBG-02.2.2** Qualify a runtime design/core identity check or equally evidenced exclusive programming-session association before capture. An embedded build token maps to the final-image digest through the manifest; do not require a bitstream to contain its own final hash or mislabel a token as cryptographic attestation.
    - [ ] **DBG-02.2.3** Reject stale maps, the wrong programmed design, unknown identity and ambiguous targets; invalidate the association on reprogramming, reset/reconnect where identity is lost, or lease loss. Host-side manifest agreement alone is insufficient.
  - [ ] **DBG-02.3** Rebuild and verify instrumentation before authorized programming.
    - [ ] **DBG-02.3.1** Keep normal and instrumented source/netlist/route/bitstream/cache artifacts separate; include probe/core/transport/constraint changes in action keys and preserve original DUT ports and behavior contracts.
    - [ ] **DBG-02.3.2** Apply the qualified VER-03 mapped/route/final-image checks to the supported instrumented profile and CON-02 timing gates to DUT, capture and transport clocks. Report added LUT/register/RAM use, fanout, timing and measurement conditions; do not assume debug is nonintrusive physically.
    - [ ] **DBG-02.3.3** Use HW-02 target plans and exclusive leases; build never programs implicitly. Compare normal and instrumented DUT outputs using formal/simulation under documented assumptions, separately from analyzer correctness and timing closure.
  - [ ] **DBG-02.4** Acquire and export captures through one independently qualified debug transport.
    - [ ] **DBG-02.4.1** Prefer a reference-board UART transport when available; qualify discover/identify/configure/arm/status/trigger/stop/read/rearm operations with bounded messages/timeouts and CDC/reset handling. JTAG user-debug access is a separate device capability, not a consequence of programmer support.
    - [ ] **DBG-02.4.2** Define readout ordering, sample count, trigger index, capture state, reset/abort/disconnect recovery and partial-read integrity; reject malformed lengths and do not automatically repeat an ambiguous hardware operation.
    - [ ] **DBG-02.4.3** Export VCD plus versioned capture metadata first, preserving sample indices, time units, clock-domain identity and invalid/incomplete regions. Record a known/measured sampling rate or explicitly unknown timebase; never invent wall-clock precision or synchronous cross-domain timing.
  - [ ] **DBG-02.5** Verify capture semantics against independent golden traces and negative fixtures.
    - [ ] **DBG-02.5.1** Test trigger/sample alignment, earliest/latest trigger, pre/post-trigger boundaries, full-depth wrap, reset while armed/capturing, rearm and supported capture enables; use a separately implemented model, not the production core to calculate expectations.
    - [ ] **DBG-02.5.2** Exercise clock loss, overflow/incomplete capture, asynchronous readout, disconnect, stale sessions, malformed payloads, wrong bitstreams and unavailable probes. Label timeout/unknown/unavailable distinctly; hardware samples cannot reveal simulation X/Z or analog metastability directly.
    - [ ] **DBG-02.5.3** Use qualified RTL simulation and applicable formal properties for capture/control/CDC contracts; mutate sample ordering, trigger index and manifest identities and verify detection. Preserve proof scope, assumptions and shared-model limitations.
  - [ ] **DBG-02.6** Demonstrate a real reference-board capture and publish reproducible evidence.
    - [ ] **DBG-02.6.1** Run a counter/handshake or equivalent conventional-HDL fixture with an independent expected sequence; trigger, read and correlate the capture with the exact qualified reference build and source identities on an explicitly selected board.
    - [ ] **DBG-02.6.2** Cross-check exported samples with an independent reader/reference trace and show CLI-only recovery from an interrupted session. DBG-03's scalable indexer and a desktop viewer are not prerequisites for this initial export check.
    - [ ] **DBG-02.6.3** Archive actual input RTL, generated instrumentation RTL, final-image/debug-manifest hashes, clock/trigger settings, raw/exported samples, commands, timing/resource reports and B5/B6 measurements. Simulation-only evidence cannot close this reference-board parent.

- [ ] **DBG-03 — Independently testable waveform indexing and offline replay**
  - **Depends on:** FND-10, VER-01, PERF-02.
  - **Capability / modules:** Query large captures without loading them whole; waveform indexes, capture windows and replay contracts.
  - **Budget / non-goals:** B3/B4; no live board/Nodal-compiler dependency, proprietary simulator replacement or unsupported waveform-format promise.
  - [ ] **DBG-03.1** Evaluate Wellen or a justified reader for a pinned VCD/FST subset with streaming/selected-signal ingestion, checked offsets, exact time units and signal-type metadata; record dependencies and licenses.
  - [ ] **DBG-03.2** Build persistent time/signal indexes and paged query APIs with bounded caches and resumable ingestion; measure real behavior rather than assume the library provides the budget guarantees.
  - [ ] **DBG-03.3** Preserve dropped-sample, overflow, unknown/X and incomplete-capture semantics; distinguish simulation values from binary hardware observations and never interpolate a missing digital event as fact.
  - [ ] **DBG-03.4** Support offline replay and source navigation from immutable capture/build identities without a live board; independently authored trace/map fixtures must cover missing source maps and stale identity failures.
  - [ ] **DBG-03.5** Cross-check supported waveform samples against independent readers/synthetic traces, including >4 GiB offsets, time overflow and corrupt files; disclose shared-parser risks when using GTKWave/Surfer-related components.
  - [ ] **DBG-03.6** Demonstrate B3/B4 on large trace fixtures and interrupted-ingestion recovery; archive exactness, index compatibility and memory evidence. Live-session integration remains required in DBG-05.5 and UX-03, not silently waived by this offline closure.

- [ ] **DBG-04 — Advanced regional and multi-clock debug**
  - **Depends on:** FND-10, DBG-02, DBG-03, DBG-05, CON-05, FLOW-05.
  - **Capability / modules:** Debug advanced engine-supported configurations; cross-domain correlation and configuration-set debug manifests.
  - **Budget / non-goals:** B4/B5/B8; no implied synchrony across clocks or support for unqualified partial reconfiguration.
  - [ ] **DBG-04.1** Model per-domain timebase, synchronization markers and explicit uncertainty for cross-clock or cross-device observations.
  - [ ] **DBG-04.2** Track probe availability and symbol validity across supported regional/reconfiguration transitions using engine legality contracts.
  - [ ] **DBG-04.3** Integrate permitted debug access and security/lifecycle restrictions without exposing protected data through cached sessions; disable active IO/memory writes or virtual stimulus unless separately qualified and explicitly authorized.
  - [ ] **DBG-04.4** Provide bounded causal/navigation queries and audit all configuration/session transitions; keep optional compression, streaming and advanced triggers capability-gated with separately defined loss and bandwidth semantics.
  - [ ] **DBG-04.5** Test stale region maps, reset races, desynchronized captures, access revocation and unsupported debug configurations.
  - [ ] **DBG-04.6** Demonstrate qualified multi-domain/regional scenarios and honest uncertainty; attach B4/B5/B8 and cross-layer evidence.

- [ ] **DBG-05 — Nodal-source insertion and own-fabric debug qualification**
  - **Depends on:** FND-10, DBG-02, DBG-03, TOOL-04, TOOL-05, VER-04.
  - **Capability / modules:** Extend the qualified analyzer workflow to actual Nodal exports and a supported own-fabric target; compiler insertion/provenance adapter and fabric debug package.
  - **Budget / non-goals:** B3/B4/B5/B6; no invented compiler API, arbitrary optimized-away-signal visibility, duplicated core/device logic, or substitution of emulation for silicon qualification.
  - [ ] **DBG-05.1** Qualify actual Nodal source-location/export identities and compiler-assisted probe selection/insertion under TOOL-04; preserve aliases/hierarchy and explicit optimized-away/merged/cloned/unavailable states through the instrumented flow.
  - [ ] **DBG-05.2** Execute a real Nodal-generated IP package through the same IP-02 contract as conventional HDL, retaining the Nodal-specific IP-02.4 acceptance formerly blocked on TOOL-04; pin generator/compiler/runtime and validate legal/illegal parameters.
  - [ ] **DBG-05.3** Qualify analyzer RAM/clock mapping, transport/user-debug endpoint and configuration/probe identities against the actual TOOL-05 device package and upstream provider capabilities; unsupported endpoints keep this child open.
  - [ ] **DBG-05.4** Apply the original-DUT/instrumented semantic, timing, final-image and capture fault checks to Nodal and own-fabric artifacts; load the actual final image through the real simulated configuration path, then exercise a qualified emulation or physical target under VER-04/HW-02.
  - [ ] **DBG-05.5** Index actual captured waveforms through DBG-03 and navigate back to Nodal source; test renamed helpers, aliases, unavailable probes, old source maps, reprogramming and loss/recovery of target identity. Keep normal/debug evidence separate.
  - [ ] **DBG-05.6** Demonstrate both the Nodal-source path and own-fabric capture with actual Nodal Scala, corresponding actual generated Verilog, instrumented RTL, final-image identity, waveforms and commands; record B3/B4/B5/B6 and exact simulation/emulation/board limits. Full parent closure requires both paths; silicon claims additionally require HW-03/VER-05 evidence.
