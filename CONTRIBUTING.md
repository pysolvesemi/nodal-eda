# Contributing to Nodal-EDA

Read [AGENTS.md](AGENTS.md), the complete owning roadmap checklist and the
[completion policy](docs/roadmap/completion-policy.md) before implementation.
Development targets `dev`; do not publish to `main` without an explicit task.
Use one increment branch and draft PR, preserve published ancestry and concurrent
changes, and keep the readiness audit and evidence in `docs/evidence/`.

## Bootstrap commands

The initial supported profile is Linux x86-64 with Rust 1.90.0 (rustfmt and
Clippy), Python 3.11+, Git and a C linker/binutils. The repository's
toolchain file selects the exact Rust version. Provision these host utilities
before an offline build; no Nodal compiler, JVM or separate LLVM/MLIR/CIRCT SDK
is required. Rust's internal use of LLVM is permitted by ADR-0001.

```sh
cargo build --workspace --locked --offline
cargo run --locked --offline -p nodal-eda-cli -- --help
cargo run --locked --offline -p nodal-eda-cli -- --version
python3 tools/dev.py targeted
python3 tools/qualify.py
```

Targeted checks enforce rustfmt, Clippy with warnings denied, binary-level CLI
behavior, the independent Python fixture suites, roadmap structure and the
all-feature dependency boundary. `qualify.py` creates a fresh target and Cargo
home and builds offline using an explicit host-tool PATH without Java, Nodal or
compiler-SDK discovery commands. It inspects actual ELF dependencies and records
real CLI output, repeated B0 startup measurements and a product RSS sample.
Outputs go to ignored `out/`; CI retains them as artifacts keyed by actual head.

Python maintenance code uses the standard library only. Follow PEP 8 naming and
clear control flow; fixture data may use long lines when keeping a complete
malformed-input example together aids review. Rust obeys workspace lints and
rustfmt. Add meaningful rejection/regression cases for changed contracts; do
not write tests that merely repeat an implementation expression.

## Progress and evidence

Use two spaces per checklist nesting level, stable numeric descendant IDs and
one `Depends on` declaration per parent. Every checked task needs an inline
local `Evidence: [label](path#heading)` reference to its actual record. The
checker verifies that the referenced file/heading exists inside the repository;
it does not certify the truth of remote execution, review or integration claims.

Parents remain open until required descendants, predecessors, applicable
qualification, review, demonstration and verified integration are complete.
Preserve partial child progress. Do not remove or reclassify required acceptance
to conceal a failure. Document and review necessary scope changes before code,
retaining original IDs, rationale and historical disposition.

Use the [evidence template](docs/evidence/template.md), keeping actual results
distinct from planned commands. A local dirty-tree result is local repair
evidence; candidate qualification requires exact source/tree identity and actual
remote jobs. Separate executed tests from skipped duplicate post-merge CI.

## Architecture and dependency review

The reviewed inventory is [policy/architecture.toml](policy/architecture.toml).
At FND-01, only `eda-contracts` and `nodal-eda-cli` are application packages;
their sole dependency edge is CLI to contracts. There are no third-party Cargo
dependencies, native build scripts, runtime plugin loaders or Cargo overrides.
Review direct, optional, target-specific, build/dev and transitive dependencies
before changing that inventory. Never relax a guard merely to pass its mutant.

For a proposed dependency, record the owning feature, exact version/source,
license and notices, maintenance/security implications, enabled features,
transitive closure, native build/link/load effects and compatibility tests.
Subprocess isolation does not decide redistribution obligations. Product
publication remains disabled; this bootstrap does not grant distribution terms
or add a product license. Review those before a release.

Host utilities are inventoried separately. Their implementation language or use
of LLVM does not make them application dependencies. Review the actual product
closure and binary rather than searching the host for the word LLVM.

## CI, review and integration

Follow the targeted-first lifecycle in AGENTS.md. The FND-01 workflow is a
bootstrap route restricted to `increment/fnd-01-bootstrap`; its full job depends
on successful targeting. Both jobs are required. The branch-push event checks
out the actual candidate SHA, avoiding prospective PR merge-tree ambiguity.
Manual dispatch is available only when GitHub has registered the workflow.

Review the complete diff, applicable fixture outcomes, exact-source artifacts,
dependency inventory, performance results and remaining limitations. Distinguish
agent self-review from an independent human review; honor any live repository
review requirement. Never invent approval. Merge with the expected head only
after all gates; verify actual parents/tree and final `dev`, then finish evidence
and checklist closure. Do not start the next increment implicitly.
