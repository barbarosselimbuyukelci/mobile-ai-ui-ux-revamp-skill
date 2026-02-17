# Workflow Reference

## Table Of Contents

1. Output contract
2. Sequence
3. Mobile constraints
4. Failure modes
5. Done criteria
6. Delivery proof
7. Execution continuity policy
8. Method defaults
9. Validation timing
10. Step output contract
11. Planning horizon policy
12. Design direction alignment checkpoint
13. Execution agent handoff
14. Implementation integrity policy
15. Cross-artifact consistency policy
16. Execution discipline policy

## Output Contract

Always include both layers:

- Concept layer: narrative, interaction concept, visual direction.
- Production layer: flow map, screen specs, component tokens, accessibility, QA.

## Sequence

1. Codebase intent inference (when code exists)
2. Problem framing
3. User and task modeling
4. Mobile IA and flow mapping
5. Screen and state specification
6. Visual system direction
7. UX writing
8. Mandatory quality gates
9. Engineering and QA handoff
10. Implementation verification and CI proof
11. Execution-agent handoff manifest generation

## Mobile Constraints

Always account for:

- One-hand use and reach zones
- Short attention windows and interruptions
- Network instability and offline states
- Small viewport hierarchy
- Touch target reliability

## Failure Modes

Watch for:

- Feature-first flows that bury user intent
- Over-animated interfaces that block speed
- Missing recovery paths in error states
- Inconsistent tone across screens
- Accessibility checks postponed until release

## Done Criteria

A design is done only when:

- Both concept and production layers are complete
- Primary flow and fallback paths are explicit
- Required states are defined per screen
- Accessibility, heuristic, and usability gates are documented
- QA acceptance criteria are testable

## Delivery Proof

A delivery claim is valid only when:

- Traceability matrix maps all critical spec items to tests and code
- Golden-flow E2E tests pass in CI
- State coverage tests pass for loading, empty, error, success, offline
- Accessibility checks pass with automated and manual evidence
- Visual regression checks pass for critical screens

## Execution Continuity Policy

Default behavior:

- Execute Step 0 through Step 10 without asking for mid-step confirmation.
- Do not pause after Step 0 to ask the user what to do next.

Allowed pause:

- Only when a hard blocker prevents continuation (access, credentials, unrecoverable runtime failure, or non-inferable mandatory input).

When paused for blocker:

- Ask one concise blocker question.
- Propose a best-effort default assumption.
- Resume immediately after answer or proceed with stated assumption if no answer.

## Method Defaults

Default method set:

- JTBD + task-flow decomposition for flow design
- State-first screen specification for behavior definition
- Token-first visual system for UI consistency
- Heuristic-first evaluation before usability test planning

Do not ask "which design method should we use?" mid-run unless explicitly requested
or blocked by mandatory external process constraints.

## Validation Timing

Run scripts only at designated stages:

- Step 0: intent inference script
- Post Step 8: spec scoring script
- Step 9: traceability validation script
- Step 9 or Step 10: artifact consistency validation script
- Step 10: execution-readiness validation script

Never run score scripts immediately after Step 0.
Never block progression on early scoring.

## Step Output Contract

Persist each step as a file artifact under a run-scoped folder:

- `run-artifacts/<run-id>/`

Use required filenames and minimum sections from:

- `references/step-output-contract.md`

Do not mark any step complete without its artifact file and execution-report link.
Do not mark the run complete if consistency keys are missing in required artifacts.

## Planning Horizon Policy

Default planning mode:

- immediate implementation batches
- dependency-first ordering
- no unsolicited week-by-week timeline

Only generate weekly or phased rollout plans when the user explicitly asks for
timeline planning.

If timeline is requested, keep implementation details concrete for "now" scope
and mark timeline assumptions clearly.

## Design Direction Alignment Checkpoint

Run one mandatory alignment checkpoint before locking major design direction.

When:

- After user/context modeling
- Before finalizing IA, flow, and visual direction choices

How:

- Present 2 to 3 options
- Show tradeoffs and recommended option
- Ask one concise selection question

If user skips input:

- Use recommended default
- Record assumption in execution report

## Execution Agent Handoff

After design artifacts are complete, generate an execution manifest:

`python scripts/build_execution_manifest.py <run-artifacts/run-id>`

Then hand off to coding agent with:

- `references/execution-agent-playbook.md`
- `assets/execution-agent-prompt-template.md`
- `assets/architecture-delta-template.md`
- `assets/implementation-completeness-template.md`

## Implementation Integrity Policy

Do not silently skip any design requirement during implementation.

If a requirement requires architecture change:

- document it in `13-architecture-delta-report.md`
- track status in `14-implementation-completeness-matrix.md`

A run is incomplete if requirements are missing status or rationale.

## Cross-Artifact Consistency Policy

Consistency is mandatory across all artifacts, not only navigation.

Required behavior:

- Use upstream source-of-truth artifacts for each decision domain.
- Do not resolve conflicts by majority vote across files.
- If a source decision changes, regenerate all dependent artifacts.
- Keep `Consistency Keys` aligned across required files.

Validation command:

`python scripts/check_artifact_consistency.py <run-artifacts/run-id>`

Completion rule:

- Run is incomplete if consistency script fails.

## Execution Discipline Policy

Execution quality requires explicit preflight and plan handoff.

Required behavior before coding:

- Generate `15-artifact-intake.md` proving all artifacts were read.
- Generate `16-execution-batch-plan.md` proving dependency-ordered plan exists.
- If planning skill/agent is available, delegate planning and attach result.
- Do not edit code before preflight and plan artifacts exist.

Required behavior during and after coding:

- Maintain `17-implementation-change-log.md` by batch.
- Validate readiness with:
  `python scripts/check_execution_readiness.py <run-artifacts/run-id>`

Completion rule:

- Run is incomplete if execution-readiness script fails.
