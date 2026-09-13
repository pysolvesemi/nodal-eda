# Synthesis, implementation and bitstream verification contract

## Scope and status

This is a required acceptance contract for the existing roadmap, not implemented verification or evidence of passing tools. It supplements [verification.md](verification.md), the [roadmap](roadmap/README.md) and [ADR-0001](adr/0001-rust-core-external-compiler-boundary.md). The per-track checkboxes remain the only task-state source of truth.

The initial roadmap already included independent oracles, direct-tool comparisons, formal integration, actual configuration loading and silicon correlation. This revision makes stage-by-stage semantic checking and route legality explicit, moves VER-03 ahead of Nodal-specific integration, and makes it a prerequisite of the first real-device milestone. It does not remove hardware, commercial or high-end qualification gates.

Nodal-EDA qualifies the execution and artifacts of synthesis/P&R/configuration engines; it does not become another synthesizer, router, FPGA generator or MLIR host. Nodal-HDL owns compiler exports. Nodal-FPGA or a qualified device provider owns architecture semantics, physical-resource models, configuration encoding and device-specific verification facilities. Independent checkers may be external programs or isolated test-oracle modules; they must not merely call the producing engine's success flag or reuse its transformation as their sole oracle.

## What cycle accuracy means

A bitstream is configuration data, not an executable clock trace. The required property is that the FPGA configured with the exact final image implements the reference circuit's specified observable behavior at the specified clock edges, under a declared reset, initialization and environment contract. Functional cycle equivalence and physical timing closure are different claims.

Freeze a SemanticContract before running a comparison: top-level port and physical pin correspondence; bit ordering and signedness; active clock edges and relationships; configuration completion and reset sequence; initial register/memory state; enables and stalls; memory read/write latency, collision and initialization modes; observable output sampling; and any intentionally undefined behavior. Uninitialized state needs an explicit state relation or refinement policy, not an assumption that two independently arbitrary register values match. EQY's safe-replacement/X semantics illustrate why this distinction matters [E02].

For a fixed-latency synchronous interface, compare every required output at every specified edge after the declared initialization sequence. A one-cycle shift is a failure unless the source contract explicitly allows it. Do not add arbitrary scoreboard delays, blanket X masking or output exclusions to make a mismatch disappear. An allowed retiming transformation needs a proven external state/latency relation. For asynchronous/multiple-clock interfaces use domain-specific event/transaction contracts and separately qualified CDC/RDC analysis; there is no single universal cycle index and RTL simulation does not model analog metastability.

## Artifact chain and independent checks

```text
original RTL + declared input/clock/reset contract
        |
        +---------------- independent golden behavior ----------------+
        |                                                            |
        v                                                            |
synthesis -> actual technology-mapped netlist                         |
        |            -> sequential equivalence / simulation ----------+
        v                                                            |
packing -> placed and routed design + actual route resource selection |
        |            -> independent packing/route legality checks     |
        |            -> route-aware functional reconstruction --------+
        v                                                            |
logical configuration -> FINAL binary bitstream                      |
        |                                                            |
        +-> independent decoding -> configured functional model ------+
        |                                                            |
        +-> actual loader -> programmable fabric RTL -----------------+
                                                                     |
                                 compare specified observable behavior
```

Record immutable hashes for every artifact, its producer and models. A post-route model must use actual selected routing, pin permutations and modes; simply exporting the pre-route netlist again does not check routing. A final-bitstream model must consume the produced binary, not the pre-packing ASCII/FASM/configuration data. Compare decoded features against the routed design as a separate check. A model made by instantiating the original user RTL behind a wrapper does not test the implementation.

### Synthesis

Compare original RTL with the actual mapped netlist using EQY for supported sequential equivalence and independent simulation for defined fixtures [E01]. Use separately reviewed primitive models, including carry, LUT, register and memory modes. Retain the original source reference as well as intermediate comparisons: comparing only two post-synthesis artifacts can miss a synthesis error shared by both.

Pin frontend, synthesis, cell-library, simulator and solver versions. Document shared components in the oracle chain: EQY is Yosys-based, so using Yosys synthesis and EQY alone is not complete frontend/model independence. Use independent hand-written reference behavior and a separately implemented simulator on supported cases to reduce common-mode errors. A second synthesizer is useful when it supports the same semantics/target, but structural netlist equality is neither necessary nor sufficient.

