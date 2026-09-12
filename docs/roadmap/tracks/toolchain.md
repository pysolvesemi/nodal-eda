# TOOL — Toolchain and device integration track

Hard gate: FND-10. Tool availability is an external capability, not an assumption. Pin exact releases/commits, models and databases. See [sources S02/S03/S06](../../research-sources.md) and the [comparison limits](../../verification.md).

- [ ] **TOOL-01 — Toolchain and device capability resolution**
  - **Depends on:** FND-10.
  - **Capability / modules:** Inspect a supported flow before running it; `eda-adapters`, `eda-packages`, ToolchainLock and DevicePackage.
  - **Budget / non-goals:** B0/B3; no automatic execution of discovered binaries or universal device support claims.
  - [ ] **TOOL-01.1** Resolve exact tool binaries/runtime libraries/plugins and device/timing/configuration packages into immutable locked identities.
  - [ ] **TOOL-01.2** Define supported language subset, stage/media types, timing/constraint features, native checkpoint and programming capabilities per tuple.
  - [ ] **TOOL-01.3** Validate part/package/speed/revision consistency and reject mixed databases, unknown features and incompatible schema versions.
  - [ ] **TOOL-01.4** Add local/offline package discovery with explicit trust and missing-dependency diagnostics; document dependency redistribution notices.
  - [ ] **TOOL-01.5** Test fake versions, wrong architectures, incompatible plugins, tampered model files and changed executable libraries.
  - [ ] **TOOL-01.6** Demonstrate capability inspection and failure before expensive work on an invalid tuple; record B0/B3 and compatibility evidence.

- [ ] **TOOL-02 — Qualified Yosys/nextpnr reference-device adapter**
  - **Depends on:** FND-10, TOOL-01.
  - **Capability / modules:** Synthesize and implement one explicitly supported open-device fixture; `adapters/yosys`, `adapters/nextpnr`, packer wrapper.
  - **Budget / non-goals:** B2/B6; no new synthesizer, router or claim of full SystemVerilog/VHDL.
  - [ ] **TOOL-02.1** Select and pin one supported reference part/package and matching synthesis, place/route, database and bitstream-packer versions.
  - [ ] **TOOL-02.2** Implement safe per-stage invocations and exact input/output contracts; keep technology mapping ownership and source order explicit.
  - [ ] **TOOL-02.3** Normalize useful status/diagnostics with raw-log retention and schema-versioned parser fixtures; preserve opaque implementation artifacts.
  - [ ] **TOOL-02.4** Supply independent direct scripts and small positive/negative fixtures including arithmetic, registers and supported memories.
  - [ ] **TOOL-02.5** Validate supported constructs, constraint delivery and invalid/unroutable failures without silently substituting defaults.
  - [ ] **TOOL-02.6** Demonstrate actual standalone adapter runs and locked reproducibility profile; record tool/device digests, B6 overhead and known limitations.

- [ ] **TOOL-03 — FABulous reference-fabric workflow**
  - **Depends on:** FND-10, TOOL-02, FLOW-02.
  - **Capability / modules:** Run a qualified reference fabric's compile/configure/simulate workflow; `adapters/fabulous-reference`, fabric-evidence manifest.
  - **Budget / non-goals:** B2/B3/B6; no FABulous rewrite, assumed cross-architecture bitstream equality or claim that simulation qualifies silicon. This optional reference increment does not block own-device qualification.
  - [ ] **TOOL-03.1** Pin a usable FABulous release/commit, architecture, models, toolchain and legal test corpus; validate actual commands for that version.
  - [ ] **TOOL-03.2** Wrap fabric artifact references, user-design compilation, configuration loading and simulator invocation without duplicating fabric generation.
  - [ ] **TOOL-03.3** Capture original design, mapped artifacts, actual bitstream, simulator inputs/results and architecture/configuration digests.
  - [ ] **TOOL-03.4** Compare defined user behavior under reset/latency/clock assumptions with an independent testbench; do not treat arbitrary byte differences as failures.
  - [ ] **TOOL-03.5** Inject corrupt configuration, wrong fabric revision and simulator failure; require errors rather than a green workflow status.
  - [ ] **TOOL-03.6** Demonstrate the real reference simulation and archive outputs/B6 measurements; keep this increment open when the qualified reference is unavailable.

- [ ] **TOOL-04 — Nodal-HDL compiler adapter and source handoff**
  - **Depends on:** FND-10, TOOL-02, FLOW-02.
  - **Capability / modules:** Build Nodal projects using actual supported exports; `adapters/nodal-hdl`, compiler-export and provenance metadata.
  - **Budget / non-goals:** B2/B3/B6; no MLIR runtime or new Scala frontend inside nodal-eda. A new direct mapped-netlist exporter is not required for this increment.
  - [ ] **TOOL-04.1** Inspect and pin nodal-hdl's real CLI/export/source-map contracts; publish a tested support matrix instead of assuming native FPGA mapping exists.
  - [ ] **TOOL-04.2** Integrate the supported Verilog-export-to-Yosys flow first, including compiler plugins, Scala/JVM runtime identity and generated dependencies.
  - [ ] **TOOL-04.3** Implement capability negotiation: accept a direct mapped-netlist route only when both providers are qualified for it, otherwise select the verified Verilog fallback or explicitly reject a forced unsupported route; test that mapping is not duplicated.
  - [ ] **TOOL-04.4** Preserve source identities, generated RTL and many-to-many provenance with explicit optimized-away/unavailable states.
  - [ ] **TOOL-04.5** Test generated artifact mutation, compiler errors, mismatched schemas and non-Nodal projects that build without any JVM dependency.
  - [ ] **TOOL-04.6** Record actual Nodal Scala source and actual generated Verilog plus E2E output and B6 evidence; unsupported optional paths stay capability-gated.

- [ ] **TOOL-05 — Nodal-FPGA device package and bring-up contract**
  - **Depends on:** FND-10, TOOL-04, CON-02.
  - **Capability / modules:** Implement a user design for an actual supported Nodal device/fabric profile; `adapters/nodal-fpga`, immutable device/evidence packages.
  - **Budget / non-goals:** B0/B3/B4/B6; no duplicated DeviceDB/P&R/STA or automatic analog/ASIC signoff.
  - [ ] **TOOL-05.1** Negotiate real device/compiler/CAD APIs, artifact types, legality checks, clock/constraint coverage and bitstream/configuration identities with nodal-fpga.
  - [ ] **TOOL-05.2** Validate part/package/revision and supported resources/modes; expose query handles rather than copying the whole physical resource graph.
  - [ ] **TOOL-05.3** Connect both qualified Nodal and conventional HDL flows to the same implementation contracts without making Nodal mandatory.
  - [ ] **TOOL-05.4** Attach fabric RTL/model/configuration and available physical-verification manifests to bring-up bundles with explicit evidence ownership.
  - [ ] **TOOL-05.5** Run actual target-fabric functional, invalid-package, unsupported-resource and stale-database tests; propagate engine failures exactly.
  - [ ] **TOOL-05.6** Demonstrate the qualified own-fabric flow and bounded queries; record actual upstream capability evidence, B3/B4/B6 and remaining silicon gates.
