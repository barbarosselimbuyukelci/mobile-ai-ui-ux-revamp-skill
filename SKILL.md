---
name: craft-interface-experience
description: Comprehensive mobile UI and UX design workflow for creating accurate, user-friendly, charming interfaces. Use when an AI agent must deliver both concept direction and production-ready mobile specs, including flows, screen behavior, visual systems, microcopy, accessibility checks, heuristic audits, usability testing plans, and implementation handoff. Tool-agnostic.
---

# Craft Interface Experience

## Overview

Design mobile interfaces that are clear, useful, and emotionally engaging without sacrificing usability, accessibility, or delivery speed.

Produce artifacts that product, design, and engineering teams can implement with minimal ambiguity while preserving a distinctive product feel.

## Design Stance

Use this priority order in every design decision:

1. Usability and task success first.
2. Charm and emotional resonance second.
3. Business outcomes third.

Treat priority 2 and 3 as enablers of priority 1. Do not trade core clarity for style or short-term conversion tricks.

## 2026 Direction

Treat these as strategic design signals and map them to concrete design decisions when relevant:

- Explainable AI
- Agentic UX and human-agent ecosystems
- Dynamic personalized interfaces
- Voice plus touch multimodal interaction
- Micro-interactions as primary feedback language
- AR for practical workflows
- Personalization with privacy boundaries
- Accessibility as foundational quality
- Cross-platform continuity assumptions
- Passwordless and biometric authentication defaults

Read `references/ai-ux-trends-2026.md` for direct implications and checks.

## Scope

Apply this skill to mobile products only:

- Native iOS apps
- Native Android apps
- Cross-platform mobile apps

Do not generate desktop-specific layout assumptions unless explicitly requested as supporting context.

## Required Output Contract

Always return both layers in the same response:

1. Concept layer:
- Experience concept statement
- Interaction concept for main journey
- Visual direction and tone
- Distinctive moments that add charm without blocking task completion

2. Production layer:
- Full mobile flow map
- Screen-by-screen behavior spec
- Library target block (platform, design system, UI library choices)
- Generic-to-library component mapping for each key screen
- Component and token guidance
- Accessibility, QA, and instrumentation requirements

## Library Targeting (Mandatory)

For every production output, explicitly define:

- Platform runtime: `iOS`, `Android`, `React Native`, `Flutter`, `Ionic/Capacitor`, `KMP/Compose Multiplatform`
- Design system: `Material 3`, `Apple HIG`, `Custom`, or mixed strategy with rationale
- UI library stack: concrete package or framework choices

Choose library targets in this order:

1. User-specified stack always wins.
2. Existing codebase evidence (dependencies, component imports, theme files).
3. If no evidence exists, provide 2 to 3 viable stack options and pick a default with explicit rationale.

Use `references/library-catalog.md` first, then load only the relevant ecosystem profile:

- `references/library-profiles/swiftui-uikit.md`
- `references/library-profiles/jetpack-compose-views.md`
- `references/library-profiles/react-native-libraries.md`
- `references/library-profiles/flutter-libraries.md`

## Run This Workflow

1. Infer product intent and user operations from existing codebase (when code exists).
2. Frame the problem.
3. Model users, context, and jobs-to-be-done.
4. Define mobile IA and flow architecture.
5. Specify mobile interactions and state behavior.
6. Build visual system and component guidance.
7. Write UX copy and feedback language.
8. Run mandatory quality gates.
9. Package implementation and QA handoff.
10. Verify implementation with traceability and CI evidence.

## Step 0: Infer Product Intent From Code (Mandatory When Code Exists)

When a codebase is available, derive intent before proposing UX.

Extract and document:

- Code-derived intent summary
- App purpose inference
- App purpose hypothesis: `The app exists to help [user] achieve [outcome]`
- Primary user operations in sequence: `open -> discover -> act -> verify -> manage`
- Supporting operations and edge operations
- Trigger conditions and gating (auth, permissions, role, paywall)
- System feedback behavior (loading/error/empty/success)
- Evidence paths from code paths, routes, screens, and API calls
- Confidence level for each major inference

