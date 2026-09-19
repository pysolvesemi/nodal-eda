# IP — IP catalog and generator track

Hard gate: FND-10. Nodal-EDA manages qualified IP packages and generator execution; it does not implement SRAM compilers, analog synthesis or the FPGA's hard macros. Hardware must have compatible simulation, synthesis, constraints and device views. See [architecture](../../architecture.md).

Use [REF-12 and REF-14..REF-16](../../reference-implementations.md) for package/generator and analyzer design references. The first IP-02 acceptance uses conventional HDL and a qualified external generator, without TOOL-04. The actual Nodal-generated path formerly included in IP-02.4 is retained in DBG-05.2 after TOOL-04; this sequencing change does not advertise untested Nodal support.

- [ ] **IP-01 — Immutable IP catalog and lock model**
  - **Depends on:** FND-10, TOOL-01, SEC-01.
  - **Capability / modules:** Discover and lock compatible IP; `eda-packages`, IPManifest and project lock extensions.
  - **Budget / non-goals:** B0/B3; no public marketplace or automatic execution of downloaded generators.
  - [ ] **IP-01.1** Define package identity, version/digest, license/notice metadata, dependency graph and exact device/tool/language capabilities.
  - [ ] **IP-01.2** Separate RTL, simulation, constraints, documentation, test vectors and generator executables with explicit trust classification.
  - [ ] **IP-01.3** Resolve offline/local catalogs deterministically with side-by-side versions and reject incompatible dependency or device combinations.
  - [ ] **IP-01.4** Record legal distribution/usage approval and proprietary-artifact access without embedding customer or foundry assets in the public repository; apply the reference-catalog adoption record to code, RTL, examples, generators and device databases separately.
  - [ ] **IP-01.5** Test conflicting versions, missing views, malformed manifests, untrusted executables and changed dependency contents.
  - [ ] **IP-01.6** Demonstrate a locked reference IP package and deterministic failure cases; record B0/B3, trust and compatibility evidence.

- [ ] **IP-02 — Reproducible generator execution and parameter validation**
  - **Depends on:** FND-10, IP-01, TOOL-02.
  - **Capability / modules:** Configure a small qualified IP and build its outputs; generator parameter/result contracts and adapters.
  - **Budget / non-goals:** B0/B2/B3; no Nodal-only requirement or invented physical PLL implementation.
  - [ ] **IP-02.1** Define typed parameters, units, legal combinations and target capability checks for a small qualified FIFO/memory/analyzer or equivalent package. For the DBG-02 analyzer package, pin probe width/depth/clock, trigger resources, BRAM mapping, transport and generated constraint views; qualify it before DBG-02 closure even if IP-02 used a different initial fixture.
  - [ ] **IP-02.2** Execute trusted generators in isolated workspaces with pinned inputs, deterministic seeds and explicit output/view manifests.
  - [ ] **IP-02.3** Cache only pure generation outputs and include generator/tool/device identity in keys; keep generated constraints traceable to parameters.
  - [ ] **IP-02.4** Define one artifact/contract path for conventional and Nodal-generated packages; qualify real conventional-HDL generation here without a Nodal compiler. Require actual Nodal execution in DBG-05.2, and reject that capability until its pinned compiler/generator integration is qualified.
  - [ ] **IP-02.5** Check generated RTL with supported formal/simulation fixtures and parameter boundaries; verify declared black boxes have the required views.
  - [ ] **IP-02.6** Demonstrate actual parameter-to-artifact output, generated RTL where applicable and B0/B3 measurements; record supported parameter limits and the adoption/rejection decision for evaluated generators. No study-only reference is a selected dependency.

- [ ] **IP-03 — Qualified hard-resource IP views and collateral**
  - **Depends on:** FND-10, IP-02, CON-03.
  - **Capability / modules:** Configure supported BRAM/DSP/PLL/IO resources with consistent collateral; extended IP/device-view schemas.
  - **Budget / non-goals:** B0/B3/B4; no automatic analog macro design or unqualified high-speed PHY support.
  - [ ] **IP-03.1** Bind hard-resource parameters/modes to actual device capabilities and documented legal clock/electrical settings.
  - [ ] **IP-03.2** Verify simulation/synthesis/constraints/configuration view agreement and reject missing required timing or physical evidence.
  - [ ] **IP-03.3** Import characterization/model versions with explicit PVT and simulation limitations; preserve opaque proprietary views with access controls.
  - [ ] **IP-03.4** Create generated usage examples and integration diagnostics for clocking, reset, IO-bank and cascade requirements.
  - [ ] **IP-03.5** Test legal/illegal mode combinations, corner changes, missing black-box models and stale device mappings with provider-approved vectors.
  - [ ] **IP-03.6** Demonstrate one actual hard-resource configuration through build/simulation and timing evidence; record B0/B3/B4 and silicon limits.

- [ ] **IP-04 — Hierarchical IP assembly and controlled migration**
  - **Depends on:** FND-10, IP-03, FLOW-05, SEC-03.
  - **Capability / modules:** Reuse qualified subsystems across configurations; hierarchical IP/interface, migration and partition manifests.
  - **Budget / non-goals:** B1/B3/B6; no second HDL or full schematic-capture engine before customer need is established.
  - [ ] **IP-04.1** Represent typed interfaces, clocks/resets and dependency boundaries for hierarchical IP composition with engine-supported partitioning.
  - [ ] **IP-04.2** Propagate interface and constraint changes into cache/checkpoint invalidation and compatibility diagnostics.
  - [ ] **IP-04.3** Provide explicit version migrations and compare generated collateral before accepting updates; never silently replace locked IP.
  - [ ] **IP-04.4** Apply tenant/license/access policy to shared IP and remote generation; preserve offline qualified builds.
  - [ ] **IP-04.5** Test interface drift, clock-domain mismatch, stale regional artifacts and denied proprietary views using independent expected outcomes.
  - [ ] **IP-04.6** Demonstrate a supported subsystem migration and full-build equivalence/qualification; retain B1/B3/B6 and compatibility evidence.
