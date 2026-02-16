# Workflow Reference

## Table Of Contents

1. Output contract
2. Sequence
3. Mobile constraints
4. Failure modes
5. Done criteria
6. Delivery proof

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