Proof assumptions require review and reachability/cover checks where applicable. Reject overconstrained or unobservable tests. A timeout, unsupported model or bounded result is not an unbounded proof. Missing primitive semantics must not be replaced by unconstrained black boxes while claiming full-circuit correctness.

### Packing, placement and routing

An independent checker must validate the actual implementation against a pinned device-resource/legality contract. Check site/BEL capacity and modes, LUT/FF shared controls, carry/cascade ordering, legal pin permutations with corresponding LUT truth-table transformations, package/IO-bank restrictions, permitted clocks, directed PIP connectivity, driver-to-sink reachability, exclusive-resource conflicts and permitted shared nets. Check active configurations, not a blanket ban on routing cycles or shared configuration bits.

Compare route-reconstructed behavior with both mapped and original circuits. Physical-resource IDs, wire paths and placement coordinates may differ between valid implementations. A valid route must implement the correct connection; an identical utilization count does not establish that. Independently review the device model or hand-authored small resource fixtures, since two checkers sharing the same wrong database can agree incorrectly.

Export enough evidence from the first adapter: cell/site/pin mapping, active routing edges, clock selections, resource constraints and device revision. When a provider cannot export an adequate checkable view, mark that verification capability unavailable and do not advertise a fully qualified flow. A checked logical connectivity view is not proof of transistor layout or all electrical properties.

### Final image and configured fabric

For a qualified iCE40 reference subset, use the following conceptual chain [E03]:

```text
Yosys -> nextpnr-ice40 -> icepack -> final.bin
                                      |
                                 iceunpack
                                      |
                              decoded-from-final.asc
                                      |
                                icebox_vlog
                                      |
                             reconstructed Verilog
                                      |
                     formal/simulation comparison to original RTL
```

Commands, supported devices, primitive modes, simulator compatibility and pin-name wrappers must be verified for the pinned tool tuple before accepting this lane. Prefer an HX1K/HX8K subset with required model coverage; do not infer support for every iCE40 primitive or derivative. IceStorm's database is shared with parts of the implementation flow, so this is a powerful end-to-end check, not a perfectly independent proof of the silicon model. Independently reviewed feature vectors and later board measurements are still required.

For a Nodal fabric, require both an independently implemented feature decoder/reference interpretation and tests that load the actual final bytes through the real simulated configuration controller. Compare the resulting fabric outputs against the golden circuit. Cover frame addressing, bit/endian order, LUT INIT, FF controls, memory initialization/modes, routing muxes, clocks, reserved fields and legal shared encodings. A successful encode/decode round trip alone can hide a shared erroneous mapping.

Keep two verification modes distinct. Preconfigured or configuration-specialized models are useful for fast functional/formal checks, but do not test the loader. Full configuration-and-operation simulation tests the loader as well. FABulous documents loading a user-design bitstream into fabric RTL [E04]; OpenFPGA explicitly separates full and preconfigured/formal-oriented testbenches [E05]. Neither project's documentation or generated testbench is itself proof that a Nodal design passed.

Own-fabric loader/reference tests are required in TOOL-05.5 before real hardware is a prerequisite. VER-04 adds the integrated configuration, emulation and hardware-path evidence after its declared dependencies. Silicon is not required to start simulation, but remains required to close silicon-dependent HW-03, VER-05 and release claims.

### Timing and physical validation

Keep functional equivalence, routing legality, timing completeness, timing result and hardware observations separate. Require declared clocks and IO delays, setup/hold coverage, exceptions, unconstrained endpoint accounting, speed/corner/model identity and dedicated-clock legality. Compare direct backend results and small independently calculated timing examples. Different STA engines can be compared numerically only after their circuit, delay, clock, corner and exception semantics are shown equivalent.

VTR documents post-implementation Verilog/SDF simulation for supported primitives [E06]. This is a useful timing-validation precedent or optional same-architecture adapter, not a universal timing oracle or replacement for a Nodal device's timing model. SDF simulation samples behavior under the exercised stimulus; it does not replace STA, CDC/RDC or physical signoff. Fast zero-delay simulation passing cannot establish the advertised maximum clock frequency.

For fabric manufacture, import owner-qualified RTL-to-gates equivalence, DRC/LVS, extraction, timing/power and other applicable signoff evidence. These are separate from mapping a user design onto an existing FPGA. FPGA-on-FPGA emulation verifies digital behavior, not the new ASIC's jitter, process margins or manufacturing reliability.

