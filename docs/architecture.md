# Nodal-EDA architecture and directory plan

## 1. Product boundary

Nodal-EDA is a workflow, integration, analysis-presentation, and hardware-session product. The commercial precedent is a suite that connects design entry, synthesis, implementation, IP and debugging, not merely a language compiler; GOWIN documents that broader scope [S01](research-sources.md#s01).

| Owner | Authoritative responsibilities | Nodal-EDA consumes |
| --- | --- | --- |
| nodal-hdl | Nodal elaboration/lowering; existing MLIR pipeline; supported HDL/netlist export; compiler source provenance. | Files and versioned metadata through an adapter, never live MLIR objects. |
| nodal-fpga | Architecture and fabric generation; DeviceDB; resource legality; target mapping contracts; implementation engines or adapters; device timing/configuration semantics. | Qualified device packages, commands/APIs, reports, logical feature maps and bitstream artifacts. |
| External synthesis/P&R/programming tools | Their supported operations and device models. | Version-pinned adapters and capability-tested results. |
| nodal-eda | Project/build model, stage scheduling, constraints delivery, result validation, artifact store, reports, packages, hardware sessions, debug experience and UI. | This repository owns the product-level contracts and conformance tests. |
| Analog/ASIC implementation flow | Macro creation, physical implementation and signoff. | Traceable evidence manifests and macro/package identities, not an assertion of silicon signoff. |

Technology mapping must have one declared owner in each flow. Initial Nodal support can be Nodal -> Verilog -> Yosys -> implementation; direct mapped-netlist export is a separate capability. Do not run a second mapper over already mapped cells or assume today's nodal-hdl exports an unverified format. Yosys/nextpnr are reusable engines, not architectural schemas [S02](research-sources.md#s02), [S03](research-sources.md#s03).

## 2. Process and dependency architecture

```text
CLI now             optional desktop later          automation clients
   \                       |                            /
                 application service API
                           |
          project / flow planner / durable run state
                           |
        artifact store + capability/trust registry
                           |
                    adapter boundary
            +--------------+----------------+
            |              |                |
        nodal-hdl       nodal-fpga      qualified tools
        Scala/MLIR         Rust        Yosys/nextpnr/etc.
```

Use a modular Rust application first. Call small, trusted, same-workspace pure libraries directly. Run expensive or crash-prone external tools as supervised subprocesses with explicit arguments, working directory, environment, limits, artifact paths and cancellation. An ABI-stable native plugin ecosystem is not an MVP requirement. Do not expose Rust's internal ABI as a public plugin contract.

The adapter protocol starts as versioned requests/results and a bounded event stream over stdio. Large netlists, waveforms, device views and logs travel as artifact references, not giant JSON messages. A local service is introduced only for persistent hardware sessions, GUI reconnection or multiple clients. Use authenticated user-local sockets/named pipes and per-project locking; it remains optional for ordinary builds. Remote workers are later execution backends, not a rewrite of the planner. Use proven remote execution/cache protocols when useful rather than inventing a cluster product [S07](research-sources.md#s07).

A subprocess is a fault boundary, **not automatically a security sandbox**. Unsupported isolation must be reported. Hosted/untrusted execution remains disabled until the sandbox and tenant-isolation gates pass.

## 3. Directory plan

Create directories when the first owning increment implements them. This is a target layout, not a request to add empty crates or placeholder product code.

```text
nodal-eda/
  AGENTS.md
  Cargo.toml                    # introduced by FND-01
  Cargo.lock                    # application dependency lock
  rust-toolchain.toml
  crates/
    eda-contracts/              # versioned envelopes, IDs, diagnostics
    eda-project/                # project, source closure, lock and migration
    eda-flow/                   # DAG planning, run state, resource scheduling
    eda-exec/                   # subprocesses, cancellation, execution providers
    eda-artifacts/              # CAS, leases, integrity, garbage collection
    eda-adapters/               # interface plus capability registry
    eda-constraints/            # typed constraints, coverage and source mappings
    eda-reports/                # bounded queries and evidence presentation
    eda-packages/               # devices, toolchains, IP catalog and trust
    eda-hardware/               # leases, safe programming, lab protocols
    eda-debug/                  # source provenance, captures, trace indexes
    eda-service/                # shared application API; daemon only later
  adapters/
    yosys/
    nextpnr/
    nodal-hdl/
    nodal-fpga/
    fabulous-reference/
    openfpgaloader/
  apps/
    cli/
    studio/                    # optional Tauri shell, not a core dependency
  ui/
    src/                       # TypeScript; no authoritative CAD algorithms
    viewers/                   # paged tables, device tiles, waveform windows
  schemas/
    project/v1/
    adapter/v1/
    artifacts/v1/
    constraints/v1/
    reports/v1/
    packages/v1/
    hardware/v1/
    debug/v1/
  tests/
    contracts/
    fixtures/
    oracles/                   # separate from production parsing/translation
    differential/
    formal/
    fault-injection/
    compatibility/
    hardware/                  # opt-in; no boards on ordinary PR runners
  benchmarks/
    manifests/
    generators/
    baselines/
  tools/                       # maintenance/lint tooling, not product state
  docs/
    roadmap/tracks/
    evidence/                  # introduced as work completes
    adr/
    compatibility/
    operations/
  packaging/
  .github/workflows/            # introduced deliberately by FND-09
```

Bootstrap only the minimal contracts/project/exec/flow/artifact/CLI modules needed. Promote a module to a crate when its ownership or dependency isolation justifies that. Adapters depend on contracts, never the GUI; core never depends on a particular tool's parser. No crates named `router`, `synth`, `fabric-generator` or `spice-engine` belong here.

## 4. Stable contracts

Freeze semantics before choosing a fast encoding. Version the project format, adapter protocol, report schemas and device-package format independently. Do not serialize raw Rust structs as a long-lived ABI.

| Contract | Required content |
| --- | --- |
| ProjectManifest | Top, source language/subset, ordered files/includes/defines, target/device/package/speed grade, constraints, IP and build profiles. |
| ToolchainLock | Exact binaries/builds, runtime dependencies, plugins, compiler exporters, device/timing/config package digests and schema capabilities. |
| ActionSpec | Stage kind, immutable input references, expected outputs, argv, declared environment, seed/thread policy, CPU/RAM/license tokens, cancellation/retry class. |
| ArtifactRef | Content digest, byte length, media/schema version, producer/source identity, trust/provenance and storage locator. |
| StageResult | Completed/failed/cancelled/unknown, raw artifacts, structured diagnostics, constraints coverage, measurements and exit status. |
| RunManifest | DAG/action keys, version/host context, event sequence, terminal states, immutable outputs and evidence links. |
| ConstraintBundle | Clock/pin/timing/region intent, units, stable objects and source locations, backend support/acceptance disposition. |
| DevicePackage | Exact part/package/speed/revision, immutable database references, models, pin/bank legality, config/protocol capabilities, qualifications and notices. |
| ProvenanceMap | Many-to-many source -> compiler objects -> mapped cells/nets -> physical resources; explicit optimized-away/merged/unavailable states. |
| HardwarePlan | Board/cable/device identity, chain position, operation, region/address, artifact digest, authorization, readback/verification capability and audit result. |

Stable identities are scoped by artifact/schema digest. They are not guaranteed to survive arbitrary recompilation. Preserve display names separately. Cross-language IDs larger than JavaScript's exact integer range use strings or a defined binary representation. Integer widths, offsets, units, endianness, maximum message size and capability negotiation are explicit.

## 5. Build graph, cache and recovery

Keep the action cache separate from the content-addressed artifact store. Bazel documents this distinction and the importance of declared inputs/environment [S07](research-sources.md#s07), [S08](research-sources.md#s08).

An action key covers schema, all transitive input content, effective source ordering/parameters/constraints, adapter version, executable/runtime/device/timing-model digests, options, explicit environment, seed, thread/determinism profile and relevant platform fingerprint. Discover implicit includes before publication or conservatively invalidate; timestamps alone are not content identity.

Stage into a private work directory. Verify outputs and completion evidence, hash them, publish immutable blobs atomically, then commit the successful action result transactionally. Failed, cancelled, partial or unverified results never become cache hits. Recheck input stability before publishing. Hardware operations are non-cacheable effects and are never automatically retried after an ambiguous outcome.

Use a local transactional index/journal with a single serialized writer or equivalent proven concurrency discipline. Keep logs/artifacts outside the database as streaming blobs. Validate migrations, power-loss recovery, dangling blobs, reference leases and quota-aware garbage collection. Do not assume a local SQLite database on a network filesystem becomes a safe distributed service.

Pipeline checkpoints are immutable stage outputs. Native engine checkpoint reuse additionally requires an engine-specific compatibility identity and actual reuse support; reusing synthesis output is not the same as incremental placement/routing.

## 6. Constraints and report truthfulness

Start with a documented strict subset: clocks, pins/IO standards and basic input/output timing. Use a typed canonical bundle plus adapters; an SDC/Tcl compatibility surface is explicit, sandboxed where executed, and never claims full SDC merely by forwarding text. Classify every constraint as accepted, rejected, unmatched, unsupported, or explicitly waived with an owner.

The engine owns timing/legality calculations. Nodal-EDA preserves their assumptions and checks completeness. Missing clocks, unknown corners, unsupported holds, ignored exceptions or unanalysed paths prevent a green timing-closed result. Report estimates and silicon-correlated timing separately. Power estimates require a named model and activity source. Reports expose bounded queries rather than loading the whole physical graph.

## 7. Distribution, trust and user experience

Provide a headless CLI first and the same application API for a later desktop shell. Tauri's capability model is a candidate for limiting GUI access; it is not a guarantee that third-party native tools are isolated [S09](research-sources.md#s09). Keep rendering and GUI frameworks replaceable. Page report tables; request viewport tiles and waveform time windows; leave the complete DeviceDB and routing graph in their owning engine or query service.

Treat device/tool/IP packages as signed, immutable, side-by-side installs with explicit compatibility ranges, known-issues metadata and offline bundles. Verify content and target identity before execution. Use a mature signing/update framework and test expiry, rotation, revoked metadata and rollback/freeze threats rather than inventing cryptography [S10](research-sources.md#s10). Do not update an active build's toolchain. Legacy replay and security exceptions are visible policies, not silent downgrades.

Telemetry is off by default; no customer RTL, bitstreams, paths, waveforms, license secrets or hardware identifiers leave the machine without explicit scoped consent. Support bundles are locally inspectable and redacted. Licenses and notices are evaluated for each exact redistributed dependency/IP; subprocess separation alone does not determine legal obligations.

## 8. Proposed CLI surface

```sh
nodal-eda project check
nodal-eda toolchain inspect --locked
nodal-eda build --target board-a --locked --offline
nodal-eda run resume <run-id>
nodal-eda report timing --run <run-id> --format json
nodal-eda report constraints --run <run-id>
nodal-eda package verify <package>
nodal-eda hardware list
nodal-eda program plan --run <run-id> --target <explicit-target>
nodal-eda program apply <plan-id>
nodal-eda debug capture <session-id>
nodal-eda support export --run <run-id> --redacted
```

These are interface proposals. Commands must return stable machine-readable errors and useful human messages. A build does not program a board, erase flash or enable network access implicitly.

## 9. Evolution without overbuilding

M0/M1 use local Rust orchestration, real subprocess adapters, immutable files and one reference device. M2 adds qualified own-fabric contracts and lab sessions. M3 adds audited distribution/support and a declared support matrix. M4 adds optional authenticated shared cache/workers only after cache correctness and recovery are established. M5 adds regional/multi-die/reconfiguration workflows only when the engines supply their legality, boundary and timing contracts.

The scalability goal is bounded product-layer overhead while expensive synthesis/P&R remains in its engine. Choosing Rust does not eliminate bad algorithms, unbounded event queues, schema churn or invalid cache keys. Measure those explicitly and keep all unavailable features blocked.
