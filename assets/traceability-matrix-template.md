# Traceability Matrix Template

Use one row per critical requirement.

| requirement_id | requirement_summary | screen_or_flow | given_when_then_id | test_case_id | automated_test_path | code_path | ci_job_name | ci_run_url | status | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| REQ-001 | Example: User can complete checkout | checkout-flow | GWT-001 | TC-E2E-001 | tests/e2e/checkout.spec.ts | src/features/checkout/CheckoutScreen.tsx | e2e-mobile | https://ci.example/run/123 | pass | |

## Rules

- `status` must be one of: `pass`, `fail`, `blocked`, `not_run`.
- All `REQ-*` with critical severity must map to at least one automated test.
- `ci_run_url` must reference the exact run used for release evidence.
