# PERF — Performance and scalability track

Hard gate: FND-10. All budgets come from the [performance contract](../../performance.md) and remain targets until measured. EDA overhead and engine runtime are measured separately; correctness, completeness and security never become optional for speed.

- [ ] **PERF-01 — Reproducible baseline and asymptotic scale ladder**
  - **Depends on:** FND-10.
  - **Capability / modules:** Explain product-layer time/RAM/I/O costs; `benchmarks`, profiling and structured measurement records.
  - **Budget / non-goals:** B0-B3; no unsupported claim that a language choice guarantees scale.
  - [ ] **PERF-01.1** Register deterministic S0/S1/S2 fixture generators for manifests, DAGs, events, opaque artifacts and index queries.
  - [ ] **PERF-01.2** Record host/tool/build/cache context and repeated p50/p95 plus peak parent/child RSS, CPU, I/O and queue statistics.
  - [ ] **PERF-01.3** Profile scheduler/index/parser/copy hot paths and identify unexpected quadratic growth or per-resource full-graph copying.
  - [ ] **PERF-01.4** Establish reviewed baselines and regression thresholds with noise controls; archive prior baselines instead of overwriting failures.
  - [ ] **PERF-01.5** Prove benchmark checksums/semantic results match correctness fixtures and that disabled work is not being counted as a speedup.
  - [ ] **PERF-01.6** Demonstrate repeatable B0-B3 measurements and growth curves; publish bottlenecks and any reviewed target adjustments.

- [ ] **PERF-02 — Bounded reports, artifacts and device-query APIs**
  - **Depends on:** FND-10, PERF-01, FLOW-02.
  - **Capability / modules:** Work with large artifacts/reports without UI/control-plane blowup; `eda-artifacts`, `eda-reports`, query/index contracts.
  - **Budget / non-goals:** B3/B4/B6; no whole-DeviceDB import or belief that mmap alone guarantees bounded memory.
  - [ ] **PERF-02.1** Separate small control messages from bulk artifact data and introduce checked wide offsets, streaming hashes and range access.
  - [ ] **PERF-02.2** Implement paged/indexed report and provenance queries with cancellation, backpressure and bounded caches.
  - [ ] **PERF-02.3** Use engine-owned viewport/resource query interfaces instead of expanding every physical wire/PIP in nodal-eda.
  - [ ] **PERF-02.4** Validate durable index formats, migrations and lazy loading; keep raw immutable artifacts available for reproducible rebuilds of indexes.
  - [ ] **PERF-02.5** Stress 10 GiB files, 10-million-row reports, malformed ranges, >4 GiB offsets and slow consumers with exact-result checks.
  - [ ] **PERF-02.6** Demonstrate B3/B4/B6 and stable memory growth, including cold-start/index costs reported separately from warm query latency.

- [ ] **PERF-03 — Concurrent projects and resource-aware throughput**
  - **Depends on:** FND-10, PERF-02, FLOW-03.
  - **Capability / modules:** Run multiple builds predictably; scheduler, artifact/index concurrency and usage-estimation policies.
  - **Budget / non-goals:** B1/B2/B3/B6; no global mutable bottleneck or unbounded automatic parallelism.
  - [ ] **PERF-03.1** Measure and enforce CPU/RAM/scratch/license budgets across jobs and nested tool thread counts.
  - [ ] **PERF-03.2** Optimize lock scopes, artifact deduplication and transaction batches while preserving publication and lease correctness.
  - [ ] **PERF-03.3** Implement fair admission and backpressure with visible blocked reasons; prevent large jobs from exhausting resources needed for cancellation/status.
  - [ ] **PERF-03.4** Track estimated versus measured resource use and tune scheduling conservatively without changing user constraints or tool semantics.
  - [ ] **PERF-03.5** Test eight concurrent S1 mock jobs, multi-project cancellation, disk pressure and GC races; compare all final artifacts to serial reference results.
  - [ ] **PERF-03.6** Demonstrate B1/B2/B3/B6 under load with reproducible throughput/resource plots and retained correctness evidence.

- [ ] **PERF-04 — Large regional and remote workload qualification**
  - **Depends on:** FND-10, PERF-03, FLOW-04, TOOL-05.
  - **Capability / modules:** Measured high-end control-plane scale; regional query/cache policy and remote workload manifests.
  - **Budget / non-goals:** B3/B4/B6/B8; synthetic resource counts are not silicon-capacity or engine-runtime guarantees.
  - [ ] **PERF-04.1** Exercise S3 million-action and opaque 100-million-resource query fixtures without flattening device graphs into product memory.
  - [ ] **PERF-04.2** Measure regional data locality, artifact transfer, shared-cache behavior and worker cold starts with provenance/security overhead included.
  - [ ] **PERF-04.3** Bound metadata/index growth, retention, slow-client queues and service fanout; document tested deployment limits.
  - [ ] **PERF-04.4** Compare supported real large-design workflows with direct-engine baselines and controlled seed distributions.
  - [ ] **PERF-04.5** Stress worker loss, network partitions, mass cancellation and large partial-result recovery without stale cache hits or false completion.
  - [ ] **PERF-04.6** Publish B3/B4/B6/B8 and asymptotic evidence for the declared profile; retain unsupported scale/device cases as exclusions.