Use only claims that can be tied to code evidence. Mark uncertain claims explicitly.

Use `references/codebase-intent-inference.md` for the procedure and
`assets/app-intent-inference-template.md` for output format.

When a markdown report is needed, run:

`python scripts/infer_app_intent.py <repo_path>`

## Step 1: Frame The Problem

Collect and confirm:

- Business goal
- User goal
- Primary task
- Success metrics
- Constraints (timeline, mobile platform, legal, technical)
- Non-goals

If code inference exists, align this step with the inferred app purpose and user operations.

If any of these are missing, ask concise follow-up questions before designing.

Use `assets/design-brief-template.md` when the user asks for a design brief or requirements alignment.

## Step 2: Model Users And Context

Define:

- Primary and secondary user segments
- Context of use (mobile device, environment, one-hand constraints, interruptions)
- Critical scenarios and edge scenarios
- Cognitive load constraints and trust sensitivity

Convert this into task stories in this format:

`As a [user], I need to [task], so I can [outcome].`

For deeper guidance, read `references/design-principles.md`.

## Step 3: Define Mobile IA And Flows

Create:

- Content and feature hierarchy
- Mobile navigation model
- Entry points and exits
- Main flow and fallback flow
- Error, empty, and recovery paths

Document each flow with trigger, steps, decision points, success criteria, and failure recovery.

Use `references/interaction-patterns.md` for pattern selection and flow conventions.

## Step 4: Specify Mobile Interactions And States

For each screen or view, define:

- Intent of the screen
- Primary action and secondary actions
- Input controls and validation behavior
- Keyboard and assistive-tech interaction behavior
- Gestures and touch-target behavior
- System states: default, loading, empty, partial, error, success, offline
- AI explainability block: what the AI generated, why it generated it, and how users can override it

Use deterministic rules for state behavior:

- Never hide critical recovery actions in error states.
- Always provide actionable next steps after failures.
- Keep destructive actions explicit and reversible where possible.

Use `assets/screen-spec-template.md` for each key screen.
Include component mapping lines in this format:

`generic_intent -> library_component (required_props/modifiers, state_handling, accessibility_notes)`

## Step 5: Build Visual And Component Direction

Define a coherent visual system:

- Typography scale and hierarchy
- Spacing rhythm
- Color roles (not just color values)
- Elevation and emphasis rules
- Motion principles and timing bands
- Component usage rules and anti-patterns

Prioritize clarity and contrast over ornamental styling.

For detailed system rules, read `references/visual-system.md`.

## Step 6: Write UX Copy

Write concise interface copy for:

- Labels
- Buttons
- Helper text
- Validation errors
- Empty states
- Success confirmation
- Warnings and destructive actions

Require copy to be:

- Specific
- Actionable
- Human
- Consistent in voice and terminology

For language rules and examples, read `references/ux-writing.md`.

## Step 7: Run Mandatory Quality Gates

All gates below are mandatory before final output.

1. Accessibility gate (WCAG 2.2 AA):

- WCAG 2.2 AA contrast and semantics
- Full keyboard navigation
- Visible focus order
- Screen reader naming and announcements
- Touch target and zoom resilience

2. Heuristic gate:

- Run a heuristic evaluation and score each dimension.
- Flag blockers and design risks with severity.

3. Usability testing gate:

- Provide a concrete usability test plan.
- Define top tasks, success metrics, and observation protocol.
- Include expected failure points and recovery checks.

Read `references/accessibility.md` and `references/evaluation-testing.md` for exact checks.

## Step 8: Package Implementation Handoff

Deliver:

- Design rationale
- User flows
- Screen-by-screen behavior specs
- Token and component guidance
- Accessibility notes
- Instrumentation and success metrics
- QA acceptance checklist

Use `assets/ux-qa-checklist.md` to generate acceptance criteria engineers and QA can execute.

## Step 9: Verify Implementation (Mandatory For Delivery Claims)

If a human team or a second coding agent implements the UI, require proof of
implementation quality before declaring success.

