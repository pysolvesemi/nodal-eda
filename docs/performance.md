# Performance and scalability contract

## Status and measurement rules

All numbers below are **proposed engineering acceptance targets**, not achieved benchmarks or hardware-capacity claims. FND-09 must record a named reference host and pilot measurements; changing a target requires a reviewed rationale and retained history. Use release builds, stable fixtures and pinned engines. Report warm/cold cache separately, p50/p95 over repeated runs, peak parent/child RSS, CPU, I/O, event loss and cancellation behavior.

Primary initial host: a declared Linux x86-64 machine with 8 logical CPU threads, 32 GiB RAM and local SSD/NVMe; record exact CPU/OS/kernel/filesystem. Later OS profiles require their own calibration. Measure orchestration separately from external synthesis/P&R and unavoidable input hashing. No performance win may drop constraints, truncate required results, skip validation or change semantics.

## Named budget profiles

| Profile | Initial target and fixture | Applies to |
| --- | --- | --- |
| B0: CLI/contracts | Warm `--help`/`--version` p95 <= 250 ms; no external engine, GUI or JVM startup. Validate a 10 MiB control document in <= 1 s with bounded allocations on the declared host. | Contracts, project checks, capability and package metadata. |
| B1: build planning | Plan/schedule 10,000 actions with 50,000 dependency edges in <= 2 s and <= 256 MiB parent RSS, excluding source content and child processes. No O(N squared) graph pass on ordinary DAGs. | Planner, scheduler and run views. |
| B2: execution/recovery | Stream a 1 GiB synthetic tool log using <= 64 MiB incremental buffering. Acknowledge cancellation in <= 1 s; terminate owned local process trees after a documented grace period, target <= 5 s. No partial outputs promoted. | Runners, adapters, journal and recovery. |
| B3: artifacts/cache | Incremental RSS <= 128 MiB when hashing/copying a 10 GiB artifact; do not deserialize it. Cache hit invokes zero CAD tools. Report lookup time separately from integrity checks and materialization; batch metadata lookup p95 <= 250 ms for a warm 10,000-action index. | CAS, packages, checkpoints. |
| B4: reports/provenance | First 1,000-row page p95 <= 300 ms from an already indexed 10-million-row synthetic report; query memory proportional to the requested window/index, not full result size. Never send a whole DeviceDB to the UI. | Reports, source mapping, waveform and device queries. |
| B5: hardware safety | Exclusive target lease; bounded protocol chunks and explicit timeout per operation. Progress/abort request acknowledged <= 1 s where host protocol permits. Device flash/erase latency and safe abort points are measured capabilities, not universal promises. | Programmer and live debug. |
| B6: qualified flow overhead | For engine workloads >= 60 s, added orchestration work excluding declared hashing/materialization <= max(2 s, 5% of direct-flow wall time). Record all excluded costs separately. No nested-thread oversubscription beyond the declared CPU/RAM tokens. | Real flows and parallel jobs. |
| B7: desktop | Initial interaction target p95 <= 100 ms for local selection/navigation on loaded pages. Render by viewport/level-of-detail; a 10-million-resource synthetic device remains bounded by a declared tile cache. | Optional GUI; framework choice is benchmarked. |
| B8: release/lab | All claimed profiles measured on the qualified matrix; no unexplained >10% median time/RSS regression against same-host stable baselines. Correctness failures are absolute gates regardless of speed. | Final qualification. |

B2/B5 distinguish an acknowledged request from physical cancellation. Irreversible flash commands may finish before a safe boundary; report that honestly. B3 does not promise a 10 GiB integrity check in 250 ms. B6 does not include an external engine's runtime within an artificial low EDA memory limit.

## Scale ladder

S0: 100 source files, 100 actions, small reports, one target.

S1: 10,000 actions, 50,000 edges, 1 GiB logs, 10 GiB opaque artifacts and eight concurrent mock jobs. This is an orchestration workload, not 10,000 synthesis jobs per design.

S2: 100,000 actions, 500,000 edges, 10-million-row reports/provenance, concurrent projects, indexed queries and >4 GiB artifacts. Record asymptotic growth; doubling workload should not unexpectedly quadruple RAM/time.

S3: 1-million-action synthetic DAG and 100-million-resource **opaque/query-only** device fixture for high-end stress. The EDA core must not flatten or ingest the whole device graph. These tests validate product-layer scalability, not feasibility or timing of a 1-million-LUT chip.

## Architectural requirements

Bound queues, log buffers, result pages, waveforms and GUI tile caches. Use immutable artifact references and checked wide offsets. Keep resource occupancy, physical routing and STA state in the owning engine. Separate control traffic from bulk data. Use backpressure and explicit slow-consumer policy; logs may spill to disk, terminal error/status events must not disappear.

Budget jobs by CPU, estimated peak RAM, scratch disk, external license seats and hardware leases. Set tool thread counts explicitly. Persist actual versus estimated usage to improve future scheduling without automatically raising unsafe limits.

Introduce shared cache/remote workers only after local correctness, authentication, content verification and crash recovery pass. Make out-of-core query/index behavior possible without assuming that mmap alone bounds resident memory or guarantees performance.

## Benchmark evidence

Every report includes fixture generator version/seed, sizes, tool/device/source hashes, command, host, cache state, repetitions, distributions, parent/child resource use and correctness checksum. Check in fixture manifests and compact results, not giant raw traces. Store large artifacts externally with content hashes and access controls. Retain reproductions when a regression exceeds the budget.
