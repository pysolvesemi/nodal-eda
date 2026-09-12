# HW — Programming and hardware track

Hard gate: FND-10. Hardware operations are explicit, authorized, non-cacheable effects. A successful build never implicitly programs a board. Device protocol semantics belong to qualified providers/nodal-fpga; this track owns safe sessions and workflows. See [verification](../../verification.md), [budgets](../../performance.md) and [source S11](../../research-sources.md#s11).

- [ ] **HW-01 — Hardware discovery, identity and exclusive leases**
  - **Depends on:** FND-10, TOOL-01.
  - **Capability / modules:** Inspect connected targets safely; `eda-hardware`, HardwareTarget/Lease/Capability schemas.
  - **Budget / non-goals:** B0/B5; discovery must not erase, reconfigure or write irreversible state.
  - [ ] **HW-01.1** Define cable, transport, board, chain-position, device/revision and capability identities without assuming a device ID is globally unique.
  - [ ] **HW-01.2** Integrate one qualified discovery provider with a simulator/mock transport and explicit permissions/device-driver prerequisites.
  - [ ] **HW-01.3** Acquire exclusive target leases and reject ambiguous selection or simultaneous operations from another client.
  - [ ] **HW-01.4** Separate read-only inspection from writes; define cancellation, timeout and disconnect states in the hardware protocol.
  - [ ] **HW-01.5** Test duplicate IDs, chain changes, cable removal, denied permissions, lease loss and stale target metadata.
  - [ ] **HW-01.6** Demonstrate read-only discovery on an approved board and mock faults; record B5, supported transport and permission limitations.

- [ ] **HW-02 — Safe programming plans and verification**
  - **Depends on:** FND-10, HW-01, FLOW-03, SEC-01.
  - **Capability / modules:** Plan/apply an authorized configuration or flash operation; HardwarePlan, ProgramResult and audit records.
  - **Budget / non-goals:** B3/B5; no automatic erase, irreversible fuse/security operations or unconditional retry after uncertainty.
  - [ ] **HW-02.1** Bind each plan to exact bitstream digest, device/package/revision, cable/chain identity, memory address/range and requested operation.
  - [ ] **HW-02.2** Require explicit target selection and authorization at apply time; revalidate identity and lease immediately before the write.
  - [ ] **HW-02.3** Implement bounded transfer/progress with provider-specific safe cancellation and optional supported readback/checksum verification.
  - [ ] **HW-02.4** Add independent functional known-answer checks and distinguish transfer success, readback verification and design correctness.
  - [ ] **HW-02.5** Inject wrong target, corrupt image, denied readback, disconnect and power loss on recoverable hardware; preserve unknown state and recovery instructions.
  - [ ] **HW-02.6** Demonstrate a qualified programming/recovery cycle with an explicit safety plan; record B5, actual results and non-supported operations.

- [ ] **HW-03 — Own-device bring-up and characterization sessions**
  - **Depends on:** FND-10, HW-02, TOOL-05.
  - **Capability / modules:** Run traceable tests on own-fabric emulation and actual silicon; lab session/instrument/evidence manifests.
  - **Budget / non-goals:** B5/B8; FPGA emulation is not ASIC timing, analog or reliability qualification.
  - [ ] **HW-03.1** Integrate the actual nodal-fpga loader/protocol and recoverable bring-up board with versioned target/configuration contracts.
  - [ ] **HW-03.2** Package known-answer bitstreams and reference results from simulation/emulation using immutable source/fabric/tool identities.
  - [ ] **HW-03.3** Record chip/board revision, supplies, temperature, clocks, instruments and test environment for each silicon observation.
  - [ ] **HW-03.4** Import qualified measurements and correlate expected functionality/timing within documented assumptions and instrument uncertainty.
  - [ ] **HW-03.5** Test interrupted bring-up, wrong revision and missing characterization evidence; keep unavailable silicon tasks open.
  - [ ] **HW-03.6** Demonstrate actual target-silicon known-answer tests and a reproducible lab record; do not close this parent on emulation alone.

- [ ] **HW-04 — Production and multi-board lab workflows**
  - **Depends on:** FND-10, HW-03, DBG-02, REL-02.
  - **Capability / modules:** Auditable qualified board programming/test recipes; station/lot/recipe contracts and hardware-session service.
  - **Budget / non-goals:** B5/B8; not an ATE/DFT platform replacement and no default irreversible security provisioning.
  - [ ] **HW-04.1** Introduce optional authenticated persistent lab sessions with device leases, operator roles and bounded multi-board concurrency.
  - [ ] **HW-04.2** Bind approved recipes to released artifacts, board revisions, station calibration and test requirements; prevent unreviewed recipe substitutions.
  - [ ] **HW-04.3** Preserve per-unit audit/result records and explicit retry/rework disposition without claiming exactly-once hardware effects.
  - [ ] **HW-04.4** Define separate approval/recovery contracts for any future irreversible provisioning; keep key material outside ordinary build/support paths.
  - [ ] **HW-04.5** Exercise station crash, cable swaps, duplicate completion, lost lease and mixed revisions; prove no cross-target write or false pass.
  - [ ] **HW-04.6** Demonstrate a qualified multi-board recipe and traceability export; record B5/B8, safety review and production-scope limits.
