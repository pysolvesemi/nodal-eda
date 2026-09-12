# Research sources and evidence limits

The links below were checked for this roadmap on 2026-09-13. They establish tool roles and design precedents, not that Nodal-EDA has implemented or qualified those features. Mutable documentation must be accompanied by exact release/commit and runtime digests when an adapter is implemented. Architecture choices and performance budgets are recommendations, not measurements copied from these sources.

## S01

GOWIN Semiconductor, [GOWIN EDA](https://www.gowinsemi.com/en/support/home). Official product description covers design entry, synthesis, place/route, bitstream download, IP generation and analyzer integration. Supports the decision to make this repository a product layer rather than another synthesizer. It does not establish feature parity for this roadmap.

## S02

YosysHQ, [Yosys documentation](https://yosyshq.readthedocs.io/projects/yosys/en/latest/) and [symbolic model checking](https://yosyshq.readthedocs.io/projects/yosys/en/latest/using_yosys/more_scripting/model_checking.html). Primary synthesis/transformation and verification reference. Qualify the precise language/frontend/plugin subset; do not advertise universal SystemVerilog or VHDL support merely because a Yosys executable is present.

## S03

YosysHQ, [nextpnr](https://github.com/YosysHQ/nextpnr) and [architecture API](https://github.com/YosysHQ/nextpnr/blob/main/docs/archapi.md). Documents timing-driven FPGA implementation, architecture-specific resources and device backends. A reference adapter must pin the architecture, database, packer and exact tool version. Generic or experimental support is not commercial device qualification.

## S04

YosysHQ, [Equivalence Checking with Yosys (EQY)](https://yosyshq.readthedocs.io/projects/eqy/en/latest/). Defines EQY's role as a formal hardware-equivalence driver, including partitioning and X-propagation considerations. Applicable to supported hardware artifacts, not a proof of Rust orchestration code.

## S05

YosysHQ, [SymbiYosys](https://yosyshq.readthedocs.io/projects/sby/en/latest/). Documents bounded and unbounded safety, cover and liveness workflows. Record assumptions and proof mode; bounded-only or unknown outcomes cannot be promoted to an unbounded proof.

## S06

FPGA Research/FABulous, [Simulation setup](https://fabulous.readthedocs.io/en/latest/user_guide/simulation/simulation.html). Documents compiling a user design, loading its bitstream into generated fabric RTL, and simulating configuration/routing/primitive behavior. This motivates an optional reference-fabric adapter. It does not justify byte-for-byte or PPA comparisons between different architectures, nor replace user-design verification.

## S07

Bazel, [Remote caching](https://bazel.build/remote/caching). Documents action-result cache versus content-addressed storage, declared actions, trusted cache writers and pitfalls involving tool/environment identity. Used as a precedent for explicit action keys and artifact provenance; this roadmap does not require adopting Bazel or implementing a new Bazel replacement.

## S08

Bazel, [Hermeticity](https://bazel.build/basics/hermeticity). Explains source identity, isolation and host dependencies. Supports replay/invalidation tests. A wrapper cannot simply promise reproducibility for all third-party engines or host platforms.

## S09

Tauri, [Capabilities](https://tauri.app/security/capabilities/) and [Updater](https://tauri.app/plugin/updater/). Reference for a possible optional Rust/web desktop shell and scoped frontend permissions/signed updates. GUI security does not by itself sandbox external CAD tools. Pin the actual major version and validate OS/WebView prerequisites before choosing the deployment matrix.

## S10

The Update Framework, [Specification](https://theupdateframework.github.io/specification/latest/) (retrieved version 1.0.36, last modified 2026-08-05). Reference for signed metadata, roles, trust rotation and update-attack defenses. Reuse a maintained implementation after dependency/security review. Signing alone does not establish correctness or a complete product security policy.

## S11

openFPGALoader, [Advanced usage](https://trabucayre.github.io/openFPGALoader/guide/advanced.html). Primary programming reference for device/cable/flash workflows. Integration and verification/readback behavior remain device-specific. Require target identity and safe recovery tests instead of assuming every board is supported.

## S12

OpenROAD, [Project documentation](https://openroad.readthedocs.io/en/latest/main/README.html). ASIC physical-design automation precedent. Relevant only to importing/coordinating physical implementation evidence where appropriate; it is not a replacement for FPGA resource-based placement/routing and is not owned by Nodal-EDA.

## Research conclusions

Integrate existing engines before writing replacements. Use direct-tool comparisons for orchestration fidelity, formal/simulation for supported generated hardware, independent small reference models for cache/state/configuration semantics, and actual lab/silicon evidence for hardware claims. No single comparison establishes a commercial product. Keep the first release support matrix narrow, explicit, pinned and independently reproducible.
