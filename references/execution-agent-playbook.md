# Execution Agent Playbook

## Purpose

Execute UX revamp artifacts into working code with minimal ambiguity.

## Inputs

Required artifact set from design run:

- `01-intent-inference.md`
- `02-problem-frame.md`
- `03-user-task-model.md`
- `04-mobile-flows.md`
- `05-screen-specs.md`
- `06-visual-system.md`
- `07-ux-copy.md`
- `08-quality-gates.md`
- `09-handoff-package.md`
- `10-verification.md`
- `11-release-summary.md`
- `12-execution-manifest.md` (generated handoff manifest)

## Execution Rules

1. Do not start coding before preflight intake and batch plan artifacts are created.
2. Implement batches in dependency order.
3. Do not redesign from scratch unless artifacts conflict with code reality.
4. Keep library target and component mapping consistent with spec.
5. Run cross-artifact consistency check before coding.
6. Update traceability matrix during implementation, not after.
7. Run tests and quality gates before claiming completion.
8. Never silently skip a requirement because it needs architecture changes.
9. If a planning skill/agent exists in the runtime, delegate planning first and attach its output.

## Mandatory Preflight (Before Any Code Edit)

Create:

- `15-artifact-intake.md`: artifact-by-artifact read notes, extracted decisions, risk map
- `16-execution-batch-plan.md`: dependency-ordered batches, requirement mapping, validation plan

Hard gate:

- No code edits until both files exist.
- If planning skill/agent is available, use it for `16-execution-batch-plan.md`.

## Batch Model

- Batch A: foundation and navigation scaffolding
- Batch B: primary flows and core screens
- Batch C: states, copy, and accessibility
- Batch D: regression checks and verification evidence

## Required Outputs

- Updated code changes
- Updated traceability matrix
- `13-architecture-delta-report.md` when structural changes are needed
- `14-implementation-completeness-matrix.md` for all design requirements
- `15-artifact-intake.md` proving artifacts were read
- `16-execution-batch-plan.md` proving planned execution path
- `17-implementation-change-log.md` mapping each batch to changed files and req IDs
- Test results summary
- Validation results for:
  - E2E golden flow
  - state coverage
  - accessibility checks
  - visual regression (if available)

## Failure Handling

If implementation conflicts with artifacts:

- Record conflict
- Propose minimal correction
- Continue with safest implementable path
- Mark assumption and risk explicitly
- Regenerate dependent artifacts after source-of-truth correction

Consistency check command:

`python scripts/check_artifact_consistency.py <run-artifacts/run-id>`

Execution readiness check command:

`python scripts/check_execution_readiness.py <run-artifacts/run-id>`

If requirement cannot be implemented in current batch:

- Mark as `blocked` or `deferred` in completeness matrix
- Add evidence and owner
- Add required architectural path in architecture delta report
