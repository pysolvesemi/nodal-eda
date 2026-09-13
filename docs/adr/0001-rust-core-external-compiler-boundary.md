# ADR-0001: Rust product core with external compiler engines

## Status and scope

Accepted architecture decision. Implementation and qualification remain open in the existing Foundation, Toolchain and Verification tracks. This record adds no completed implementation claim and does not create a new compiler track.

Keep this boundary through MVP, commercial release and high-end product growth. It is not a temporary shortcut that must later be replaced by an in-process compiler framework.

## Context

Nodal-EDA is the project, workflow, artifact, reporting and hardware-session product. Nodal-HDL owns its compiler pipeline; Nodal-FPGA and qualified external engines own device and implementation semantics. See the [ownership table](../architecture.md).

MLIR provides reusable compiler representations and transformations; CIRCT applies LLVM/MLIR infrastructure to hardware design [1, 2]. These capabilities can be used by the complete Nodal suite without embedding them in the EDA application. Rust is an implementation language, not an alternative compiler framework. Interoperability is possible: MLIR provides a C API intended for language bindings [3]. The decision below is therefore about responsibility, isolation and compatibility, not a claim that Rust cannot use MLIR.

## Decision

The Nodal-EDA core, contracts, default CLI and ordinary product services are Rust components with no required MLIR/CIRCT compiler-framework dependency. They do not link or dynamically load LLVM/MLIR/CIRCT compiler libraries, host dialects, run compiler passes or require a separate compiler-framework SDK to build. Direct and transitive dependencies are covered; an optional/default Cargo feature must not silently defeat this boundary.

This restriction does not ban the approved Rust toolchain, platform compiler/linker, coverage tools or other build utilities because of how those tools are implemented. Audit application dependencies and linked/loaded libraries, not merely the occurrence of the word LLVM on a machine. A separate LLVM SDK is not a Nodal-EDA core requirement.

Nodal-HDL may use MLIR and any qualified CIRCT components within its own process/tool package. Other selected synthesis, simulation or analysis engines may also use them. Their dependencies are declared in the selected toolchain, not imposed on every installation of the product core. A full commercial suite may redistribute qualified compiler packages with their licenses and notices; this does not make them core runtime dependencies.

Do not create a Scala frontend, duplicate compiler IR or MLIR pass manager in this repository. UI frameworks remain optional and must not introduce a compiler-framework dependency into the shared product core. Circuit-changing compilation and technology mapping have one declared owning engine per flow.

## Integration contract

```text
Nodal-EDA Rust core / CLI / optional UI
                |
     versioned action and result contracts
                |
       supervised external tool process
          /             |              \
   Nodal-HDL       synthesis tools    Nodal-FPGA
   MLIR pipeline                      device/CAD
          \             |              /
      artifacts + diagnostics + provenance
                |
       product reports and run state
```

Adapters pass versioned requests, explicit options, artifact references and bounded diagnostics/results. Large designs stay in files or engine-owned query services, not full copies of compiler IR in the product process. Source navigation, schematic views and timing views use exported provenance and bounded queries; missing provenance is reported, not reconstructed by importing live MLIR objects.

Pin the adapter, compiler/exporter, actual tool/runtime/plugin dependency closure, target package and export-schema identity in the lock and relevant cache keys. Compiler upgrades must invalidate affected cached actions. Different external engines need compatible interchange contracts, not a single global LLVM/MLIR build. Never infer exporter compatibility from a matching filename extension.

Initial Nodal integration uses the verified Nodal -> Verilog -> Yosys flow. Direct mapped-design handoff is enabled only after both providers qualify its schema, cell modes, constraints and provenance. Do not perform a second technology mapping on already mapped cells. This ADR does not assert that a direct exporter exists today.

MLIR text/bytecode or other engine checkpoints may be archived as opaque artifacts. Nodal-EDA may hash, store, transfer and associate them with their producer, but only a qualified external provider interprets or transforms them. Validation of a transport envelope is not validation of an MLIR program.

