# REL — Distribution, commercial qualification and support track

Hard gate: FND-10. A commercial release is an exact, independently tested support matrix, not a label attached to an unqualified engine. This track owns distribution and acceptance, not a new licensing business model or foundry signoff. See [verification](../../verification.md), [performance](../../performance.md) and [sources](../../research-sources.md).

- [ ] **REL-01 — Reproducible headless distribution and support manifest**
  - **Depends on:** FND-10, TOOL-02, SEC-01.
  - **Capability / modules:** Install and replay a pinned reference workflow; `packaging`, `eda-packages`, release/support manifests.
  - **Budget / non-goals:** B0/B3/B8; no commercial-grade claim yet, mandatory GUI or automatic license bypass.
  - [ ] **REL-01.1** Define supported OS/architecture/tool/device tuples and build reproducible headless application artifacts with exact dependency records.
  - [ ] **REL-01.2** Package or locate external tools according to reviewed distribution rights, notices and runtime dependencies; do not assume executable separation resolves licenses.
  - [ ] **REL-01.3** Implement user-local install/uninstall and offline bundles with side-by-side tool/device versions; report permissions rather than requiring blanket sudo.
  - [ ] **REL-01.4** Produce inspectable redacted support/replay bundles and known-issues metadata without collecting customer source or credentials by default.
  - [ ] **REL-01.5** Test clean host, missing runtime, relocation, offline replay, incompatible package and uninstall without deleting user projects.
  - [ ] **REL-01.6** Demonstrate a fresh supported installation and direct-flow replay; record B0/B3/B8 and the precise pre-commercial support matrix.

- [ ] **REL-02 — First own-device release-candidate qualification**
  - **Depends on:** FND-10, REL-01, SEC-02, TOOL-05, VER-04, HW-03, CON-03.
  - **Capability / modules:** Install a qualified own-device candidate with traceable bring-up evidence; device/release candidate manifests.
  - **Budget / non-goals:** B8; no release based only on mock tools, emulation or an uncharacterized timing estimate.
  - [ ] **REL-02.1** Freeze the candidate source/tree, binaries, models, part/package/revision support, schema versions and device configuration identities.
  - [ ] **REL-02.2** Collect engine/fabric verification, supported timing-corner coverage and actual silicon bring-up evidence from their accountable owners.
  - [ ] **REL-02.3** Validate signed offline delivery, safe programming and support replay against the exact candidate tuple.
  - [ ] **REL-02.4** Publish explicit HDL/constraint/IP/debug limitations and a known-issues matrix; distinguish estimates, proofs, lab observations and signoff records.
  - [ ] **REL-02.5** Run final-head acceptance and reject unexplained mismatch, missing applicable check, unsafe hardware action or invalid cache result.
  - [ ] **REL-02.6** Record the candidate qualification decision and reproducible evidence bundle; keep the parent open until all applicable device gates are genuinely satisfied.

- [ ] **REL-03 — First commercial device/tool release**
  - **Depends on:** FND-10, REL-02, VER-05, CON-04, IP-02, DBG-02.
  - **Capability / modules:** Supported customer release with lifecycle, support and incident processes; release catalog and operations documentation.
  - **Budget / non-goals:** B8; no advertised feature outside the qualified matrix and no GUI requirement unless that release advertises it.
  - [ ] **REL-03.1** Define product acceptance, release ownership, support lifetime, upgrade/rollback and incident/security-response procedures.
  - [ ] **REL-03.2** Complete qualification of every advertised host/device/flow/IP/programmer/debug profile, including offline and clean-machine tests.
  - [ ] **REL-03.3** Publish honest language/constraint/timing/power support, reproducible examples, errata and hardware recovery guidance.
  - [ ] **REL-03.4** Review all licenses/notices and any optional entitlement mechanism; preserve error/report visibility and documented offline behavior without bypassing rights.
  - [ ] **REL-03.5** Exercise a customer support reproduction, corruption/update failure and old-project migration on final candidate artifacts.
  - [ ] **REL-03.6** Obtain release acceptance with immutable evidence and B8 results; mark commercial readiness only for the explicitly qualified product profile.

- [ ] **REL-04 — Mid-range and team deployment qualification**
  - **Depends on:** FND-10, REL-03, FLOW-04, SEC-03.
  - **Capability / modules:** Supported team-scale builds and artifact sharing; deployment profiles, remote-provider and tenant policies.
  - **Budget / non-goals:** B6/B8; no mandatory cloud or claim that shared infrastructure grants access to proprietary IP.
  - [ ] **REL-04.1** Qualify supported multi-project/concurrent-job workloads and mid-range devices with actual engine/tool/model versions.
  - [ ] **REL-04.2** Test authenticated remote workers/shared cache, tenant boundaries, artifact retention and license-seat scheduling on deployment profiles.
  - [ ] **REL-04.3** Define operational backup/recovery, worker rollout, capability compatibility and audit policies with local/offline fallbacks.
  - [ ] **REL-04.4** Publish measured build/cache/network costs and seed/QoR distributions instead of extrapolating small-device results.
  - [ ] **REL-04.5** Run cross-version project migration, worker loss, cache corruption and permission-revocation acceptance tests.
  - [ ] **REL-04.6** Demonstrate an independently reproducible team deployment and attach B6/B8/security/support evidence for each advertised profile.

- [ ] **REL-05 — High-end professional product qualification**
  - **Depends on:** FND-10, REL-04, VER-06, FLOW-05, UX-04, HW-04.
  - **Capability / modules:** Qualified advanced-device workflows and professional operations; high-end release/evidence profiles.
  - **Budget / non-goals:** B8; no assumed high-end silicon availability, automatic signoff or blanket parity with other vendors.
  - [ ] **REL-05.1** Define the exact advanced profile: qualified hierarchical/multi-die/reconfiguration capabilities, devices, clocks, models and UI/hardware operations.
  - [ ] **REL-05.2** Require cross-region timing/configuration legality, full-versus-incremental validation and large-workload evidence from the owning engines.
  - [ ] **REL-05.3** Complete security, distribution, supportability, production/lab safety and long-term schema/device compatibility qualification.
  - [ ] **REL-05.4** Correlate advertised silicon-dependent claims with applicable target measurements and named characterization/signoff sources.
  - [ ] **REL-05.5** Exercise disaster recovery, revoked packages/keys, cross-version replay and high-load regressions on frozen candidate artifacts.
  - [ ] **REL-05.6** Publish the complete qualification matrix, B8 results and remaining exclusions; close only the supported high-end profile, not an unbounded future promise.
