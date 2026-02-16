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

Rules:
1) Implement in dependency-ordered batches from the execution manifest.
2) Follow library target and component mapping from screen specs.
3) Do not ask for routine approval between batches unless hard blocker exists.
4) Update traceability evidence as you implement.
5) Never silently drop a requirement. If a requirement needs architectural work,
   record it in architecture delta report and completeness matrix.
6) Run tests and quality gates before completion:
   - golden flow
   - state coverage
   - accessibility checks
   - visual regression (if available)
7) Validate completeness matrix:
   - each requirement is implemented, blocked, or deferred
   - blocked/deferred must include reason, evidence, and owner
8) At the end, return:
   - changed files summary
   - test/validation results
   - architecture-impact items and decisions
   - remaining risks and blockers
```
