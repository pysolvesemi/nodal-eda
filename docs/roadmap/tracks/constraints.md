# CON — Constraints, timing and analysis track

Hard gate: FND-10. Engines calculate legality/timing; Nodal-EDA owns intent capture, delivery, completeness checks and presentation. Missing analysis must not become a passing timing result. Follow [verification](../../verification.md) and [budgets](../../performance.md).

- [ ] **CON-01 — Typed constraints and strict supported subset**
  - **Depends on:** FND-10.
  - **Capability / modules:** Validate clocks/pins/basic timing before a build; `eda-constraints`, ConstraintBundle and coverage schema.
  - **Budget / non-goals:** B0/B1; no full SDC/Tcl promise, proprietary vendor-constraint clone or silent unsupported commands.
  - [ ] **CON-01.1** Define canonical clock, pin/IO-standard and basic input/output timing intent with explicit units, scope and source locations.
  - [ ] **CON-01.2** Specify stable design-object references and deterministic wildcard/collection matching; diagnose zero, ambiguous and stale matches.
  - [ ] **CON-01.3** Implement strict parser/export interfaces and per-backend capability classification for accepted, rejected, unmatched and unsupported intent.
  - [ ] **CON-01.4** Keep any SDC/Tcl compatibility subset explicit; treat evaluated scripts as executable inputs under the trust policy.
  - [ ] **CON-01.5** Test units, escaped identifiers, hierarchy changes, clock period errors, conflicting pins and ignored/unknown constraints.
  - [ ] **CON-01.6** Demonstrate complete constraint accounting on independent fixtures; record B0/B1 and negative-test evidence.

- [ ] **CON-02 — Structured reports and truthful build acceptance**
  - **Depends on:** FND-10, CON-01, TOOL-02, FLOW-02.
  - **Capability / modules:** Timing/utilization/constraint reports in CLI and JSON; `eda-reports`, ReportEnvelope and completion verdicts.
  - **Budget / non-goals:** B4; no new STA engine or unconditional Fmax number for incomplete analysis.
  - [ ] **CON-02.1** Import engine utilization, timing, clock and constraint-coverage results with exact device/tool/model identity and raw evidence links.
  - [ ] **CON-02.2** Separate tool completion, functional verification, timing completeness and timing pass/fail; make unknown/unanalysed states visible.
  - [ ] **CON-02.3** Block timing-closed status on missing required clocks, unsupported checks, ignored exceptions, absent hold coverage or unknown corner policy.
  - [ ] **CON-02.4** Provide paged report queries, stable diagnostic IDs and source navigation handles without flattening large implementation graphs.
  - [ ] **CON-02.5** Compare normalized reports with direct-tool output and hand-reviewed fixtures, including deliberate sign/unit/clock omissions.
  - [ ] **CON-02.6** Demonstrate actual positive and negative timing-completeness cases; record B4 and report-fidelity evidence.

- [ ] **CON-03 — Multiple clocks, corners and commercial timing evidence**
  - **Depends on:** FND-10, CON-02, TOOL-05.
  - **Capability / modules:** Qualified timing scenarios and exception audit; extended ConstraintBundle/TimingScenario/report contracts.
  - **Budget / non-goals:** B4/B6; no blanket signoff claim or treating different STA models as interchangeable.
  - [ ] **CON-03.1** Support engine-qualified generated clocks, uncertainty, setup/hold, clock relationships and per-scenario exceptions with explicit feature negotiation.
  - [ ] **CON-03.2** Bind voltage/temperature/process/speed-grade and model provenance to each timing scenario; distinguish estimates from correlated characterization.
  - [ ] **CON-03.3** Audit false/multicycle/asynchronous constraints and unconstrained endpoints; preserve per-engine semantics and unsupported coverage.
  - [ ] **CON-03.4** Aggregate multi-scenario results without hiding a failing or missing corner behind a passing summary.
  - [ ] **CON-03.5** Test small independent timing fixtures and same-model direct-engine comparisons; inject missing arcs/scenarios/clock relations.
  - [ ] **CON-03.6** Demonstrate the declared clock/corner matrix and acceptance policy on an actual supported device; attach B4/B6 and characterization limits.

- [ ] **CON-04 — Power, activity and QoR reporting**
  - **Depends on:** FND-10, CON-02.
  - **Capability / modules:** Honest power/QoR comparison dashboards; `eda-reports`, activity/model/provenance schemas.
  - **Budget / non-goals:** B3/B4; no transistor-level power engine or power-signoff claim without qualified models.
  - [ ] **CON-04.1** Import engine power estimates with voltage/corner, activity source, coverage and assumptions; retain unavailable as unavailable.
  - [ ] **CON-04.2** Stream/index supported activity artifacts and flag missing/defaulted activity rather than disguising estimates as measured power.
  - [ ] **CON-04.3** Define normalized utilization, timing, congestion, runtime and power comparison records with device/model compatibility checks.
  - [ ] **CON-04.4** Require controlled seeds/options/workloads and multi-run distributions for QoR comparisons; separate semantic correctness from optimization quality.
  - [ ] **CON-04.5** Test changed units, stale activity, different architectures/models and invalid comparisons; reject misleading like-for-unlike charts.
  - [ ] **CON-04.6** Demonstrate a qualified estimate or explicitly unavailable result plus direct-reference fidelity; attach B3/B4 and uncertainty evidence.

- [ ] **CON-05 — Advanced region, IO, clock and reconfiguration planning**
  - **Depends on:** FND-10, CON-03, TOOL-05.
  - **Capability / modules:** Validate engine-supported floorplans and complex device intent; region/bank/boundary contracts and query APIs.
  - **Budget / non-goals:** B4/B6; no hard-coded rectangular-device assumption or self-invented physical legality rules.
  - [ ] **CON-05.1** Model hierarchical regions, IO banks, clock reach and dedicated-resource requirements through device capability/query contracts.
  - [ ] **CON-05.2** Preserve inter-region/inter-die constraints and boundary timing budgets where the implementation engine supports them.
  - [ ] **CON-05.3** Represent partial-reconfiguration/static interfaces and permitted configuration sets only with an explicit engine/device legality contract.
  - [ ] **CON-05.4** Provide dry-run legality reports and bounded spatial queries shared by CLI and later GUI planners.
  - [ ] **CON-05.5** Test incompatible IO voltages, unreachable clocks, illegal region overlap, stale boundary models and unsupported advanced features.
  - [ ] **CON-05.6** Demonstrate actual supported advanced constraints and precise rejection elsewhere; record B4/B6, direct-engine fidelity and limits.
