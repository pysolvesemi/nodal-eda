# Verification and qualification strategy

## What this project must prove

Nodal-EDA must faithfully translate user intent into engine actions, preserve constraints and provenance, never reuse an invalid artifact, and never label a failed/unknown result successful. It must also program only the intended authorized target and present accurate evidence. It does not independently prove a manufactured FPGA or an arbitrary user circuit correct.

The verification track has its own fixtures, independent oracles and qualification evidence. Foundation supplies bootstrap tests before that track is unblocked. The same parser/translator must not generate both the implementation result and the sole expected result.

## Valid comparisons and their limits

| Subject | Suitable reference | Compare | Do not claim |
| --- | --- | --- | --- |
| Flow orchestration | Hand-reviewed direct scripts invoking the exact qualified Yosys/nextpnr/packer tuple. | Effective inputs/flags/constraints; artifact semantics; selected exact bytes under a proven deterministic profile; success/failure and reports. | Independence of synthesis algorithms when both paths invoke the same synthesizer. |
| HDL export or generated wrappers | Source reference, independent simulation where available, EQY and SBY for supported formal models. | Functional/sequential properties under explicit reset, initialization, X, memory and clock assumptions. | A timeout, bounded result or unsupported construct proves arbitrary equivalence. |
| Own-fabric integration | Configured fabric simulation/emulation supplied by nodal-fpga; optional qualified FABulous reference. | Same user behavior with explicit timing/latency/initialization contract; DB/config/RTL agreement evidence. | Byte-identical bitstreams, PPA or physical equivalence across different architectures. |
| Timing reports | Direct backend reports and hand-calculated small timing fixtures; a separately qualified STA implementation only when models are genuinely equivalent. | Units, clocks/corners, setup/hold coverage, exception meaning and path completeness. | STA engines with different routing/clock models must have identical slack or one validates silicon. |
| Configuration | Independent feature decoder/reference vectors and actual fabric loader simulation. | Intended logical features, addressing, target identity, reserved-bit policy and corruption rejection. | encode/decode round-trip alone proves correctness if both share the same erroneous mapping. |
| Programming | A qualified programmer such as openFPGALoader on explicitly supported devices, plus lab readback and functional tests. | Target selection, transaction behavior, permitted readback, post-program function and recovery. | Readback is universally available, or checksum/transport success proves user logic correctness. |
| Build/cache/state | Independently generated small DAGs and expected state transitions. | Replay, invalidation, dependency closure, atomic publication, crash and cancellation invariants. | All external tools are bitwise deterministic across hosts or versions. |