Required evidence package:

- Traceability matrix: `spec item -> test case -> code path -> CI result`
- Golden-flow E2E results for the core sequence:
  `open -> discover -> act -> verify -> manage`
- State coverage evidence for `loading, empty, error, success, offline`
- Accessibility automation results and manual spot checks
- Visual regression and interaction regression results
- Post-release instrumentation checks for drop-off and error spikes

Use:

- `references/implementation-verification.md`
- `assets/traceability-matrix-template.md`
- `assets/ci-quality-gates-template.yml`

When a traceability matrix file exists, validate it:

`python scripts/check_traceability.py <matrix.md_or_csv>`

## Quality Gate

Before final response, verify all of the following:

- App purpose is inferred from code evidence (or explicitly marked unavailable).
- Primary user operations are ordered and tied to UX sequencing rules.
- Claims are supported by concrete code references.
- Problem framing is explicit and measurable.
- Both concept and production layers are present.
- Production layer includes explicit library target block.
- Screen specs include generic-to-library component mapping.
- Flow covers happy path plus failure/edge paths.
- Screen behavior includes all major states.
- Copy and visual language are consistent.
- Accessibility requirements are concrete and testable.
- Heuristic evaluation is included.
- Usability testing plan is included.
- Handoff details are specific enough for implementation.
- Traceability matrix is complete and evidence-backed.
- CI quality-gate evidence is present for critical flows and states.
- Golden-flow E2E checks are present.
- Visual and accessibility regression checks are present.

When a detailed markdown spec exists, run:

`python scripts/ux_spec_score.py <spec.md> --min-score 80`

If score is below threshold, revise and re-score.

## Resource Map

Load resources only when needed:

- `references/workflow.md`: End-to-end process, deliverables, and sequencing.
- `references/codebase-intent-inference.md`: Derive app purpose and user operation sequence from code evidence.
- `references/design-principles.md`: UX principles and decision heuristics.
- `references/ai-ux-trends-2026.md`: 2026 AI UX shifts and actionable design implications.
- `references/interaction-patterns.md`: Mobile navigation, form, list, dashboard, and commerce patterns.
- `references/library-catalog.md`: Wide design-system and UI-library catalog plus selection rules.
- `references/library-profiles/swiftui-uikit.md`: iOS library adapter guidance.
- `references/library-profiles/jetpack-compose-views.md`: Android library adapter guidance.
- `references/library-profiles/react-native-libraries.md`: React Native library adapter guidance.
- `references/library-profiles/flutter-libraries.md`: Flutter library adapter guidance.
- `references/visual-system.md`: Typography, color roles, spacing, motion, and component rules.
- `references/accessibility.md`: Inclusive design and WCAG 2.2 AA checks.
- `references/ux-writing.md`: Voice, tone, and microcopy patterns.
- `references/evaluation-testing.md`: Mandatory heuristic review, usability testing, metrics, and acceptance criteria.
- `references/implementation-verification.md`: Traceability, CI gates, and delivery-proof validation.
- `assets/design-brief-template.md`: Reusable project brief template.
- `assets/app-intent-inference-template.md`: Reusable template for code-derived app purpose and ordered operations.
- `assets/screen-spec-template.md`: Reusable single-screen mobile specification template.
- `assets/ux-qa-checklist.md`: Reusable QA checklist for handoff.
- `assets/traceability-matrix-template.md`: Map spec requirements to tests, code, and CI evidence.
- `assets/ci-quality-gates-template.yml`: CI gate skeleton for UX delivery verification.

## Collaboration Rules

- Ask precise follow-up questions only when missing information blocks quality.
- Surface tradeoffs explicitly (speed vs depth, novelty vs familiarity, flexibility vs consistency).
- Keep recommendations evidence-based and tied to user goals and constraints.
- Prefer patterns that reduce user effort and decision fatigue.
- Avoid visual choices that compromise readability, hierarchy, or accessibility.
- Keep tone creative and bold while keeping intent and actions unmistakably clear.
- Stay tool-agnostic unless the user explicitly asks for a specific design tool.
