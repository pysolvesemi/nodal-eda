# Repository working instructions

## Scope and branches

Work on the branch explicitly requested for the task. The current development branch is `dev`. Do not write, reset, merge, or force-push `main` without a separate explicit instruction. Inspect the remote branch and relevant files before resuming work; a chat report or a roadmap checkbox is not implementation evidence.

Keep `nodal-eda` a Rust-first EDA orchestration/product layer. Do not duplicate synthesis, placement, routing, timing engines, FPGA fabric generation, MLIR infrastructure, or analog physical design here. Use the ownership boundaries in `docs/architecture.md`.

## Roadmap execution

The controlling index is `docs/roadmap/README.md`; per-track files own the task state. Follow `docs/roadmap/completion-policy.md`.

Every increment is a parent Markdown task and every deliverable is a child Markdown task. Mark a child `[x]` only when that child is implemented and its applicable tests/evidence exist. A parent remains `[ ]` while any child is `[ ]`, a dependency is incomplete, an applicable check fails, or evidence is missing. Completing the documentation is not completing an implementation increment.

All non-foundation implementation tracks are blocked by `FND-10`. Foundation includes its own executable bootstrap tests; it must not depend on the later verification track. Respect additional cross-track and external capability blockers. Do not silently waive, delete, or weaken a child to close its parent. Reopen affected parents if later changes invalidate their evidence.

Preserve stable increment and child IDs. Split oversized work into explicit children or new increments rather than claiming partial work is complete. Record partial progress at child level so work can resume safely.

## Evidence and reports

Record implementation commits, the tested source/tree, tool and device-package digests, exact commands, test outcomes, artifacts, and limitations under `docs/evidence/<increment-id>.md` when implementation starts. Never report skipped, unavailable, timed-out, bounded-only, or unknown verification as passed.

For an increment affecting emitted RTL, include actual Nodal Scala source and the corresponding actual generated Verilog where applicable, with reproduction commands and tool versions. Label illustrative syntax as illustrative. For an increment that does not affect generated RTL, state: "This increment does not affect generated Verilog (Verilog-*)." Show an actual CLI/API demonstration instead when useful.

Use local/unit tests and applicable integration, security, scalability, and final-head qualification checks. Documentation-only updates must not claim product CI passed. Do not add or alter CI merely to make a documentation change appear tested.

## Security and compatibility

Treat projects, third-party tool output, plugins, packages, and archives as untrusted inputs. Never commit keys, credentials, proprietary PDKs, customer designs, unlicensed reference artifacts, or support bundles containing private data. Hardware writes require explicit target identity and an authorized operation; builds must never implicitly program a board.

Schema/protocol/constraint changes need compatibility fixtures and a documented migration. Performance budgets are targets until measured on a declared host. Correctness and security gates cannot be traded for a faster benchmark.
