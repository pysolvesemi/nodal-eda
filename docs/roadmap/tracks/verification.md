# VER — Independent verification and quality track

Hard gate: FND-10. Foundation's bootstrap tests run before this track. This track adds independent evidence, not a second copy of production parsers. Detailed oracle boundaries and CI lanes are in [verification.md](../../verification.md). Hardware formal tools validate supported hardware artifacts, not Rust itself.

- [ ] **VER-01 — Independent oracle, corpus and evidence harness**
  - **Depends on:** FND-10.
  - **Capability / modules:** Reproduce expected results and classify failures; `tests/oracles`, fixture registry and EvidenceManifest.
  - **Budget / non-goals:** B0-B3; no tests that derive their only expected output from the same production implementation.
  - [ ] **VER-01.1** Register reviewed reference projects, direct scripts, independent expected results, licenses and fixture provenance.
  - [ ] **VER-01.2** Implement separate small DAG/state/cache models and hand-reviewed schema/constraint/configuration vectors.
  - [ ] **VER-01.3** Standardize pass/fail/unknown/unavailable/skipped/bounded-only outcomes and exact source/tool/device/host identity in evidence.
  - [ ] **VER-01.4** Add property/randomized test generation with retained seeds and minimization, plus mutation hooks for intentional defect classes.
  - [ ] **VER-01.5** Verify the harness detects wrong outputs, missing tests, ignored constraints and stale artifacts rather than merely a tool exit code.
  - [ ] **VER-01.6** Demonstrate passing references and intentionally failing mutants; retain B0-B3 and oracle-independence evidence.

- [ ] **VER-02 — Direct-tool differential flow validation**
  - **Depends on:** FND-10, VER-01, TOOL-02, FLOW-02.
  - **Capability / modules:** Verify product orchestration matches a qualified direct flow; `tests/differential`, canonical comparison and support-matrix records.
  - **Budget / non-goals:** B3/B6; same-engine comparisons validate orchestration, not independent synthesis correctness.
  - [ ] **VER-02.1** Run direct reviewed scripts and Nodal-EDA on the same pinned device/tool/model/source/constraint/seed/thread tuple.
  - [ ] **VER-02.2** Compare effective invocation intent, accepted constraints, artifact structures, behavior and raw/normalized results.
  - [ ] **VER-02.3** Use exact byte equality only for explicitly qualified deterministic artifacts; record permitted nonsemantic normalization without hiding differences.
  - [ ] **VER-02.4** Compare clean, cached and resumed results after changes to every meaningful action-key component.
  - [ ] **VER-02.5** Include wrong-pin, missing-clock, unroutable-design, tool-error, absent-output and misleading-success-log mutants.
  - [ ] **VER-02.6** Demonstrate complete differential coverage for the MVP tuple and detected mutants; archive B6, reproducibility limits and raw evidence.

- [ ] **VER-03 — Formal and simulation validation of generated hardware**
  - **Depends on:** FND-10, VER-02, TOOL-04.
  - **Capability / modules:** Validate supported compiler/export/wrapper hardware artifacts; `tests/formal`, simulation adapters and proof-assumption records.
  - **Budget / non-goals:** B2/B3/B8; no assumption that EQY/SBY prove Rust logic or arbitrary analog/multi-clock designs.
  - [ ] **VER-03.1** Select supported actual Nodal-export and adapter-generated HDL fixtures with independent golden behavior and reproducible commands.
  - [ ] **VER-03.2** Integrate qualified EQY equivalence and SBY property runs where applicable; pin solvers and supported language features.
  - [ ] **VER-03.3** Document reset/initial-state relations, clock/latency assumptions, X semantics and memory/black-box models for every proof.
  - [ ] **VER-03.4** Add independent simulation and boundary/parameter fixtures; retain counterexamples, generated RTL and source provenance.
  - [ ] **VER-03.5** Inject incorrect widths, reset polarity, cell modes and source-map mismatches; distinguish formal proof, bounded result, timeout and unavailable.
  - [ ] **VER-03.6** Demonstrate actual source/generated-Verilog evidence and valid proofs/simulation outcomes; document every excluded capability and measured test cost.

