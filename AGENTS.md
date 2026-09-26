# Nodal-EDA project instructions

These instructions apply to the whole repository. A more specific `AGENTS.md`
may narrow them for its subtree. A direct user instruction for the current task
takes precedence. The canonical instruction file is `AGENTS.md`; do not maintain
a second editable `AGENT.md`.

## Scope, branches and architecture

Work on the branch requested for the task; the integration branch is `dev`.
Inspect live refs and the relevant files before resuming. Do not write, reset,
merge or force-push `main` without a separate explicit instruction. Preserve
concurrent changes, published ancestry and historical evidence.

Read [the roadmap index](docs/roadmap/README.md), the complete owning checklist,
[the completion policy](docs/roadmap/completion-policy.md), relevant ADRs and any
contribution instructions that exist before implementing or completing work.

Keep Nodal-EDA a Rust-first, headless-first orchestration/product layer. Follow
[the ownership boundary](docs/architecture.md) and
[ADR-0001](docs/adr/0001-rust-core-external-compiler-boundary.md). Synthesis,
placement, routing, timing engines, fabric generation, compiler IR and analog
physical design belong to Nodal-HDL, Nodal-FPGA or qualified external engines.
Core/fake-tool work must not acquire a Nodal compiler, JVM, device-package or
in-process LLVM/MLIR/CIRCT dependency. Real integrations require actual pinned
provider capabilities; fake tools cannot qualify a real engine or device.

## Pre-implementation increment readiness gate

Before changing implementation source for an increment or sub-increment:

1. Refresh the integration target, candidate branch and PR. Read this file,
   the entire parent/child checklist, linked plans, ADRs, predecessor evidence,
   open review discussion and durable checkpoint.
2. Inspect the relevant Rust modules, contracts, CLI, adapters, artifact/cache
   and run-state boundaries, tests, fixtures, tools and live workflow triggers.
   Identify reusable code, actual external capabilities and validation owners.
3. Classify each obligation as required now, blocked by a named dependency,
   owned by a named later increment, explicitly optional, or genuinely
   non-applicable to the selected profile. Record the reason and the resulting
   acceptance limit. An applicability review is not execution evidence.
4. Preserve stable IDs, original intent, task state and historical evidence.
   Correct inaccurate or duplicate wording under its existing ID. Normally
   retain a non-applicable obligation as an explicit disposition with rationale.
   Removing, narrowing or moving required acceptance needs an explicit reviewed
   scope change under the completion policy; an audit cannot silently waive a
   failure or defer required work to close its parent.
5. Add missing feature-specific obligations. Reuse existing representations and
   validation infrastructure; avoid fixture-specific exceptions, duplicated
   generic checklists, circular prerequisites and unbounded test matrices.
6. For a new implementation increment, use one `increment/<id>-<slug>` branch
   from the refreshed target and one draft PR. Resume the existing branch/PR
   when they exist. Do not start another increment or repository implicitly.
7. If the audit requires checklist edits, publish them as the first focused
   branch commit with `[skip ci]`, update the draft PR/checkpoint, and verify the
   changed-file scope before implementation. No CI is needed for that authorized
   documentation-only scope commit. If no edit is needed, retain the audit
   conclusion without creating an empty commit.
8. Start implementation when scope, dependencies, owners, rejection coverage
   and acceptance are coherent. Required unavailable execution stays blocked;
   it does not become non-applicable merely because a tool is absent.

After the first durable increment commit and draft PR exist, create, re-enable
or update exactly one hourly continuation for that increment. It initially
tracks implementation and blockers, then becomes the CI/closure monitor.
Do not create competing monitors for successive phases.

## Nested checklists and progress

Track Markdown is the authoritative editable task state. The index, generated
views and evidence records reference stable IDs rather than maintaining another
editable checklist. Preserve `FND-01` through `FND-10` and existing numeric child
IDs; use numeric descendants such as `FND-03.2.1` for separately verifiable work.

Mark a leaf `[x]` only with its own deliverable and applicable evidence. A child
with descendants and its parent stay open while any required descendant,
dependency, applicable check, review, demonstration, integration or required
evidence-closure obligation is unfinished. A completed implementation child is
valid partial progress; it does not close the whole increment.

Apply the Foundation review perspectives in
[the Foundation checklist](docs/roadmap/tracks/foundation.md): architecture,
implementation, correctness/rejection, independent validation, optimization
review, scale/determinism/compatibility and final evidence. Adapt these to the
actual feature rather than importing compiler or HDL work into a Rust product.

All non-foundation implementation tracks remain blocked by `FND-10`. Foundation
tests and remote qualification grow with each increment. `FND-01` owns a minimal
self-contained bootstrap CI lane; `FND-09` consolidates and expands coverage,
rather than becoming a reverse prerequisite for earlier increments. Foundation
never depends on the later VER track or on completion of either upstream repo.
Keep required later real-tool/device qualification assigned to its actual owner.

