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

## Core Capabilities

- Codebase intent inference with evidence paths and confidence levels
- Continuous Step 0 to Step 10 workflow execution
- Mobile-first UX architecture and state-first screen specs
- Design-system and UI-library mapping across major mobile stacks
- Accessibility, heuristic, and usability gates
- Traceability matrix and CI quality-gate validation
- Step output contract with file-based run memory

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

## Validation Scripts

Run these at the right stage:

```bash
python scripts/infer_app_intent.py <repo_path>
python scripts/ux_spec_score.py <spec.md> --min-score 80
python scripts/check_traceability.py <matrix.md_or_csv>
```

## Artifact Memory Model

Use a run folder:

`run-artifacts/<run-id>/`

Each step must write its own output artifact. See:

- `references/step-output-contract.md`
- `assets/execution-report-template.md`

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