- [ ] **VER-04 — Fabric, configuration and hardware-path cross-checks**
  - **Depends on:** FND-10, VER-03, TOOL-05, HW-02.
  - **Capability / modules:** Validate own-fabric integration and configuration delivery; config oracles, fabric evidence and cross-layer fixtures.
  - **Budget / non-goals:** B2/B3/B5/B8; no cross-architecture bitstream/PPA equality or treating individual resource coverage as universal proof.
  - [ ] **VER-04.1** Build an independent small configuration/feature decoder with fixed reference vectors, not the production encoder's mapping reused backward.
  - [ ] **VER-04.2** Check reserved fields, addressing, declared shared-bit/mode semantics, target revisions and single-feature mutation effects.
  - [ ] **VER-04.3** Load actual produced bitstreams through real simulated configuration paths and compare specified user behavior under explicit reset/clock contracts.
  - [ ] **VER-04.4** Import nodal-fpga primitive/tile/configuration proof and coverage evidence; record compatible FABulous comparisons separately when TOOL-03 is complete. Independent configuration and golden-behavior checks remain mandatory regardless of that optional adapter.
  - [ ] **VER-04.5** Exercise qualified emulation/programmer paths and wrong-device/corrupt-image/loader-failure cases; retain configuration-to-source identity.
  - [ ] **VER-04.6** Demonstrate cross-layer agreement and detected configuration mutants with actual artifacts; record B5/B8 and separate remaining silicon qualification.

- [ ] **VER-05 — Commercial regression, fuzzing and silicon correlation**
  - **Depends on:** FND-10, VER-04, SEC-02, PERF-03, HW-03.
  - **Capability / modules:** Qualify the first commercial profile with independent negative and lab evidence; regression corpus and release evidence aggregator.
  - **Budget / non-goals:** B8; no green release with missing advertised checks or emulation substituted for required silicon evidence.
  - [ ] **VER-05.1** Expand property/fuzz/mutation campaigns over schemas, archives, constraints, reports, cache keys, logs and hardware plans with minimized failures.
  - [ ] **VER-05.2** Inject process/disk/power/network interruption at publication/recovery boundaries; verify state invariants and no false successful cache entries.
  - [ ] **VER-05.3** Run old-project/schema/device/tool compatibility and offline install/update/replay matrices on exact release candidates.
  - [ ] **VER-05.4** Correlate the shared known-answer corpus across simulation, qualified gate-level evidence, emulation and actual target silicon with conditions recorded.
  - [ ] **VER-05.5** Enforce correctness, constraint completeness, security and performance gates; keep named reviewed exceptions visible rather than treating them as passes.
  - [ ] **VER-05.6** Publish final-head qualification evidence and actual lab results for the declared commercial profile; archive B8 and outstanding exclusions.

- [ ] **VER-06 — High-end, incremental and fleet qualification**
  - **Depends on:** FND-10, VER-05, FLOW-05, PERF-04, SEC-04.
  - **Capability / modules:** Independently qualify advanced workflows at scale; hierarchical/reference comparisons and professional acceptance corpus.
  - **Budget / non-goals:** B8; no monolithic proof claim for an entire high-end device or comparison of incompatible timing models.
  - [ ] **VER-06.1** Compare qualified full and incremental/regional builds with matching interfaces, timing scenarios, device/configuration revisions and feature sets.
  - [ ] **VER-06.2** Validate cross-region/die clocks, constraints, configuration sets and debug identities with compositional evidence supplied by owning engines.
  - [ ] **VER-06.3** Stress S3 data, concurrent projects, remote workers, tenant boundaries, slow clients and hardware-session failure modes.
  - [ ] **VER-06.4** Recheck support/upgrade/rollback/key-rotation and long-lived project/device/tool compatibility on the exact high-end candidate matrix.
  - [ ] **VER-06.5** Correlate silicon-dependent claims with actual characterized target data; perform independent review of oracle assumptions and residual coverage gaps.
  - [ ] **VER-06.6** Publish reproducible final-head professional-profile evidence with B8 and explicit unsupported capabilities; only then permit REL-05 closure.
