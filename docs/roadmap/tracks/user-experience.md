# UX — CLI, application API and optional desktop track

Hard gate: FND-10. CLI is a first-class product, not a GUI fallback. A desktop shell may use Tauri and TypeScript but must not own project semantics or CAD algorithms. Validate framework and OS prerequisites before adoption; see [source S09](../../research-sources.md#s09).

- [ ] **UX-01 — Shared application API and accessible headless experience**
  - **Depends on:** FND-10, FLOW-02, CON-02.
  - **Capability / modules:** Consistent human/automation workflow; `eda-service`, CLI commands, application request/result contracts.
  - **Budget / non-goals:** B0/B4; no mandatory background daemon, GUI or JVM for non-Nodal projects.
  - [ ] **UX-01.1** Define shared project/build/report/cancel APIs independent of CLI formatting and GUI implementation.
  - [ ] **UX-01.2** Stabilize machine-readable results, exit categories, help, progress, diagnostics and noninteractive behavior.
  - [ ] **UX-01.3** Expose source/error navigation and reproducible command export while retaining exact engine evidence.
  - [ ] **UX-01.4** Support user-local configuration and accessible text output without encoding mandatory work solely in interactive prompts.
  - [ ] **UX-01.5** Test API/CLI semantic parity, pipe closure, terminal-less CI, Unicode paths and invalid/large queries.
  - [ ] **UX-01.6** Demonstrate complete headless use and B0/B4 measurements; publish stable automation examples with actual outputs.

- [ ] **UX-02 — Optional desktop shell and scalable analysis views**
  - **Depends on:** FND-10, UX-01, TOOL-05, PERF-02.
  - **Capability / modules:** Open projects and inspect builds/device/timing views; `apps/studio`, `ui`, scoped IPC/query contracts.
  - **Budget / non-goals:** B4/B7; no full DeviceDB JSON transfer, bespoke editor, or GUI-only build semantics.
  - [ ] **UX-02.1** Benchmark Tauri/TypeScript or a justified alternative for supported OS/WebView deployment, memory, packaging and accessibility.
  - [ ] **UX-02.2** Implement scoped IPC to the shared Rust service; keep untrusted reports/content from gaining arbitrary shell/file access.
  - [ ] **UX-02.3** Build virtualized report tables and viewport/level-of-detail device rendering with bounded query caches and cancellation.
  - [ ] **UX-02.4** Reuse a supported editor/viewer component where needed; preserve plain-file project portability and command-line parity.
  - [ ] **UX-02.5** Test UI reconnection, stale result selection, oversized data, malicious report markup and headless operation with no GUI installed.
  - [ ] **UX-02.6** Demonstrate large synthetic views within B4/B7 and archive framework/deployment tradeoffs plus security evidence.

- [ ] **UX-03 — Integrated pin, IP, programmer and debug workflows**
  - **Depends on:** FND-10, UX-02, HW-02, DBG-02, IP-02.
  - **Capability / modules:** Unified workflows through existing application APIs; planners/configurators and capture views.
  - **Budget / non-goals:** B4/B5/B7; GUI does not override target safety, constraints or engine legality.
  - [ ] **UX-03.1** Add pin/clock/IP configuration views that edit the same canonical project/constraint/generator model used by CLI.
  - [ ] **UX-03.2** Show build diagnostics, resource costs and timing-completeness results before applying device operations.
  - [ ] **UX-03.3** Render explicit hardware programming plans, identity, consequences and authorization; never hide an erase behind a build action.
  - [ ] **UX-03.4** Add qualified probe/trigger/capture views with exact bitstream/source identity and offline replay.
  - [ ] **UX-03.5** Test GUI/CLI parity, undo/migration, inaccessible hardware, stale debug maps and safe cancellation at every workflow step.
  - [ ] **UX-03.6** Demonstrate real end-to-end workflows and accessible error recovery; retain B4/B5/B7 and hardware-safety evidence.

- [ ] **UX-04 — High-end hierarchical analysis experience**
  - **Depends on:** FND-10, UX-03, CON-05, FLOW-05.
  - **Capability / modules:** Analyze supported large/regional/multi-die designs; hierarchical view/query and session-state contracts.
  - **Budget / non-goals:** B4/B7/B8; UI presence does not imply engine support or make a huge flat graph acceptable.
  - [ ] **UX-04.1** Navigate hierarchical regions/dies, timing scenarios, boundary constraints and approved configuration sets from engine query APIs.
  - [ ] **UX-04.2** Implement viewport streaming, cancellable search and level-of-detail aggregation without losing individual-object provenance.
  - [ ] **UX-04.3** Persist lightweight view state separately from immutable design/device data and tolerate artifact/session expiry.
  - [ ] **UX-04.4** Provide comparable multi-run/seed/corner views that expose missing data and invalid comparison conditions.
  - [ ] **UX-04.5** Stress large synthetic device/report datasets, disconnects, slow storage, accessibility and stale cross-region selections.
  - [ ] **UX-04.6** Demonstrate supported professional workflows within B4/B7/B8 and document actual device/OS feature limits.
