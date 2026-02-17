# Execution Agent Prompt Template

Use this prompt with a coding agent after design artifacts are complete.

```text
Use the execution-agent playbook and implement the UX revamp from artifact files.

Inputs:
- artifact directory: <run-artifacts/run-id>
- execution manifest: <run-artifacts/run-id/12-execution-manifest.md>
- traceability matrix: <run-artifacts/run-id/traceability-matrix.md or csv>
- architecture delta report: <run-artifacts/run-id/13-architecture-delta-report.md>
- implementation completeness matrix: <run-artifacts/run-id/14-implementation-completeness-matrix.md>
- artifact intake: <run-artifacts/run-id/15-artifact-intake.md>
- execution batch plan: <run-artifacts/run-id/16-execution-batch-plan.md>
- implementation change log: <run-artifacts/run-id/17-implementation-change-log.md>

Rules:
1) Before coding, read all artifacts and create `15-artifact-intake.md`.
2) If planning skill/agent is available, delegate planning and produce `16-execution-batch-plan.md`.
3) Do not edit code before 15 and 16 exist.
4) Implement in dependency-ordered batches from the execution manifest and batch plan.
5) Follow library target and component mapping from screen specs.
6) Run cross-artifact consistency check before implementation:
   - python scripts/check_artifact_consistency.py <run-artifacts/run-id>
7) Run execution-readiness check before claiming completion:
   - python scripts/check_execution_readiness.py <run-artifacts/run-id>
8) Do not ask for routine approval between batches unless hard blocker exists.
9) Update traceability evidence as you implement.
10) Never silently drop a requirement. If a requirement needs architectural work,
   record it in architecture delta report and completeness matrix.
11) Run tests and quality gates before completion:
   - golden flow
   - state coverage
   - accessibility checks
   - visual regression (if available)
12) Validate completeness matrix:
   - each requirement is implemented, blocked, or deferred
   - blocked/deferred must include reason, evidence, and owner
13) At the end, return:
   - changed files summary
   - test/validation results
   - architecture-impact items and decisions
   - planning handoff proof and batch log
   - remaining risks and blockers
```
