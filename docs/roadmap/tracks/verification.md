# VER — Independent verification and quality track

Hard gate: FND-10. Foundation's bootstrap tests run before this track. This track adds independent evidence, not a second copy of production parsers. Detailed oracle boundaries and CI lanes are in [verification.md](../../verification.md). Hardware formal tools validate supported hardware artifacts, not Rust itself.

[ADR-0001](../../adr/0001-rust-core-external-compiler-boundary.md) defines the core/compiler dependency and availability matrix. Retain independent core tests and real-tool qualification separately; neither a missing compiler nor a passing mock test satisfies an advertised compiler capability.

The [stage-by-stage verification contract](../../verification-pipeline.md) is mandatory acceptance detail. VER-03 now qualifies synthesis, post-route behavior and the final bitstream for the initial open-device flow, before TOOL-04 adds Nodal-specific exports. This deliberately removes the old dependency of VER-03 on TOOL-04; no Nodal-specific tests are discarded, since TOOL-04 must apply the same qualified harness to actual Nodal artifacts. M1 requires VER-03. Existing IDs are preserved, with eighteen further nested subtasks under VER-03 so partial work remains visible.

- [ ] **VER-01 — Independent oracle, corpus and evidence harness**
  - **Depends on:** FND-10.
  - **Capability / modules:** Reproduce expected results and classify failures; `tests/oracles`, fixture registry and EvidenceManifest.
  - **Budget / non-goals:** B0-B3; no tests that derive their only expected output from the same production implementation.
  - [ ] **VER-01.1** Register reviewed reference projects, direct scripts, independent expected results, licenses and fixture provenance; record shared parsers/models and common-mode oracle risks.
  - [ ] **VER-01.2** Implement separate small DAG/state/cache models and hand-reviewed schema/constraint/configuration vectors, including the stage-artifact and SemanticContract fixtures required by verification-pipeline.md.
  - [ ] **VER-01.3** Standardize pass/fail/unknown/unavailable/skipped/bounded-only outcomes and exact source/tool/device/host identity in evidence; keep execution, functional correctness, route legality, timing and hardware verdicts separate.
  - [ ] **VER-01.4** Add property/randomized test generation with retained seeds and minimization, plus mutation hooks for intentional defect classes.
  - [ ] **VER-01.5** Verify the harness detects wrong outputs, missing tests, ignored constraints and stale artifacts rather than merely a tool exit code; retain the foundation dependency-boundary mutant and a missing-compiler false-success mutant as regression fixtures.
  - [ ] **VER-01.6** Demonstrate passing references and intentionally failing mutants; retain B0-B3 and oracle-independence evidence.

- [ ] **VER-02 — Direct-tool differential flow validation**
  - **Depends on:** FND-10, VER-01, TOOL-02, FLOW-02.
  - **Capability / modules:** Verify product orchestration matches a qualified direct flow; `tests/differential`, canonical comparison and support-matrix records.
  - **Budget / non-goals:** B3/B6; same-engine comparisons validate orchestration, not independent synthesis correctness. VER-03 supplies the separate semantic/legality gate.
  - [ ] **VER-02.1** Run direct reviewed scripts and Nodal-EDA on the same pinned device/tool/model/source/constraint/seed/thread tuple; qualify the traditional-HDL lane without Nodal-HDL, JVM or MLIR/CIRCT compiler packages while retaining its declared reference-tool dependencies.
  - [ ] **VER-02.2** Compare effective invocation intent, accepted constraints, artifact structures, behavior and raw/normalized results; retain original RTL, actual mapped netlist, route evidence, logical features and final binary identities for VER-03.
  - [ ] **VER-02.3** Use exact byte equality only for explicitly qualified deterministic artifacts; record permitted nonsemantic normalization without hiding differences.
  - [ ] **VER-02.4** Compare clean, cached and resumed results after changes to every meaningful action-key component, including adapter, compiler/runtime and export-schema identity where applicable; check unaffected actions remain reusable.
  - [ ] **VER-02.5** Include wrong-pin, missing-clock, unroutable-design, tool-error, absent-output and misleading-success-log mutants.
  - [ ] **VER-02.6** Demonstrate complete differential coverage for the MVP tuple and detected mutants; archive B6, reproducibility limits and raw evidence. Do not label this same-engine comparison independent synthesis/P&R correctness.

