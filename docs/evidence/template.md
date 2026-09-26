# Increment evidence template

Copy the relevant fields into the increment's durable record. Fill them with
actual observations; this template itself is not accepted execution evidence.

- Increment, branch, PR and current phase:
- Readiness target commit/tree and inspected instructions/plans:
- Obligation applicability, actual prerequisites and validation owners:
- Implementation commits and completed leaf/child IDs:
- Reviewed/tested source commit/tree; dirty local evidence identified separately:
- Toolchain, package/device and host identities:
- Exact commands, independently authored fixtures and retained seeds:
- Results: pass / fail / bounded-only / unknown / unavailable / skipped:
- Targeted/full workflow ID, path, definition identity, event/ref and inputs:
- Run/attempt/job IDs, actual checkout and required lane outcomes:
- Artifact paths, hashes and immutable external references:
- Performance measurements, budgets and supported-profile limits:
- Source/dependency/optimization review and reviewer identity/kind:
- Actual CLI/API or applicable source/generated-Verilog demonstration:
- Verified merge commit, parents, tree and observed target head:
- Post-merge CI disposition and reason; skipped is never executed/passed:
- Remaining closure obligations, next safe action and monitor disposition:

Keep historical failures and evidence immutable. A source commit cannot contain
its own final hash; identify runtime-generated qualification by the actual CI
source/checkout and link its artifact/PR record. Record actual merge facts only
after merge, never pre-fill a prospective merge as completed.
