# SEC — Security, trust and privacy track

Hard gate: FND-10. Foundation already establishes basic trust boundaries. This track hardens them before distribution, hardware writes or multi-user operation. Use existing reviewed cryptography/update components; [TUF](../../research-sources.md#s10) and [Tauri capabilities](../../research-sources.md#s09) are precedents, not complete product security proofs.

- [ ] **SEC-01 — Hardened local execution and privacy policy**
  - **Depends on:** FND-10.
  - **Capability / modules:** Run qualified local tools with explicit trust and inspectable data handling; policy, package and execution layers.
  - **Budget / non-goals:** B0/B2/B3; no remote untrusted execution or implied sandbox when the host cannot enforce it.
  - [ ] **SEC-01.1** Expand the threat model into executable allow/deny policies for projects, generators, tool adapters, archives and hardware effects.
  - [ ] **SEC-01.2** Implement supported OS isolation controls and capability reporting; disable unsafe profiles rather than silently weakening required isolation.
  - [ ] **SEC-01.3** Enforce path/archive/message limits and handle environment/credential separation without leaking secrets through logs or command export.
  - [ ] **SEC-01.4** Keep telemetry off by default and require scoped consent for uploads; provide local support-bundle inspection/redaction and retention controls.
  - [ ] **SEC-01.5** Test malicious packages/projects, output floods, shell injection, symlinks, privilege assumptions and sensitive-data leakage.
  - [ ] **SEC-01.6** Demonstrate denied unsafe actions and qualified local execution with documented residual risk; record B0/B2/B3 and security-review evidence.

- [ ] **SEC-02 — Signed packages, updates and offline trust**
  - **Depends on:** FND-10, SEC-01, REL-01.
  - **Capability / modules:** Verify/release/update exact tool/device/IP packages; trust metadata, update client and offline bundle contracts.
  - **Budget / non-goals:** B0/B3/B8; no custom cryptography, silent downgrade or active-build tool replacement.
  - [ ] **SEC-02.1** Select a maintained signing/update implementation after review and define trusted roles, thresholds, key custody and rotation responsibilities.
  - [ ] **SEC-02.2** Verify package digests, signatures, metadata freshness and compatibility before extraction/activation; install immutable side-by-side versions.
  - [ ] **SEC-02.3** Define explicit offline trust/freshness and legacy-replay exception policy; separate user-authorized replay from an undetected rollback attack.
  - [ ] **SEC-02.4** Implement atomic update/rollback-to-approved-version behavior and prevent changes to toolchains locked by active runs.
  - [ ] **SEC-02.5** Test wrong/revoked keys, expiry, freeze/rollback, compromised mirror, partial download, interrupted installation and key rotation.
  - [ ] **SEC-02.6** Demonstrate signed online/offline installation and rejection cases; record B3/B8, recovery and external review evidence.

- [ ] **SEC-03 — Team isolation, shared-cache trust and entitlements**
  - **Depends on:** FND-10, SEC-02, FLOW-03.
  - **Capability / modules:** Enforce per-user/project/tenant access; identity, authorization, artifact and entitlement policy contracts.
  - **Budget / non-goals:** B0/B3/B6; no account requirement for local offline use and no bypass of third-party licensing.
  - [ ] **SEC-03.1** Define authenticated identities, authorization scopes and trust namespaces for artifacts, cache publication, IP and optional services.
  - [ ] **SEC-03.2** Prevent cross-tenant deduplication/existence queries from leaking private design information; verify cache writer/result provenance.
  - [ ] **SEC-03.3** Implement least-privilege service/hardware roles and license-seat allocation where applicable, with explicit offline/expiry behavior.
  - [ ] **SEC-03.4** Keep secrets outside cache keys, public logs and support bundles while including non-secret output-affecting capability identity.
  - [ ] **SEC-03.5** Test permission revocation, tenant crossover, cache poisoning, stale credentials and concurrent entitlement requests with independent expected outcomes.
  - [ ] **SEC-03.6** Demonstrate isolated team workflows and recorded residual risks; attach B0/B3/B6 and authorization/security evidence.

- [ ] **SEC-04 — Professional service, debug and incident hardening**
  - **Depends on:** FND-10, SEC-03, FLOW-04, DBG-03.
  - **Capability / modules:** Harden advanced remote/hardware/debug services; audit, incident, credential-rotation and retention interfaces.
  - **Budget / non-goals:** B3/B5/B8; no claim of tamper-proof audit or protection beyond the documented threat model.
  - [ ] **SEC-04.1** Review remote execution and debug capture attack surfaces, data classification, privilege separation and network/service exposure.
  - [ ] **SEC-04.2** Enforce scoped local/remote IPC, authenticated leases and sensitive-capture access with bounded sessions and revocation.
  - [ ] **SEC-04.3** Implement auditable update, program, export and administrative actions with privacy-preserving retention and deletion policy.
  - [ ] **SEC-04.4** Rehearse vulnerability triage, compromised-key/package response, worker quarantine and customer notification/recovery procedures.
  - [ ] **SEC-04.5** Run independent security assessment and fuzz/fault tests against supported profiles, including malicious UI/report content and stale capture access.
  - [ ] **SEC-04.6** Close critical findings and record B3/B5/B8 plus residual-risk acceptance for the exact candidate profile.
