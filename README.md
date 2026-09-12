# nodal-eda

A planned Rust-first, headless-first EDA product for the Nodal commercial FPGA ecosystem.

`nodal-eda` manages projects, build flows, tool integration, constraints, reports, device packages, programming, debugging, and the eventual desktop experience. It is **not another synthesis engine or FPGA fabric generator**.

## Development plan

Start with the [incremental roadmap](docs/roadmap/README.md). It contains a foundation track and eleven dependent tracks, with individually checkable subtasks and explicit completion gates.

- [Architecture and scalable directory plan](docs/architecture.md)
- [Verification strategy and valid cross-tool comparisons](docs/verification.md)
- [Performance budgets and scale fixtures](docs/performance.md)
- [Checkbox and completion policy](docs/roadmap/completion-policy.md)
- [Research sources and limits](docs/research-sources.md)

## Ecosystem boundaries

| Project | Responsibility |
| --- | --- |
| `nodal-hdl` | Nodal language, Scala frontend, existing MLIR-based compiler, source provenance, and supported compilation/export paths. |
| `nodal-fpga` | FPGA architecture/fabric, device database, target-specific legality and implementation engines, configuration/bitstream semantics, and device protocol contracts. Initially it may use external engines. |
| `nodal-eda` | Customer workflow and product layer that invokes those engines and qualified third-party tools through versioned adapters. |

Traditional Verilog users must not need Nodal or a JVM. No LLVM/MLIR runtime is required inside the `nodal-eda` core. An initial Nodal integration may use generated Verilog followed by Yosys; direct mapped-netlist integration is gated on an actual supported compiler export, not assumed to exist.

**Status:** documentation and implementation plan only. No product capability, benchmark result, formal proof, device support, or commercial qualification is claimed by this repository yet. The initial roadmap deliberately leaves every implementation checkbox open.

Development takes place on `dev`. This documentation update does not change `main`.
