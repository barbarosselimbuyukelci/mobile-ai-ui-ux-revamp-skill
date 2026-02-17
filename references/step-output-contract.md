# Step Output Contract

## Purpose

Guarantee continuity and memory by storing each workflow step as a file artifact,
not only as conversational output.

## Artifact Root

Use a run-scoped folder:

- `run-artifacts/<run-id>/`

`<run-id>` can be date-time or ticket ID.

## Required Step Artifacts

| step | required_file | minimum content |
|---|---|---|
| 0 | `01-intent-inference.md` | app purpose inference, ordered user operations, evidence paths, confidence |
| 1 | `02-problem-frame.md` | business goal, user goal, primary task, success metrics, constraints |
| 2 | `03-user-task-model.md` | user segments, JTBD/task stories, context constraints, edge scenarios |
| 3 | `04-mobile-flows.md` | IA summary, primary flow, fallback flow, error/empty/recovery paths |
| 4 | `05-screen-specs.md` | screen intents, state matrix, library target block, component mapping |
| 5 | `06-visual-system.md` | typography, color roles, spacing, motion, component token rules |
| 6 | `07-ux-copy.md` | labels, CTA copy, error/success messages, tone rules |
| 7 | `08-quality-gates.md` | accessibility, heuristic, usability-test outputs |
| 8 | `09-handoff-package.md` | implementation guidance, QA acceptance, instrumentation plan |
| 9 | `10-verification.md` | traceability summary, CI gate results, regression outcomes |
| 10 | `11-release-summary.md` | final decisions, residual risks, next actions |

Each required file must include a `## Consistency Keys` section.

## Optional Execution-Agent Artifact

When implementation is delegated to a coding agent, also generate:

- `12-execution-manifest.md`
- `13-architecture-delta-report.md`
- `14-implementation-completeness-matrix.md`
- `15-artifact-intake.md`
- `16-execution-batch-plan.md`
- `17-implementation-change-log.md`

This file should include dependency-ordered implementation batches, quality
targets, and handoff contract references.

Execution gate:

- No code edits before `15-artifact-intake.md` and `16-execution-batch-plan.md`
  are created and linked in execution report.

## Consistency Keys (Mandatory In Every Artifact)

Each step artifact must include a `## Consistency Keys` section with bullet
entries in `key: value` format.

Canonical keys:

- `app_purpose_hypothesis`
- `primary_operation_sequence`
- `platform_runtime`
- `design_system_strategy`
- `ui_library_stack`
- `navigation_model`
- `visual_concept`
- `copy_terminology_contract`

Required minimum per file:

- `01-intent-inference.md`: `app_purpose_hypothesis`, `primary_operation_sequence`
- `04-mobile-flows.md`: `navigation_model`
- `05-screen-specs.md`: `platform_runtime`, `design_system_strategy`, `ui_library_stack`, `navigation_model`
- `06-visual-system.md`: `visual_concept`
- `07-ux-copy.md`: `navigation_model`, `copy_terminology_contract`
- `09-handoff-package.md`: `platform_runtime`, `design_system_strategy`, `ui_library_stack`, `navigation_model`
- `10-verification.md`: `navigation_model`
- `11-release-summary.md`: `navigation_model`, `visual_concept`

## Artifact Precedence And Conflict Resolution

No majority voting across artifacts.

Source-of-truth precedence:

- Product purpose and operation sequence: `01-intent-inference.md`
- User/task constraints: `03-user-task-model.md`
- IA and navigation model: `04-mobile-flows.md`
- Platform/design-system/library target: `05-screen-specs.md`
- Visual concept and tokens: `06-visual-system.md`
- Terminology and UX copy: `07-ux-copy.md`

If downstream artifact conflicts with upstream source:

1. Do not implement from conflicting downstream artifact.
2. Correct upstream source if intent changed.
3. Regenerate all dependent downstream artifacts.
4. Record the change in execution report notes.

## Dependency Rule

Each step file must reference inputs from prior files it depends on.
Example:

- `04-mobile-flows.md` must cite `02-problem-frame.md` and `03-user-task-model.md`.
- `05-screen-specs.md` and `07-ux-copy.md` must remain aligned with
  `04-mobile-flows.md` for navigation decisions.

## Completion Rule

A step is complete only when:

- its required file exists
- minimum sections are present
- execution report links the artifact path

## Validation Rule

Before final response, verify:

- all required files exist for executed steps
- execution report `artifact/output` paths are populated
- no step is marked complete without an artifact
- consistency keys are present for required files
- `python scripts/check_artifact_consistency.py <run-artifacts/run-id>` passes
- `python scripts/check_execution_readiness.py <run-artifacts/run-id>` passes for implementation runs
