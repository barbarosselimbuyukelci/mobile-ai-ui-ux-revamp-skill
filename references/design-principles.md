# Design Principles

## Core Principles

1. Optimize for comprehension before decoration.
2. Reduce decision load at every step.
3. Keep actions predictable and reversible.
4. Make system status visible and actionable.
5. Design error recovery as a primary path.
6. Build trust with explainability and control.
7. Keep accessibility first-class.
8. Use personality to support clarity, not replace it.

## Priority Ladder

Apply this ranking:

1. Usability and task success
2. Charm and emotional resonance
3. Business outcomes

Never sacrifice level 1 for level 2 or 3.

## Decision Heuristics

- If confidence is low, use explicit labels and stronger guidance.
- If stakes are high, expose rationale and user control.
- If task is frequent, prioritize speed and gesture ergonomics.
- If flow is complex, split into progressive steps with clear progress.
- If data is dense, improve hierarchy before adding features.

## Explainability Requirements

For AI-driven behavior, always include:

- What the system changed or generated
- Why the system made that recommendation
- Confidence or uncertainty statement when relevant
- User override and correction controls

## Agentic UX Requirements

When multiple agents exist, define:

- Role and scope for each agent
- Handoff triggers and context payload
- Human takeover points
- Error ownership and recovery path
