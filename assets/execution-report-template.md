# Execution Report Template

Use this file to record continuous workflow execution.

## Run Metadata

- Project/repo:
- Date:
- Agent:
- Mode: Continuous execution (Step 0 to Step 10)
- Artifact root: run-artifacts/<run-id>/
- Planning mode: Immediate implementation (default)

## Step Status Log

| step | title | status | artifact/output | blocker | notes |
|---|---|---|---|---|---|
| 0 | Codebase intent inference | pending |  |  |  |
| 1 | Problem framing | pending |  |  |  |
| 2 | User and context modeling | pending |  |  |  |
| 3 | Mobile IA and flow mapping | pending |  |  |  |
| 4 | Screen and state specification | pending |  |  |  |
| 5 | Visual system direction | pending |  |  |  |
| 6 | UX writing | pending |  |  |  |
| 7 | Mandatory quality gates | pending |  |  |  |
| 8 | Handoff packaging | pending |  |  |  |
| 9 | Implementation verification | pending |  |  |  |
| 10 | Final validation and release summary | pending |  |  |  |

## Blocker Log (Only If Needed)

| step | blocker_reason | question_asked | fallback_assumption | resolution |
|---|---|---|---|---|

## Method Selection Log

| area | method_selected | source (default/user-mandated) | reason |
|---|---|---|---|
| flow design | JTBD + task-flow decomposition | default | |
| screen behavior | state-first specification | default | |
| visual system | token-first system | default | |
| evaluation | heuristic-first + usability plan | default | |

## Validation Timing Log

| script | intended_step | actual_step | status | notes |
|---|---|---|---|---|
| scripts/infer_app_intent.py | 0 |  | pending | |
| scripts/ux_spec_score.py | 8+ |  | pending | |
| scripts/check_traceability.py | 9 |  | pending | |

## Planning Horizon Log

| item | status | notes |
|---|---|---|
| Immediate implementation batches provided | pending | |
| Week-by-week/phase timeline added | pending | Only if explicitly requested |

## Design Direction Alignment Log

| item | status | notes |
|---|---|---|
| Options presented (2 to 3) | pending | |
| Tradeoffs documented | pending | |
| Recommended option stated | pending | |
| User alignment response captured | pending | |
| Fallback assumption documented (if no response) | pending | |

## Final Verification

- [ ] Continuous execution confirmed
- [ ] Any blockers documented with fallback assumptions
- [ ] No mid-run method-choice interruption without hard blocker
- [ ] Validation scripts run at correct steps
- [ ] Step output contract satisfied for completed steps
- [ ] Design direction alignment checkpoint completed or explicitly skipped
- [ ] Required artifacts produced
- [ ] Quality gates passed
