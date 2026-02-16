# Evaluation And Testing

## Mandatory Gates

All outputs must include:

1. Accessibility gate
2. Heuristic gate
3. Usability testing gate
4. Implementation verification gate

## Heuristic Rubric

Score 1 to 5 with evidence for:

1. System status visibility
2. Match with user mental model
3. User control and freedom
4. Consistency and standards
5. Error prevention
6. Recognition over recall
7. Efficiency of use
8. Minimalist clarity
9. Recovery quality
10. Help and guidance

## Usability Test Plan

Define:

- Target participants
- Top tasks
- Success criteria
- Observation method
- Debrief questions

Track at minimum:

- Task completion rate
- Time on task
- Error frequency
- Confidence rating

## Explainability Validation

Check that users can answer:

- What did the AI do?
- Why did it do that?
- How can I change or reject it?

If users cannot answer these quickly, the design fails trust criteria.

## Agentic Validation

Where agent orchestration exists, verify:

- Agent responsibility boundaries are clear
- Handoff state is preserved
- Human override is always reachable
- Failures map to clear owner and recovery action

## Library Adapter Validation

Verify:

- Platform runtime is explicitly named
- Design system is explicitly named
- UI library stack is explicitly named
- Each key screen includes generic-to-library component mapping

## Code Intent Inference Validation

Verify:

- App purpose statement is present and evidence-backed
- Ordered user operations are present (`open -> discover -> act -> verify -> manage` or equivalent)
- Each operation references UX sequencing rule
- Claims include confidence and code path references

## Implementation Verification Gate

Verify:

- Traceability matrix exists and covers critical requirements
- Every critical requirement has at least one automated test
- Golden-flow E2E suite is green in CI
- State coverage tests include loading, empty, error, success, offline
- Accessibility checks are automated and documented
- Visual regression is enabled for critical screens
- Fail criteria are explicit and block release

## Execution Continuity Validation

Verify:

- Workflow log shows sequential execution from Step 0 to Step 10
- No mid-step "what next" pause occurred without a hard blocker
- Any pause includes blocker reason, question, and fallback assumption

## Method Selection Validation

Verify:

- Default method set was applied automatically when user did not specify method
- No method-choice question interrupted workflow without hard blocker
- Method choices are logged in execution report

## Validation Timing Validation

Verify:

- `ux_spec_score.py` was not run before Step 8 artifacts existed
- `check_traceability.py` was run only when matrix artifact existed
- Early script runs did not block progression to downstream steps

## Step Output Contract Validation

Verify:

- Required step artifact files exist in `run-artifacts/<run-id>/`
- Execution report links each completed step to its artifact file path
- No completed step is missing minimum required sections

## Planning Horizon Validation

Verify:

- Output defaults to immediate implementation batches
- No unsolicited week-by-week or phase timeline was introduced
- If timeline exists, user explicitly requested it and assumptions are documented

## Design Direction Alignment Validation

Verify:

- User received 2 to 3 concrete direction options with tradeoffs
- Recommended default option was stated
- One concise alignment question was asked before direction lock
- If user input was unavailable, fallback assumption was documented