Yosys/nextpnr provide suitable engine integration references [S02](research-sources.md#s02), [S03](research-sources.md#s03). EQY is a hardware equivalence driver; SBY handles hardware property-verification flows, not Rust program verification [S04](research-sources.md#s04), [S05](research-sources.md#s05). FABulous documents loading a user-design bitstream into generated fabric RTL; that is useful precedent, not a universal commercial-signoff oracle [S06](research-sources.md#s06). Programmer support must be checked per device [S11](research-sources.md#s11).

## Verification layers

**Contract and negative testing.** Exercise version negotiation, required fields, stable IDs, units, malformed/oversized data, missing capability, wrong package, source path traversal, duplicate outputs, unsupported constraints and ambiguous hierarchy references. Use immutable golden fixtures reviewed separately from production adapters.

**State-machine and property testing.** Generate acyclic and intentionally invalid task graphs, failures at every transition, concurrent cancellation, lost child processes, write races and randomized cache dependencies. Invariants include one terminal result per attempt, no success before verified publication, no cancelled task becoming a cache hit and no unsafe automatic hardware retry.

**Differential flow testing.** For each qualified tool/device tuple, maintain direct invocation and product invocation fixtures. Record seed, threads, executable/runtime digests, source order, defines, libraries, constraints, part and timing database. Compare canonical structures and behavior; allow byte comparisons only for an explicitly tested determinism profile. A normalizer cannot discard constraints or semantic differences merely to make a diff pass.

**Formal and simulation integration.** Use EQY/SBY on the hardware artifacts the product generates or transforms, with separate simulation on suitable fixtures. Record assumptions, solver version, proof mode and result. Unbounded proof, bounded pass, unknown, failure and tool error are distinct. Check reset/initial-state relations rather than assuming arbitrary register states align. Debug insertion must preserve defined functional behavior; source-debug metadata itself needs separate mapping tests.

**Configuration and fabric evidence.** A toy feature model with an independent decoder catches bit order, address, mode and ownership faults. Own-fabric tests must load the actual bitstream through the real configuration path and compare defined behavior. The fabric owner supplies primitive/configuration/compositional verification. Fabric topology may legally contain routing cycles and configuration fields may share bits by design; validate supported active configurations and declared sharing rather than banning all cycles or overlaps.

**Coverage and mutation.** Track requirements, constraint dispositions, parser/schema versions, error classes, cancellation points, device modes and tool capabilities. Inject wrong pins, missing exceptions, swapped fields, stale hashes, failing solvers and successful exit codes without outputs. Require all specified seeded defect classes to be detected. Routing-resource coverage belongs to nodal-fpga evidence; 100% individual resource coverage does not prove all resource combinations or all timing behavior.

**Physical and hardware correlation.** Reuse known-answer designs in RTL simulation, qualified gate-level simulation, FPGA emulation and target silicon. Tag each observation with board/chip revision, device package, bitstream digest, instruments, voltage/temperature and environment. Emulation does not measure ASIC timing, analog jitter, ESD, reliability or manufacturing yield. The EDA product links signoff/characterization reports; it does not substitute for them. OpenROAD is an ASIC physical-design tool, not a drop-in FPGA router [S12](research-sources.md#s12).

## Fault-injection inventory

Crash before/after every artifact/index commit; full disk; truncated output; killed grandchild; malformed UTF-8; extremely long diagnostics; symlink escape; archive traversal; decompression bomb; stale device revision; corrupted package signature; wrong key; expired metadata; network partition; disconnected cable; duplicate JTAG IDs; readback denied; power loss during flash write; worker loss; cache poisoning; tenant crossover; clock/constraint removal; stale debug-to-bitstream mapping.

The expected result is explicit failure or a documented recoverable state, never false success. Hardware fault tests run on approved recoverable boards with a recovery plan and no irreversible operation by default.

## Test lanes

| Lane | Required content | Boundary |
| --- | --- | --- |
| Local/PR | Rust unit/property tests, contracts, roadmap/link checks, fake tools, small real-tool differential fixture where available, parser security and deterministic artifact tests. | No secrets or physical boards for untrusted contributions. |
| Scheduled | Expanded random seeds, mutation, fuzzing, crash recovery, cross-version and scale suites, supported formal/simulation fixtures. | Persist seeds, failures and environment identities. |
| Hardware lab | Device-locked program/readback/function/recovery and capture suites. | Authenticated leases, authorization, board power limits and recovery capability. |
| Release | Exact final-head/tool/package/OS support matrix, clean/offline install, compatibility, security, performance, documentation and support replay. | No missing applicable result may silently count as pass. |
| Device/tapeout evidence | Fabric owner verification, relevant physical signoff and characterization records, silicon known-answer results. | Requires owning team approval; product CI is not foundry signoff. |

## Commercial gate

A release candidate is blocked by an unexplained functional mismatch, ignored required constraint, invalid cache hit, unresolved critical trust issue, wrong-target programming risk, or missing qualification for an advertised feature. Every exception is named, scoped, approved and visible in the support matrix. Numerical QoR differences require baseline/seed analysis; correctness failures are not tolerated as QoR variation.

Evidence includes commit/tree, commands, exact dependency digests, feature/profile, host, independent expected result, actual result, logs, proof assumptions and workload. Retain minimal reproductions and approved customer regressions without committing customer IP. The final evidence matrix is immutable per release and can distinguish software validation, fabric verification and silicon qualification.
