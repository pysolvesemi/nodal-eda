# nodal-eda

A Rust-first, headless-first EDA product under development for the Nodal commercial FPGA ecosystem.

`nodal-eda` manages projects, build flows, tool integration, constraints, reports, device packages, programming, debugging, and the eventual desktop experience. It is **not another synthesis engine or FPGA fabric generator**.

## Development plan

The FND-01 bootstrap provides a pinned Rust workspace, `nodal-eda --help` and
`nodal-eda --version`, plus executable roadmap/dependency checks. See
[contribution and build commands](CONTRIBUTING.md), the
[bootstrap design](docs/development/fnd-01.md) and
[current FND-01 evidence](docs/evidence/FND-01.md) for qualification status.

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

**Status:** executable help/version and repository-check bootstrap. Project builds,
real tool/device integration, FPGA programming and commercial qualification remain
roadmap work. The task files and evidence records distinguish implemented children
from accepted increment completion; no real-device or HDL capability is implied.

Development takes place on `dev`. This documentation update does not change `main`.
