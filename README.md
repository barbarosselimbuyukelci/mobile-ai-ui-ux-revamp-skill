# Mobile AI UI UX Revamp Skill

Build production-ready mobile UX revamps with one continuous workflow.

This skill is designed for AI agents that need to analyze an existing codebase, infer product intent, design a full UX system, map design decisions to real UI libraries, and verify delivery quality with traceability and CI gates.

## Why This Skill Exists

Most AI design flows stop too early.

- They generate abstract ideas with weak implementation links.
- They ask too many method questions mid-run.
- They run scoring too early and stall execution.
- They fail to keep durable memory across long revamp sessions.

This skill fixes that with strict execution rules, artifact-based memory, and validation timing.

## 2026 Trend Alignment

This skill is built to track and operationalize 2026 UX direction.

- Explainable AI by default with what/why/override patterns
- Agentic UX with role boundaries, handoffs, and human takeover points
- Dynamic interface generation with constraints, safety rails, and evaluation criteria
- Voice plus touch multimodal interaction patterns
- Micro-interactions as core feedback language, not decoration
- Personalization with privacy boundaries and explicit user control
- Accessibility as a foundational quality gate
- Passwordless and biometric-first flow assumptions

Trend coverage is baked into workflow rules and references, especially:

- `references/ai-ux-trends-2026.md`
- `references/design-principles.md`
- `references/evaluation-testing.md`

Attribution note:

- This trend framing also references: "10 UX Design Shifts You Can't Ignore in 2026"  
  https://uxdesign.cc/10-ux-design-shifts-you-cant-ignore-in-2026-8f0da1c6741d

## Core Capabilities

- Codebase intent inference with evidence paths and confidence levels
- Continuous Step 0 to Step 10 workflow execution
- Mobile-first UX architecture and state-first screen specs
- Design-system and UI-library mapping across major mobile stacks
- Accessibility, heuristic, and usability gates
- Traceability matrix and CI quality-gate validation
- Step output contract with file-based run memory
- No silent requirement drops during implementation

## Product Strategy Layer (PM Mode)

This skill does not jump directly into screens.
It starts like a strong product manager and builds design from product logic.

For each run, it defines:

- Product objective and user outcome
- North-star and supporting success metrics
- Constraints (platform, legal, engineering, timeline)
- Assumptions and risks
- Explicit non-goals

The result is a decision baseline that prevents random UI changes.

Before major direction lock, the skill runs a short alignment checkpoint:

- 2 to 3 direction options
- clear tradeoffs
- one recommended option
- one concise question to capture your preference

## Target Audience Modeling

The skill "imagines" target users through structured modeling, not guesswork.

It builds:

- Primary and secondary user segments
- Context of use (when, where, interruption level, urgency)
- Capability differences (novice, regular, power user)
- Trust and cognitive load risks

Each audience claim is tied to code evidence or clearly marked as an assumption.

## User Story Generation

The skill produces executable product stories before visual design.

Primary format:

`As a [user], I need to [task], so I can [outcome].`

Optional high-precision format for complex flows:

`When [context], I want to [action], so I can [benefit].`

Every critical story gets:

- Priority level
- Flow position (`open`, `discover`, `act`, `verify`, `manage`)
- Success signal
- Failure and recovery expectation

## Design Decision Engine

Design decisions are made through a transparent chain:

1. Codebase evidence and current behavior
2. Product goal and user story impact
3. Platform conventions and library constraints
4. Accessibility and trust requirements
5. 2026 trend alignment

For major decisions, the skill documents:

- Decision statement
- Options considered
- Selected option
- Why it was selected
- Tradeoffs
- Metric impact hypothesis

This keeps design review objective and implementation-friendly.

## What You Get Per Run

In addition to final specs, each run produces durable artifacts:

- Intent inference report
- Product framing and audience model
- User stories and flow architecture
- Screen-level specs with state behavior
- Visual system and UX writing package
- Quality gate reports
- Traceability and CI verification evidence

See:

- `references/step-output-contract.md`
- `assets/execution-report-template.md`

## Workflow At A Glance

1. Infer app purpose and user operations from code
2. Frame the problem and goals
3. Model users and task context
4. Define mobile IA and flow logic
5. Specify screen behavior and states
6. Build visual system direction
7. Craft UX writing
8. Run mandatory quality gates
9. Package handoff artifacts
10. Verify implementation with CI and traceability evidence

Default delivery style:

- Immediate implementation batches
- Dependency-first ordering
- No week-by-week roadmap unless user explicitly requests timeline planning

## Validation Scripts

Run these at the right stage:
Compatible with Python 3.9+.

```bash
python scripts/infer_app_intent.py <repo_path>
python scripts/ux_spec_score.py <spec.md_or_artifact_dir> --min-score 80
python scripts/check_traceability.py <matrix.md_or_csv>
python scripts/build_execution_manifest.py <run-artifacts/run-id>
python scripts/check_implementation_completeness.py <matrix.md_or_csv>
```

## Artifact Memory Model

Use a run folder:

`run-artifacts/<run-id>/`

Each step must write its own output artifact. See:

- `references/step-output-contract.md`
- `assets/execution-report-template.md`

## Execution Agent Setup

After design artifacts are ready, generate a coding handoff manifest:

```bash
python scripts/build_execution_manifest.py run-artifacts/<run-id>
```

Then execute with:

- `references/execution-agent-playbook.md`
- `assets/execution-agent-prompt-template.md`
- `assets/architecture-delta-template.md`
- `assets/implementation-completeness-template.md`

This lets a second coding agent move directly from design artifacts to
dependency-ordered implementation batches.

## Library Coverage

The skill supports broad mobile ecosystems:

- iOS: SwiftUI, UIKit
- Android: Jetpack Compose, Views + Material
- React Native: Paper, NativeBase, UI Kitten, Tamagui, GlueStack, more
- Flutter: Material, Cupertino, hybrid strategies
- Hybrid: Ionic/Capacitor, KMP/Compose Multiplatform

## Repo Structure

```text
SKILL.md
agents/openai.yaml
assets/
references/
scripts/
```

## How To Use In Claude Code

Copy this folder into your project skills path:

```bash
mkdir -p .claude/skills
cp -R mobile-ai-ui-ux-revamp-skill .claude/skills/
```

Then invoke it explicitly in your prompt:

`Use $mobile-ai-ui-ux-revamp-skill and run a full mobile UI/UX revamp in continuous mode.`

## How To Use In Codex

Reference the skill by name in your request and require continuous execution with artifact outputs.

## License

Use freely for internal and commercial UX revamp workflows.