## Cross-tool policy

| Comparison | Valid purpose | Limitation |
| --- | --- | --- |
| Nodal-EDA versus reviewed direct Yosys/nextpnr/packer scripts | Input/constraint/options preservation, cache/recovery and report correctness | Same engines do not independently validate their algorithms. |
| Original RTL versus mapped netlist with EQY and separate simulation | Synthesis semantic preservation under explicit assumptions | Shared frontend/models and unsupported constructs remain visible. |
| Selected routes versus independent legality checker and reconstructed behavior | Packing, connection and mode correctness | Does not prove the physical device database or silicon by itself. |
| Final binary versus independently decoded model and actual loader simulation | Bitstream encoding, feature mapping and configured behavior | A pre-bitstream netlist or forced configuration does not test final serialization/loader. |
| Two packers on the same logical features and exact device revision | Format/feature cross-check | Byte equality only under a declared deterministic encoding; compression/header policies can differ. |
| nextpnr versus another qualified implementation backend on the same architecture | Correctness and separately reported quality of results | Do not demand identical placement, route, LUT count or Fmax; align models before numerical comparisons. |
| FABulous/OpenFPGA versus Nodal-FPGA | Same application behavior and explicitly aligned small architecture/resource contracts | Different fabrics do not have equivalent bitstream bytes or directly comparable PPA. |
| Hardware versus simulation/reference traces | Device-specific functional and timing-model correlation | A finite corpus is not proof of all configurations or operating conditions. |

Do not require multiple complete engines before the first useful increment. Start with one supported open-device flow and independent output checkers. Add a second implementation backend only when a genuinely comparable target and exporter are qualified. No vendor tool, VTR, FABulous or OpenFPGA is silently installed or made a universal dependency.

## Day-one evidence and adapter contracts

These are required acceptance details of existing children; task state remains in the track files.

| Owner | Requirement |
| --- | --- |
| FND-02.1, FND-02.5 | Versioned SemanticContract, artifact stage role, model/assumption identity and VerificationResult/EvidenceManifest references; identifiers scoped by immutable artifact. |
| FND-03.1, FND-03.4 | Capability negotiation for mapped netlist, route evidence, feature map, final-bitstream decode, simulation models and timing export; one mapping owner per flow. |
| FND-06.2, FND-06.3 | Verification action keys include checker/model/contract/solver versions and exact inputs; successful execution is not automatically verified success. |
| FND-09.1, FND-09.2, FND-10.3 | Mock mismatches, missing checkable artifacts, wrong model/hash, false-success results and nested-checklist validation before the foundation gate closes. No real engines or future VER dependency added to Foundation. |
| VER-01, VER-02 | Independent corpus/oracle provenance and exact direct-versus-orchestrated flow comparison. |
| TOOL-02, VER-03, CON-02 | Actual reference-device stage artifacts, early synthesis/route/final-bitstream semantic qualification and separate timing verdicts; required for M1. |
| TOOL-04 | Add real Nodal source/export proof and simulation using the already qualified VER-03 harness; direct mapped exports remain capability-gated. |
| TOOL-05, VER-04 | Actual own-fabric route/configuration/loader evidence, independent reference checks and integrated hardware paths. |
| VER-05, VER-06, HW-03 | Release/fleet regressions and actual silicon correlation for advertised profiles. |

A VerificationResult must identify: claim/stage; exact source and candidate hashes; device/package/configuration/model revisions; checker and solver versions; SemanticContract and assumptions; stimuli/seed or proof mode/depth; covered features and excluded behavior; status; raw evidence; counterexample/minimal reproduction; and the originating commit/tree. Keep execution, functional proof/simulation, route legality, timing and hardware outcomes as separate axes. Preserve fail, unknown, unavailable, skipped and bounded-only; do not flatten them into pass.

Build artifacts may exist before expensive qualification completes. The UI must label them accordingly; release acceptance and any verified-cache label require the relevant evidence. User-requested exploratory builds are not falsely advertised as formally verified. Never reuse a proof after the checked design, model, assumptions or checker changes without an explicit validated reuse contract.

## Corpus, mutation and scalability

