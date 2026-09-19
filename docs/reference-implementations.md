# Open-source implementation references and adoption plan

Review date: 2026-09-19. These primary-source links identify study targets and integration candidates, not qualified Nodal implementations or a promise of feature parity. No upstream source code, device database or hardware IP is imported by this documentation update. Existing source IDs in [research-sources.md](research-sources.md) remain stable.

## Ownership and selection rules

Preserve [the architecture boundary](architecture.md) and [ADR-0001](adr/0001-rust-core-external-compiler-boundary.md). Nodal-EDA is the Rust-first product/orchestration layer. Compiler lowering and source identities belong to nodal-hdl; fabric, mapping, device legality, timing and implementation engines/adapters belong to nodal-fpga or qualified external providers. ASIC fabric implementation is a separate flow, not FPGA user-design P&R.

A reference can be a study-only precedent, an externally invoked tool, a redistributed dependency, a library, hardware IP, or an independent checker. Record that choice explicitly. Studying an algorithm does not authorize copying its implementation; selecting one candidate does not require adopting all the projects below. Do not port an entire C++/Python framework to Rust merely to match the product language.

## Engine and device references

| ID / primary source | Component or idea to inspect | Recommended use and owner | Owning roadmap work / acceptance |
| --- | --- | --- | --- |
| REF-01: [Yosys](https://github.com/YosysHQ/yosys), [ABC](https://github.com/berkeley-abc/abc) | Synthesis pass boundaries, technology libraries, Boolean optimization and technology mapping. | External synthesis first; algorithm studies stay with the compiler/FPGA engine owner. | TOOL-02.1/.2; VER-03.2. Pin the actual ABC build and mapping script selected by Yosys, not merely the top-level executable. Check original-to-mapped semantics. |
| REF-02: [nextpnr](https://github.com/YosysHQ/nextpnr), [architecture API](https://github.com/YosysHQ/nextpnr/blob/main/docs/archapi.md) | Common pack/place/route infrastructure versus architecture-specific resources, legality, clocks and timing. | Primary practical P&R adapter and nodal-fpga engine-contract reference. | TOOL-02.2/.5, TOOL-05.1; VER-03.3. Inspect the packer, selected routes and actual architecture database; do not infer universal device support. |
| REF-03: [VTR / VPR](https://github.com/verilog-to-routing/vtr-verilog-to-routing) | Architecture-driven packing, placement, routing, routing-resource models and benchmark methodology. | Algorithm/reference-flow study for nodal-fpga; optional qualified comparison provider for nodal-eda. | TOOL-05.1, VER-03.3/.5, VER-04.4. Compare semantics/legality on compatible architecture subsets; QoR is a separate measured result. |
| REF-04: [Tatum](https://github.com/verilog-to-routing/tatum) | Timing graphs and static timing-analysis interfaces. | Timing-engine reference for nodal-fpga/external providers; result-contract study for nodal-eda. | CON-02/CON-03 and TOOL-05.1. Require qualified clock, exception, setup/hold and model coverage; do not add a duplicate STA engine to the product core. |
| REF-05: [Apicula](https://github.com/YosysHQ/apicula) | Gowin device/configuration documentation, packing/unpacking and reference board flows. | Optional Gowin-device adapter, separate from own-fabric development and the first iCE40 lane. | TOOL-06. Pin part/package/family/database and qualify exported semantics; vendor-tool support and proprietary GAO compatibility are not implied. |
| REF-06: [FABulous](https://github.com/FPGA-Research/FABulous), [OpenFPGA](https://github.com/lnis-uofu/OpenFPGA) | Fabric generation, architecture/configuration coupling, generated models and configured-fabric tests. | nodal-fpga architecture studies; optional external reference flows. | TOOL-03, TOOL-05, VER-04. Preserve real loader tests and original-design golden behavior. Different fabrics need not produce identical bitstreams or PPA. |
| REF-07: [FPGA Interchange](https://github.com/chipsalliance/fpga-interchange-schema), [FASM](https://github.com/chipsalliance/fasm) | Device, logical/physical netlist interchange and logical configuration-feature representation. | Contract/interoperability study across nodal-fpga and nodal-eda, not mandatory schemas. | FND-02/FND-03, TOOL-01.2, TOOL-05.1. Document lossless subset, identities, unsupported fields and round-trip limits before adoption. FASM is not a final binary or independent proof. |
| REF-08: [OpenPARF](https://github.com/PKU-IDEA/OpenPARF) | Parallel/GPU-oriented placement and routing framework for heterogeneous FPGAs. | Deferred algorithm/performance study for the implementation-engine owner. | PERF-03/PERF-04 and upstream engine work. Require comparable device, legal outputs, hardware/runtime costs and reproducible workloads; do not add GPU dependencies to the product baseline. |
| REF-09: [OpenROAD](https://github.com/The-OpenROAD-Project/OpenROAD) | ASIC physical-design workflow and evidence organization. | Secondary reference for the separate ASIC/fabric physical flow. | TOOL-05.4/VER-04 evidence imports only. It is not a replacement for FPGA resource-based placement/routing. |

The preferred initial synthesis/implementation lane remains the qualified Yosys/nextpnr/IceStorm iCE40 subset in TOOL-02/VER-03. Apicula currently documents Yosys `synth_gowin`, nextpnr's Himbaechel Gowin backend, `gowin_pack` and openFPGALoader. Treat executable names, family options and database formats as version-specific capabilities. TOOL-06 must verify the selected installation rather than hard-code a historical `nextpnr-gowin` assumption.

## Product and workflow references

| ID / primary source | Component or idea to inspect | Recommended use and owner | Owning roadmap work / acceptance |
| --- | --- | --- | --- |
| REF-10: [FOEDAG](https://github.com/os-fpga/FOEDAG), [Raptor](https://github.com/os-fpga/Raptor) | EDA project/task GUI, RTL-to-bitstream integration, IP/programmer workflows and Raptor's OCLA debugger commands. | Product/workflow and interaction reference for nodal-eda. | FLOW-02, UX-01..UX-03, HW-01/HW-02, DBG-02. Study project state and debug sessions; do not replace the Rust/headless architecture or assume their device/IP support is portable. |
| REF-11: [Edalize](https://github.com/olofk/edalize) | Backend abstraction, flow configuration and external-tool invocation. | Adapter/workflow study; integration only after an explicit dependency decision. | FND-03, FLOW-02, TOOL-01/TOOL-02. Verify ordering, paths, options, errors and locked tool identity against direct scripts. |
| REF-12: [FuseSoC](https://github.com/olofk/fusesoc) | IP package descriptions, dependencies, parameters, generators and build targets. | IP/package model study, not a second mandatory project format. | IP-01/IP-02 and FND-04. Check source closure, deterministic generation, license metadata and unsupported-language rejection. |
| REF-13: [openFPGALoader](https://github.com/trabucayre/openFPGALoader) | Cable/board/device programming adapters and recovery behavior. | Candidate external programming provider for nodal-eda. | HW-01/HW-02. A working programmer does not establish a user-debug endpoint or proprietary analyzer-protocol support. |

## Soft logic analyzer and waveform references

The target is a vendor-style internal-signal debug experience, not a claim to clone Gowin GAO's protocol. Capture hardware, communication transport, host controller and waveform reader/viewer are separate qualification units. A waveform viewer alone is not an embedded analyzer.

| ID / primary source | What to inspect | Initial decision / owning tasks | Specific qualification limit |
| --- | --- | --- | --- |
| REF-14: [LiteScope](https://github.com/enjoy-digital/litescope) | Configurable triggers, BRAM capture, generated Verilog, host driver and waveform exports. | First analyzer candidate to evaluate for IP-02 and DBG-02; pin its generator and any LiteX/Migen/bridge dependencies. | Upstream documents BSD-2-Clause. Qualify a single-clock, uncompressed, bounded-depth subset first. UART/Ethernet/PCIe bridges have separate dependencies; availability is not Nodal qualification. |
| REF-15: [Manta](https://fischermoseley.github.io/manta/latest/), [source](https://github.com/fischermoseley/manta) | Separation of analyzer/IO/memory cores from UART/Ethernet interfaces and host API; conventional Verilog export. | API/core/transport study for IP-02, HW-01 and DBG-02; alternative integration only after review. | Upstream documents GPLv3. Register/memory writes and virtual stimulus are not passive capture and need separately scoped authorization and qualification. |
| REF-16: [ZipCPU wbscope](https://github.com/ZipCPU/wbscope) | Small capture engine, circular-buffer ordering, trigger holdoff, rearming and bus readout. | RTL/verification reference for DBG-02.1/.5; possible alternative IP package after selection. | Upstream documents GPLv3 and alternative commercial licensing. Shared RTL/algorithms are not independent test oracles; the project alone is not a complete IDE debug system. |
| REF-17: [Raptor OCLA debugger](https://github.com/os-fpga/Raptor) | Probe metadata loading, clock-domain selection, trigger setup, capture status and waveform output. | Suite-level workflow study for DBG-02 and UX-03. | Underlying IP, transports, device support and redistribution rights must be checked separately. Documented commands are not evidence of Nodal or Gowin support. |
| REF-18: [Wellen](https://github.com/ekiwi/wellen) | Rust waveform data structures and VCD/FST ingestion. | First Rust reader candidate to evaluate for DBG-03.1/.2. | Upstream identifies BSD-3-Clause. Measure the selected version's memory/query behavior and verify format semantics; do not infer bounded indexing from the language choice. |
| REF-19: [Surfer](https://surfer-project.org/), [GTKWave](https://github.com/gtkwave/gtkwave) | Waveform interaction, source navigation and external-viewer interoperability. | Viewer references for UX-02/UX-03; optional external viewing in DBG-02 and independent-reader checks in DBG-03. | No mandatory GUI for capture/export. Readers sharing parsers are not fully independent; review licenses and deployment separately before embedding. |

Recommended evaluation order: LiteScope for one real reference-device capture, Manta for API ideas, wbscope for capture-state verification, Raptor for suite interaction, and Wellen for offline waveform ingestion. This order is a project recommendation, not a benchmark result or a dependency lock. Automatic Nodal-source insertion and own-fabric integration remain in DBG-05; advanced correlation remains in DBG-04.

## Required adoption record

Before an owning implementation child claims a dependency is selected or qualified, attach a record to its evidence with:

| Field | Required content |
| --- | --- |
| Scope and owner | Reference ID, owning increment/child, component/subdirectory studied and the decision: study-only, subprocess, library, IP, redistribution or checker. |
| Immutable identity | Upstream URL, exact release/commit, source/archive digest, transitive dependencies, device databases and host/tool runtime digests. All are unselected in this roadmap until recorded by the owning implementation. |
| Rights and maintenance | Exact license files/notices for code, IP, examples and databases; approved use/distribution decision; support/maintenance assessment and known issues. Subprocess separation does not by itself settle obligations. |
| Reproduction | Supported device/language/features, commands, inputs, expected results, generated artifacts and actual measurements on a declared host. |
| Correctness and independence | Relevant stage, trigger/capture, timing, protocol and failure tests; shared model/parser risks; independent fixtures and negative cases. |
| Outcome | Adopt, adapt, retain as study-only, defer or reject, with rationale, limitations and a replacement boundary. Missing dependencies or unavailable tests remain open, never a pass. |

TOOL-01.4, IP-01.4 and each integrating child own these records; this catalog is not a duplicate task tracker. No particular upstream release, commercial redistribution approval, hardware result or performance number is asserted here.