Do not silently drop, weaken, check or relabel a required task to obtain closure.
Reopen affected tasks when their evidence becomes invalid; retain prior evidence
and the reason. Documentation reorganization alone completes no implementation.

## Targeted CI before full CI

For each implementation increment, repair and required evidence closure, qualify
affected source with targeted remote CI before full CI. Local checks are useful
repair evidence; they do not replace required remote qualification.

1. Read live target/candidate/PR state. Publish a clean candidate and record its
   full commit SHA, tree SHA and target SHA. Normally use `[skip ci]` to suppress
   broad automatic push/PR checks during the targeted phase; first inspect which
   live events honor the annotation.
2. Inventory affected workflows from source, tests, schemas, fixtures, toolchain
   pins, manifests, shared gates and prior failures. Record workflow IDs, paths,
   definition identities, inputs, jobs and matrix lanes. Names alone are not
   stable workflow identities.
3. Verify registration, supported triggers and event conditions. Prefer connected
   GitHub `workflow_dispatch` on the candidate ref. Confirm that it executes
   the intended jobs, not PR-only jobs that silently skip.
4. Do not duplicate queued, running or successful qualification for the same
   workflow, candidate, inputs and context. Verify each resulting event, branch,
   head, actual checkout/tree and latest attempt before accepting evidence.
5. Inspect all relevant run/job/check/status pages, logs and artifacts, including
   pagination and matrix lanes. Missing jobs, zero-job greens, old-head results,
   timeouts, cancellations and skipped required jobs are not passes. Record
   genuinely non-applicable skips without giving them execution credit.
6. After the first targeted launch, verify that the increment's single hourly
   continuation is enabled and transition it to CI monitoring. Diagnose actual
   failed logs, fix the cause, and repeat only failed or newly affected checks.
7. Once targeting passes, inventory the full applicable suite for that exact
   candidate, including required repository contexts. Reuse qualifying same-head
   targeted runs; launch only missing full-phase requirements.
8. A full-CI failure returns to failed-first diagnosis and targeted repair.
   Finish qualification for the repaired head before review and merge. Never
   repeatedly relaunch the complete matrix or cancel unrelated work.

A job rerun retains the original source identity. Use a failed/specific-job rerun
only for a diagnosed transient failure with unchanged source. After source,
test, workflow, schema or contract changes, publish a new commit and run the
affected checks on that head. Copied successes in a rerun are not new execution;
verify checkout and step identities. Old-head results do not qualify a new head.

Skip annotations do not bypass required contexts or authorize fabricated status.
If a required check cannot be run through an authorized route, record the exact
blocker and keep the increment open.

### Bootstrap and browserless CI routes

Do not require the user to run CLI commands or supply a personal token when an
authorized repository route exists. Prefer connected GitHub operations.

This repository starts without implementation workflows. FND-01 must establish
the smallest remote build/help, roadmap and architecture-boundary qualification
lane; later increments extend checks for their own work. FND-09 owns consolidated
fault, compatibility, determinism and performance coverage. Do not postpone all
early testing until FND-09 or call nonexistent workflows successful.

For a new workflow unavailable to `workflow_dispatch`, use a reviewed,
narrowly filtered bootstrap push/PR trigger that runs only the affected checks
on the intended candidate. Inventory every matching workflow before publishing;
the trigger commit must not be skipped if that would prevent qualification.
Use this route only when the task already authorizes implementation and CI.
It must not change `main`, the default branch, repository protection or unrelated
triggers. If no isolated route exists, report that specific blocker.

Where implementation publication and CI are already authorized, a narrowly
scoped repository dispatcher may be used when direct dispatch is unavailable:

- Use a dedicated control branch distinct from feature/integration branches,
  with exact branch/path filters and only `contents: read` and `actions: write`.
  Use the runner's automatic job token; never request or extract personal tokens.
- Bind the controller to the repository, increment/PR, base and candidate
  refs/SHAs/tree, workflow IDs/definition hashes and exact dispatch inputs.
  Recheck live identities before each action and fail closed on movement.
- Allow only the reviewed workflow-dispatch endpoint as a write. Deduplicate
  matching active/passing runs, record intent before dispatch, and reconcile
  uncertain responses before retrying. Keep a token-free dispatch ledger.
- Use bounded timeouts and serialized dispatch. Do not execute candidate-owned
  code in the privileged job, publish source, merge, change protections,
  cancel unrelated work or launch broad CI as a side effect.
- Verify that only the intended controller matches its push; keep its files off
  feature/integration branches. A controller launch commit must not suppress its
  own trigger. A green controller proves dispatch only, not qualification.

A dispatcher does not solve missing workflow registration or override a safety
denial, repository restriction or genuinely missing access. Use the reviewed
bootstrap route where applicable; otherwise preserve and report the blocker.

## Hourly continuation through closure