- [ ] **VER-03 — Early synthesis, post-route and final-bitstream semantic qualification**
  - **Depends on:** FND-10, VER-02, TOOL-02, FLOW-02, CON-02.
  - **Capability / modules:** Independently check the initial open-device implementation chain; `tests/formal`, `tests/oracles`, simulation/decoder adapters, SemanticContract and stage evidence.
  - **Budget / non-goals:** B2/B3/B8; no new synthesis/P&R engine, assumed universal primitive support, fabricated native Nodal exporter, or substitution of functional simulation for physical timing. Existing performance profiles remain authoritative.
  - [ ] **VER-03.1** Freeze independent reference semantics and a reproducible early corpus.
    - [ ] **VER-03.1.1** Specify ports/pins, signedness, clock edges, configuration completion/reset, initialization, memory modes, enables/stalls, latency and output sampling in a versioned SemanticContract.
    - [ ] **VER-03.1.2** Add hand-reviewed counters, enabled/stalled pipelines, signed/overflow arithmetic, mux/carry and supported memory fixtures plus bounded random circuits and retained seeds.
    - [ ] **VER-03.1.3** Pin independent reference models and simulation tools; inventory shared frontend/device-model assumptions and reject missing primitive models or blanket X masking.
  - [ ] **VER-03.2** Qualify synthesis semantic preservation using actual outputs.
    - [ ] **VER-03.2.1** Compare original RTL with actual technology-mapped netlists using qualified EQY/SBY flows where appropriate, plus separately implemented simulation on the supported corpus.
    - [ ] **VER-03.2.2** Validate reset/initial-state relations, clock/latency contracts, memory and X/refinement semantics, proof scope and reachability; distinguish unbounded proof, bounded result, timeout and unavailable.
    - [ ] **VER-03.2.3** Detect deliberately wrong widths/signedness, carry behavior, reset polarity, enable priority and memory modes; retain minimized counterexamples and source/model/solver hashes.
  - [ ] **VER-03.3** Check packing, selected routes and post-route behavior independently.
    - [ ] **VER-03.3.1** Implement or integrate an independently tested legality checker for site/BEL capacity/modes, shared controls, carry/cascade placement, clocks/IOs, directed PIP reachability and resource conflicts using actual exported route data.
    - [ ] **VER-03.3.2** Reconstruct behavior from actual selected routing and cell modes, including LUT-pin permutations and corresponding INIT changes; compare against both mapped and original circuits, not a re-exported pre-route netlist.
    - [ ] **VER-03.3.3** Detect missing/reversed PIPs, wrong sinks, shorted unrelated nets, illegal resource sharing and mismatched LUT permutations; use independent tiny device fixtures to expose common-model errors.
  - [ ] **VER-03.4** Reconstruct and check the exact final binary bitstream.
    - [ ] **VER-03.4.1** Qualify final.bin -> iceunpack -> icebox_vlog -> reconstructed Verilog for a declared supported iCE40 subset, or an equivalently evidenced independent decoder for the selected reference device. Never substitute the pre-icepack ASCII/FASM input.
    - [ ] **VER-03.4.2** Validate physical-pin/port correspondence, device revision, initialization, LUT/FF/memory/routing modes and decoded feature agreement with the route artifact; keep unsupported features explicitly unqualified.
    - [ ] **VER-03.4.3** Compare reconstructed behavior against original RTL using qualified formal and cycle-accurate simulation checks; preserve the exact binary hash, decoder/model identity and counterexamples. A checksum or encode/decode round trip alone is insufficient.
  - [ ] **VER-03.5** Qualify timing distinctions and demonstrate that verification detects defects.
    - [ ] **VER-03.5.1** Apply CON-02 timing-completeness gates independently of functional equivalence; audit clocks, setup/hold, constraints and model/corner coverage, with direct-backend and small independent timing fixtures.
    - [ ] **VER-03.5.2** Test malformed-image rejection and format-valid semantic mutations, including LUT INIT, frame/field order, register latency and memory addressing; detect every enumerated observable non-equivalent defect and classify equivalent/unobservable mutations.
    - [ ] **VER-03.5.3** Compare controlled seeds/alternative legal implementations by semantics and legality, reporting QoR separately; never require identical placement/routing/bitstream bytes across unlike architectures or encodings.
  - [ ] **VER-03.6** Close the initial real-device verification chain with exact-head evidence.
    - [ ] **VER-03.6.1** Reproduce original -> mapped -> routed -> final binary -> reconstructed behavior on the pinned reference profile; record hashes, commands, assumptions, checker results and measured B2/B3/B8 resource use.
    - [ ] **VER-03.6.2** Prove the harness reports missing exports, stale evidence, checker failure, timeouts and unsupported models honestly; verify a cached result cannot retain a proof after relevant semantic inputs change.
    - [ ] **VER-03.6.3** Publish actual reference RTL, generated mapped/reconstructed Verilog and cycle traces with positive and negative cases; keep Nodal-source extension tests in TOOL-04 and own-fabric loader/hardware tests in TOOL-05/VER-04. No M1 closure before every required descendant passes.