## Availability, failure and distribution

Core help/version, project-only validation, stored-report access and the fake-tool foundation workflow must work without Nodal-HDL, a JVM or installed MLIR/CIRCT compiler packages. Select and qualify at least one traditional HDL reference flow that also works without the Nodal compiler stack. Its own Yosys/nextpnr/packer and ordinary platform dependencies remain required.

A Nodal-source build still requires its selected Nodal compiler and runtime. Missing or incompatible compilers fail that requested flow clearly; no false pass, unapproved fallback, automatic download or failure of unrelated core operations is allowed. External crashes/timeouts/cancellation must preserve durable run state and must not publish successful cache entries.

Base application and optional tool packages need separate inventories and dependency manifests. Installation, upgrade, offline replay and support bundles identify which package owns each dependency. Measure product overhead separately from external compiler resources, while also reporting total end-to-end CPU, memory, disk and time. A subprocess boundary is not a security sandbox.

## Acceptance matrix and roadmap ownership

These are required acceptance details for the existing child tasks, not a second copy of checkbox state. Applicable candidate-head evidence is required before the owning child can close.

| Gate | Existing owner | Required evidence |
| --- | --- | --- |
| Dependency boundary | FND-01.2, FND-01.5 | Reviewed dependency/feature and build/link/load boundaries; reject a test mutant that introduces an in-process compiler library into the core. |
| Compiler-independent foundation | FND-09.3, FND-10.3 | Clean core build and fake-tool/help/project/report tests without separately installed compiler-framework SDKs, Nodal-HDL or JVM; record allowed host/toolchain utilities. |
| Traditional HDL independence | TOOL-02.6, VER-02.1 | Actual qualified Yosys/nextpnr/packer flow on a host without the Nodal compiler stack; compare against the pinned direct-tool reference. |
| Compiler adapter isolation | TOOL-04.1 through TOOL-04.6 | Real exporter capability negotiation, source provenance, versioned artifacts and absent/crashed/incompatible compiler cases; unrelated core operations remain usable. |
| Upgrade and cache correctness | TOOL-04.5, VER-02.4 | Changed adapter/compiler/runtime/export identity invalidates affected actions; unsupported exports fail explicitly; stable unrelated actions remain reusable. |
| Release continuity | VER-05.3, VER-06.4 | Repeat the boundary and package-availability matrix on advertised release profiles, including optional desktop/service builds when shipped. |

Foundation gates use fake tools and dependency fixtures; they do not depend on real Nodal integration or later VER tasks. All non-foundation work remains blocked by FND-10. Keep existing performance budgets and nested-checkbox closure rules. A passed mock boundary test does not complete a real-tool integration child.

## Consequences and reconsideration

The product can invoke, upgrade and replace qualified engines independently while preserving its project, cache and report contracts. The cost is maintaining explicit exporters/adapters and accounting for serialization and subprocess startup. Measure these costs before replacing process boundaries with native bindings; use persistent external query/compiler services only when justified and keep ordinary builds headless.

A future feature that genuinely needs compiler-IR transformation should first be implemented in the owning compiler or a separately versioned optional helper. An in-process exception requires a superseding ADR with a concrete use case, measured benefit, alternatives, ABI/version and license analysis, security/failure isolation, rollback strategy and revised compatibility/performance tests. It must not silently become mandatory for core or traditional-HDL users. "Commercial grade" or "high-end" alone is not a reason to reverse this decision.

## Primary references

References establish tool scope and interoperability, not a claim that this implementation already exists. Reviewed 2026-09-13.

1. MLIR project, [Multi-Level Intermediate Representation Overview](https://mlir.llvm.org/): compiler infrastructure and modular transformations.
2. CIRCT project, [CIRCT Charter](https://circt.llvm.org/docs/Charter/): LLVM/MLIR-based hardware design abstractions and flows.
3. MLIR project, [MLIR C API](https://mlir.llvm.org/docs/CAPI/): interface intended for wrapping by other languages. Recheck version compatibility for any proposed integration.
