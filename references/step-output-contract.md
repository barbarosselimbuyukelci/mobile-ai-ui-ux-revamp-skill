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

## Dependency Rule

Each step file must reference inputs from prior files it depends on.
Example:

- `04-mobile-flows.md` must cite `02-problem-frame.md` and `03-user-task-model.md`.

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