- [ ] **VER-04 — Fabric, configuration and hardware-path cross-checks**
  - **Depends on:** FND-10, VER-03, TOOL-05, HW-02.
  - **Capability / modules:** Validate own-fabric integration and configuration delivery; config oracles, fabric evidence and cross-layer fixtures.
  - **Budget / non-goals:** B2/B3/B5/B8; no cross-architecture bitstream/PPA equality or treating individual resource coverage as universal proof. TOOL-05 runs initial own-fabric loader simulation before boards; this increment retains integrated hardware qualification.
  - [ ] **VER-04.1** Build an independent small configuration/feature decoder with fixed reference vectors, not the production encoder's mapping reused backward; identify shared device-model assumptions.
  - [ ] **VER-04.2** Check reserved fields, addressing, declared shared-bit/mode semantics, target revisions and single-feature mutation effects; compare decoded final-image features against actual routed resource choices.
  - [ ] **VER-04.3** Load actual produced final bitstreams through real simulated configuration paths and compare specified user behavior under the SemanticContract. Verify configuration completion/reset sequencing; do not replace loader coverage with forced configuration or compare only pre-bitstream models.
  - [ ] **VER-04.4** Import nodal-fpga primitive/tile/configuration, route-legality, compositional proof and feature-interaction coverage evidence; record compatible FABulous/OpenFPGA comparisons separately when qualified. Independent configuration and golden-behavior checks remain mandatory regardless of optional adapters.
  - [ ] **VER-04.5** Exercise qualified emulation/programmer paths and wrong-device/corrupt-image/loader-failure cases; retain configuration-to-source identity. Reuse cycle/event contracts and exact binary hashes across simulation and hardware; do not call transfer success design correctness.
  - [ ] **VER-04.6** Demonstrate cross-layer agreement and detected configuration mutants with actual artifacts; record B5/B8, proof/model exclusions and separate remaining silicon qualification.

- [ ] **VER-05 — Commercial regression, fuzzing and silicon correlation**
  - **Depends on:** FND-10, VER-04, SEC-02, PERF-03, HW-03.
  - **Capability / modules:** Qualify the first commercial profile with independent negative and lab evidence; regression corpus and release evidence aggregator.
  - **Budget / non-goals:** B8; no green release with missing advertised checks or emulation substituted for required silicon evidence.
  - [ ] **VER-05.1** Expand property/fuzz/mutation campaigns over schemas, archives, constraints, reports, cache keys, logs and hardware plans with minimized failures; retain stage-semantic and route/configuration mutants from VER-03/VER-04.
  - [ ] **VER-05.2** Inject process/disk/power/network interruption at publication/recovery boundaries; verify state invariants and no false successful cache entries.
  - [ ] **VER-05.3** Run old-project/schema/device/tool compatibility and offline install/update/replay matrices on exact release candidates; repeat ADR-0001 core/compiler availability and dependency checks for advertised CLI/desktop/service profiles, with separate base-application and optional-tool inventories.
  - [ ] **VER-05.4** Correlate the shared known-answer corpus across simulation, qualified gate-level evidence, emulation and actual target silicon with conditions recorded; keep cycle correctness, physical timing and silicon scope separate.
  - [ ] **VER-05.5** Enforce correctness, constraint completeness, security and performance gates; keep named reviewed exceptions visible rather than treating them as passes. Require complete applicable stage evidence for each advertised device/tool/feature profile.
  - [ ] **VER-05.6** Publish final-head qualification evidence and actual lab results for the declared commercial profile; archive B8 and outstanding exclusions.

- [ ] **VER-06 — High-end, incremental and fleet qualification**
  - **Depends on:** FND-10, VER-05, FLOW-05, PERF-04, SEC-04.
  - **Capability / modules:** Independently qualify advanced workflows at scale; hierarchical/reference comparisons and professional acceptance corpus.
  - **Budget / non-goals:** B8; no monolithic proof claim for an entire high-end device or comparison of incompatible timing models.
  - [ ] **VER-06.1** Compare qualified full and incremental/regional builds with matching interfaces, timing scenarios, device/configuration revisions and feature sets; validate evidence reuse keys and partition/interface assumptions.
  - [ ] **VER-06.2** Validate cross-region/die clocks, constraints, configuration sets and debug identities with compositional evidence supplied by owning engines; use domain-specific contracts rather than a fictitious global cycle for asynchronous clocks.
  - [ ] **VER-06.3** Stress S3 data, concurrent projects, remote workers, tenant boundaries, slow clients and hardware-session failure modes; measure bounded checker/model-reconstruction overhead independently of implementation time.
  - [ ] **VER-06.4** Recheck support/upgrade/rollback/key-rotation and long-lived project/device/tool compatibility on the exact high-end candidate matrix; retain ADR-0001 compiler independence and external-engine isolation rather than making MLIR/CIRCT mandatory as a scaling shortcut.
  - [ ] **VER-06.5** Correlate silicon-dependent claims with actual characterized target data; perform independent review of oracle assumptions and residual coverage gaps.
  - [ ] **VER-06.6** Publish reproducible final-head professional-profile evidence with B8 and explicit unsupported capabilities; only then permit REL-05 closure.
