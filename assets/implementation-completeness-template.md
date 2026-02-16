# Implementation Completeness Matrix Template

Track every major design requirement from spec to implementation status.

| requirement_id | design_feature | status | code_path | evidence | architecture_change | reason | owner | decision_date | notes |
|---|---|---|---|---|---|---|---|---|---|
| REQ-001 | Example: Center FAB scan entry | implemented | src/navigation/AppTabs.tsx | PR#123, test TC-E2E-001 | no | | mobile-dev | 2026-02-17 | |
| REQ-002 | Example: Offline recovery state | blocked | | failing test TC-STATE-004 | yes | missing queue persistence layer | mobile-tech-lead | 2026-02-17 | architecture delta required |

## Status Rules

- Allowed `status`: `implemented`, `blocked`, `deferred`
- `blocked` and `deferred` must include:
  - `reason`
  - `owner`
  - `evidence`

## Completeness Rule

No major requirement can be omitted from this matrix.
