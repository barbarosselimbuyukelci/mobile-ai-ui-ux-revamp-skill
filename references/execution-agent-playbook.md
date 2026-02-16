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

1. Implement batches in dependency order.
2. Do not redesign from scratch unless artifacts conflict with code reality.
3. Keep library target and component mapping consistent with spec.
4. Update traceability matrix during implementation, not after.
5. Run tests and quality gates before claiming completion.
6. Never silently skip a requirement because it needs architecture changes.

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

If requirement cannot be implemented in current batch:

- Mark as `blocked` or `deferred` in completeness matrix
- Add evidence and owner
- Add required architectural path in architecture delta report