Begin with counters, pipelines with enables/stalls, reset variants, signed arithmetic and overflow, muxes, carry chains, high fanout, constants and supported RAM initialization/collision modes. Include narrow/non-power-of-two dimensions and packing boundaries. Add FSMs, DSPs, multiple clocks, debug instrumentation and reconfiguration only with matching models and contracts. Use hand-written expected behavior plus bounded random generators and retained seeds; no customer/private IP enters public fixtures.

Seed defects deliberately: a wrong LUT INIT bit, an inconsistent LUT-input permutation, missing/reversed routing edge, short between unrelated nets, wrong FF enable/reset/edge, one-cycle latency shift, memory mode/address corruption, swapped bitstream field, dropped frame, stale package, ignored clock/hold constraint and false-success log. For format-preserving semantic corruption, regenerate checksums using a controlled offline fixture so the semantic checker is exercised rather than only the CRC checker. Also test malformed images rejected by the loader. Never apply these mutants to physical boards by default.

Require detection of every enumerated observable, non-equivalent seeded defect for the declared suite. Some mutations are functionally equivalent or unobservable; classify them rather than hiding survivors. MCY provides an existing mutation-testing approach for suitable synthesized hardware [E07]. A high mutation score or full individual-PIP coverage is not proof of all interactions. Record feature/mode pairs, shared configuration interactions, clock/resource boundaries, requirements and exclusions.

Small real-device checks run in the qualified integration lane once available; expanded simulation/formal/mutation runs are scheduled; hardware tests use authorized lab targets. Exact release heads repeat the advertised device/tool/OS profile. At large scale, use primitive/tile/region proofs supplied by owners, configuration-specialized models, independent connectivity scans, bounded artifact queries and cached evidence keyed to all semantic inputs. Partition assumptions and inter-region interfaces must be checked; do not claim composition from isolated local proofs alone.

Measure checker runtime, peak memory, disk and model reconstruction cost separately from engine time, retaining end-to-end totals under the existing performance profiles. A resource timeout leaves the proof unknown, not passing. Keep small mandatory smoke checks and larger qualification campaigns distinct without removing required release evidence. Do not flatten the whole physical fabric into the product process or impose one enormous monolithic formal proof as the only gate.

## Primary references

Reviewed 2026-09-13. Pin actual tool revisions during implementation; these pages establish mechanisms, not installed capabilities or completed tests.

- E01: YosysHQ, [EQY documentation](https://yosyshq.readthedocs.io/projects/eqy/en/latest/) and [getting started](https://yosyshq.readthedocs.io/projects/eqy/en/latest/quickstart.html): formal hardware equivalence, including checking synthesis changes.
- E02: YosysHQ, [Equivalence and X-Propagation](https://yosyshq.readthedocs.io/projects/eqy/en/latest/xprop.html): initial-state, undefined-value and safe-replacement semantics. [SBY documentation](https://yosyshq.readthedocs.io/projects/sby/en/latest/) describes supported property-checking flows.
- E03: Project IceStorm, [project overview and tools](https://prjicestorm.readthedocs.io/en/latest/overview.html): icepack/iceunpack and icebox_vlog bitstream-to-Verilog reconstruction. Historical examples mention Arachne-pnr; use a separately qualified current nextpnr tuple, not an assumed legacy installation.
- E04: FABulous, [Simulation setup](https://fabulous.readthedocs.io/en/latest/user_guide/simulation/simulation.html): configured-fabric simulation using a user-design bitstream; not validation of arbitrary user design intent.
- E05: OpenFPGA, [Testbench](https://openfpga.readthedocs.io/en/master/manual/fpga_verilog/testbench/) and [FPGA-Verilog commands](https://openfpga.readthedocs.io/en/latest/manual/openfpga_shell/openfpga_commands/fpga_verilog_commands/): full versus preconfigured tests and explicit reference benchmark for self-checking. A generated formal-oriented wrapper is not a completed formal proof.
- E06: VTR, [Post-Implementation Timing Simulation](https://docs.verilogtorouting.org/en/latest/tutorials/timing_simulation/) and [analysis options](https://docs.verilogtorouting.org/en/latest/vpr/command_line_usage/#analysis-options): implementation netlists, SDF and supported-primitive limitations.
- E07: YosysHQ, [Mutation Cover with Yosys](https://yosyshq.readthedocs.io/projects/mcy/en/latest/): mutation-based evaluation of self-checking hardware testbenches; not proof of complete tool correctness.
