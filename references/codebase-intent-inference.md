# Codebase Intent Inference

## Table Of Contents

1. Goal
2. Inputs
3. Inference procedure
4. UX sequencing rules
5. Confidence and evidence policy
6. Output contract

## Goal

Infer what the app is for and what users can do, directly from code evidence.

Target output:

- App purpose statement
- Ordered user operations
- Operation-level UX rule mapping
- Code evidence list for each claim

## Inputs

Scan these evidence types first:

- Route definitions and navigation graph
- Screen/page names and component trees
- Authentication and role guards
- API endpoints and domain models
- Error/loading/empty/success UI handling
- Analytics events and action names

## Inference Procedure

1. Detect runtime and stack from dependencies and folder conventions.
2. Build screen inventory from route declarations and page components.
3. Build transition map from navigation calls and route links.
4. Extract domain nouns and verbs from identifiers, copy, and endpoint names.
5. Infer primary jobs from most connected flows and repeated action verbs.
6. Derive ordered operations from entrypoint to confirmation and management loops.
7. Attach confidence per claim and link evidence paths.

Use fast file search patterns where available:

- Route keywords: `route`, `router`, `navigate`, `NavHost`, `go_router`, `NavigationStack`
- Auth keywords: `login`, `signup`, `token`, `session`, `auth`
- Action keywords: `checkout`, `book`, `create`, `submit`, `pay`, `confirm`
- State keywords: `loading`, `empty`, `error`, `success`, `retry`

## UX Sequencing Rules

When ordering operations, enforce:

1. Purpose first: first action should orient the user to core value.
2. Shortest viable path: minimize steps to first successful outcome.
3. Progressive disclosure: defer advanced options until needed.
4. Trust checkpoints: show state, rationale, and reversibility for risky actions.
5. Recovery guarantees: every critical failure point must expose next action.
6. Continuity: preserve user progress across interruption when feasible.

## Confidence And Evidence Policy

For every inferred claim:

- Include confidence: `high`, `medium`, or `low`
- Include at least one code reference path
- Mark assumptions explicitly when evidence is incomplete

Do not present low-confidence claims as facts.

## Output Contract

Always output these sections:

1. App purpose inference
2. Ordered user operations
3. UX rule mapping per operation
4. Evidence table (claim -> file reference -> confidence)
5. Gaps and unknowns