After the first durable increment commit and draft PR exist, use the available
scheduler with `RRULE:FREQ=HOURLY`. Reuse one task through implementation,
targeted CI, full CI, review, merge and evidence closure. Verify scheduling
actually succeeded before reporting it enabled; report unavailable scheduling
without claiming background progress.

Each execution must:

1. Refresh live refs, PR/review state, checklist and checkpoint. Avoid competing
   writes when another worker is active or publishing. Recheck refs before writes.
2. Continue only already-authorized work. Before CI, work from the audited
   checklist, run proportionate local checks and retain durable checkpoints.
   Do not launch CI before a clean candidate and affected-check inventory exist.
3. During CI, inspect latest-attempt failures and actual artifacts; diagnose
   infrastructure failures before bounded retries. Publish generic repairs and
   qualify only failed/newly affected requirements before completing full CI.
4. Update the checkpoint with phase, repository/increment/PR, candidate/base/tree,
   completed child IDs, scope decisions, local evidence, workflow/run/attempt
   identities, failures, remaining obligations and the next safe action.
5. After exact-final-head qualification and review, perform the already-authorized
   verified merge below. Continue until evidence, authoritative roadmap state
   and completion demonstration/report are complete.

Stay quiet for unchanged queued/running work; report meaningful failures, fixes,
blockers, verified merge and accepted completion. Keep the monitor enabled
while closure is outstanding unless the user pauses/cancels it. A persistent
blocker is not completion; do not repeatedly publish identical checkpoints or
hammer failing services. Disable the task only after legitimate closure.

## Verified merge with post-merge CI suppressed

- Require all applicable targeted/full checks and review on the exact final
  head. Re-read target/candidate refs, required contexts and mergeability just
  before merge. Reconcile target movement and qualify changed integration before
  proceeding.
- Preserve published ancestry. Use a normal merge unless the user or repository
  policy explicitly requires another method; do not import another repository's
  squash policy implicitly. Supply the verified expected head and include
  `[skip ci]` in the actual merge message. Do not add an untested source commit
  just to carry that annotation or bypass protection.
- Verify GitHub's actual merged state, merge commit, parents, final target ref,
  message and tree. The integrated tree must equal the qualified candidate tree
  for CI suppression; a prospective test-merge SHA is not a verified merge.
- Inspect live event filters before relying on skip annotations. Verify intended
  post-merge push suppression; do not globally disable workflows, cancel
  unrelated runs or dispatch duplicate post-merge CI. Inspect and report
  unexpected triggered runs.
- Record `post_merge_ci: skipped`, reason `qualified-identical-tree-merge`,
  actual merge/tree identities and the executed pre-merge evidence. Never call
  skipped CI executed/passed, invent run IDs or rewrite historical records.
- Complete any required evidence-closure change with its applicable checks and
  review. Do not create a separate closure PR solely as ceremony when the
  completion policy can be satisfied in the increment PR.

A mismatched merge tree or unsatisfied mandatory check leaves the increment
open and monitoring active until the discrepancy is resolved and qualified.

## Evidence and completion demonstrations

Keep durable implementation checkpoints and evidence under
`docs/evidence/<increment-id>.md` when work starts. Record implementation commits,
the tested source/tree, actual tool/device-package identities, exact commands,
fixtures, outcomes, artifacts, limits, review and verified integration. Report
pass, fail, bounded-only, unknown, unavailable and skipped distinctly.

For every completed increment/sub-increment, show an actual CLI/API demonstration
when useful. When the work affects generated RTL, include actual Nodal Scala
source and corresponding actual generated Verilog-* output, the backend,
source/output paths, commands and tool versions. Label illustrative syntax as
illustrative; it cannot replace actual output.

When generated RTL is unaffected, state:
"This increment does not affect generated Verilog (Verilog-*)."
Explain briefly why. Do not invent HDL work for a Rust orchestration increment.

Never weaken tests, simulations, proofs, mutation controls, review contracts,
timeouts or required matrices merely to obtain a pass. Retain failed evidence.

## Documentation-only updates

For an authorized instruction/roadmap-only update with CI waived, use the
requested existing branch and a `[skip ci]` commit. Review the diff, links, IDs,
nesting, dependencies and preserved task states locally. Do not create a new
branch, PR, controller, monitor, workflow or implementation merely to exercise
the increment lifecycle. This exception does not waive implementation or
increment-closure qualification, and document validation is not product CI.

## Security and compatibility

Treat projects, third-party tool output, plugins, packages and archives as
untrusted inputs. Never commit keys, credentials, proprietary PDKs, customer
designs, unlicensed artifacts or private support-bundle data. Hardware writes
require explicit target identity and an authorized operation; builds must not
implicitly program a board.

Schema/protocol/constraint changes need compatibility fixtures and documented
migration. Performance budgets remain targets until measured on a declared
host; correctness/security gates cannot be traded for a faster benchmark.
