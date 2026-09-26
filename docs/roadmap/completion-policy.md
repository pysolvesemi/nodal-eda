# Increment and subtask completion policy

## Source of truth

The task list in each track file is authoritative. The index and release milestones reference IDs rather than maintaining a second copy of task state. All initial task boxes are open because the repository contains a plan, not an implementation.

## Nested task semantics

Use this structure; the checked child below is an **illustrative example, not project status**:

```markdown
- [ ] **FLOW-EXAMPLE — Recoverable build execution**
  - [x] **FLOW-EXAMPLE.1** Implement and test the state journal.
  - [ ] **FLOW-EXAMPLE.2** Test cancellation and process crashes.
  - [ ] **FLOW-EXAMPLE.3** Attach final integration evidence and close the increment.
```

An implemented, verified child can be marked `[x]` even while the parent remains `[ ]`. Every level obeys the same rule if a child is split into grandchildren. Progress is the count of completed required leaf tasks, not a subjective percentage. A parent is not automatically complete merely because its first coding task is done.

Preserve existing task identities when splitting compound work. Foundation uses
numeric grandchildren under its existing six children per increment; a split
must retain every original obligation. A task's text and applicable linked
acceptance remain binding even when descendants do not repeat every detail.
Applicability review and execution are separate results: absent tools, unfinished
dependencies or failed checks cannot be relabeled non-applicable. Required
blocked descendants keep their ancestors open.

## Parent closure predicate

An increment may become `[x]` only when all of the following hold:

1. Every required descendant is `[x]` and each has evidence appropriate to its scope.
2. All declared internal dependencies are complete and external capabilities are verified against pinned artifacts.
3. The user-visible demonstration and exit criteria pass; applicable correctness, compatibility, security, and performance gates pass on the exact reviewed candidate. Apply the [targeted-first CI and review rules](../../AGENTS.md#targeted-ci-before-full-ci), including current predecessor coverage.
4. Implementation is integrated into the required branch; the report identifies the commit/tree actually tested and the verified integration result. Apply the [merge/suppression rule](../../AGENTS.md#verified-merge-with-post-merge-ci-suppressed): skip duplicate post-merge CI only for the qualified identical tree, and report it as skipped. If integration changes the tree, reconcile and qualify the change.
5. An evidence record exists with commands, inputs, outcomes, tool/device versions, limitations, raw artifact references, review and integration identities. Complete any required evidence-closure work and the actual user-facing demonstration/report; only then end the increment's hourly continuation.

A completed child may cite a prior commit when its result remains valid, but the parent needs current integrated qualification. A mock adapter is not evidence of a real tool/device integration. A simulation result is not silicon qualification. A plan, interface stub, generated example, or unavailable dependency cannot close implementation work.

## Changes and exceptions

Before implementation, follow the [readiness gate](../../AGENTS.md#pre-implementation-increment-readiness-gate):
review live source, complete checklist, real prerequisites and validation owners.
Classify obligations and retain the rationale, restricted claim and any later
owner; publish a necessary checklist correction before code changes. A review
does not grant permission to remove required acceptance merely to unblock work.

Never silently drop a failed child, mark an unsupported requirement complete, or turn a required test into an optional test. Scope changes require an explicit rationale and review; preserve the original ID and historical disposition. Reopen the affected parent and child when their evidence becomes invalid. An approved product exception must remain visible in release qualification and must not be called a passing test.

## Dependency rules

`FND-10` is an implicit hard prerequisite of every non-foundation increment. Track files also list additional prerequisites. Dependencies mean predecessor completion, not merely having started it. Foundation has independent bootstrap verification, avoiding a cycle through the verification track. FND-01 introduces minimal remote qualification; each increment supplies its own tests, while FND-09 consolidates and expands the harness without becoming a reverse prerequisite. Work can proceed in parallel after the gate only when the individual prerequisite graph allows it.

External dependencies are capability contracts: record provider, exact version/digest, API/schema, supported feature subset, test fixture, and availability. They are not unverifiable statements such as "latest Nodal supports this".

## Evidence record template

```markdown
# <INCREMENT-ID> evidence
Current phase, increment branch and PR:
Readiness audit, scope/applicability decisions and validation owners:
Implementation commits:
Reviewed/tested source commit and tree:
Integration target/base and verified merged commit/tree:
Integrated branch/head:
Completed leaf/child IDs and their evidence references:
Dependency and external-capability evidence:
Toolchain/device/package/OS/host digests:
Commands and fixture IDs:
Results: pass / fail / bounded-only / unknown / unavailable / skipped
Targeted/full workflow IDs, paths, definition identities, inputs and required lanes:
Run/attempt/job identities, checkout evidence and applicable outcomes:
Review, merge verification and post-merge CI disposition with reason:
Hourly continuation identity and remaining closure obligations:
Performance measurements and baseline:
Artifacts and content hashes:
CLI/API or source/generated-Verilog demonstration:
Known limits and remaining work:
```

No future evidence file should contain invented benchmark numbers, tool output, generated RTL, CI status, or a claimed merge.

## Automated policy checks to implement in FND-01

The documentation checker must parse task nesting, unique IDs, valid dependency references, dependency cycles, missing evidence for closed tasks, and a closed parent containing an open descendant. It must ignore fenced examples. Tests must include a partially complete parent that is valid, and an incorrectly closed parent that fails. Checking a child must never automatically check its parent without evaluating the full closure predicate.
