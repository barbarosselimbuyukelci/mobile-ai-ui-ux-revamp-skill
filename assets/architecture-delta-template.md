# Architecture Delta Report Template

Use this when UX requirements need architectural changes.

| requirement_id | requirement_summary | current_limit | required_architecture_change | migration_plan | rollback_plan | owner | decision_status | notes |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | Example: Offline scan queue sync | No persistent queue | Add durable queue + retry worker | Add queue model, migrate pending items, phase rollout | Feature flag rollback to current behavior | mobile-tech-lead | approved | |

## Rules

- `decision_status` one of: `approved`, `pending`, `blocked`
- Include one row for each architecture-impact requirement
- Do not mark requirement complete without a decision path
