# Architecture Delta Guidelines

## Purpose

Prevent silent feature drops when UX requirements need architectural changes.

## When To Trigger

Trigger architecture-delta handling when a requirement needs:

- navigation structure rewrite
- state management model change
- data contract or API shape change
- shared component system refactor
- persistence or offline model change
- permission/security model change

## Required Handling

For each impacted requirement:

1. describe current limitation
2. describe target UX behavior
3. define minimum architectural change
4. define migration strategy
5. define risk and rollback
6. define owner and decision status

Do not mark requirement as "done" without an implementation path.

## Output Artifacts

- `13-architecture-delta-report.md`
- `14-implementation-completeness-matrix.md`

## Decision Status

Allowed statuses:

- approved
- pending
- blocked

`blocked` requires explicit reason and next action.
