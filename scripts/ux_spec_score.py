#!/usr/bin/env python3
"""
Score a markdown UX spec against this skill's mandatory quality criteria.
"""

import argparse
import sys
from pathlib import Path
from typing import List, Optional, Tuple


CHECKS = [
    (
        "problem_framing",
        4,
        ["business goal", "user goal", "success metric"],
    ),
    (
        "concept_layer",
        4,
        ["concept layer", "experience", "visual direction"],
    ),
    (
        "production_layer",
        4,
        ["production layer", "screen", "flow"],
    ),
    (
        "mobile_scope",
        4,
        ["mobile", "ios", "android"],
    ),
    (
        "flow_coverage",
        4,
        ["happy path", "fallback", "error"],
    ),
    (
        "state_coverage",
        4,
        ["loading", "empty", "success", "offline"],
    ),
    (
        "accessibility_gate",
        9,
        ["wcag", "focus", "screen reader", "touch target"],
    ),
    (
        "heuristic_gate",
        5,
        ["heuristic", "score", "severity"],
    ),
    (
        "usability_test_gate",
        5,
        ["usability test", "task completion", "time on task"],
    ),
    (
        "explainability",
        5,
        ["what the ai", "why", "override"],
    ),
    (
        "agentic_ux",
        5,
        ["agent", "handoff", "human"],
    ),
    (
        "library_target",
        4,
        [
            "library target",
            "platform runtime",
            "design system",
            "ui library",
            "swiftui",
            "jetpack compose",
            "react native paper",
            "flutter",
        ],
    ),
    (
        "component_mapping",
        4,
        [
            "component mapping",
            "generic intent",
            "library component",
            "required props",
            "state handling",
        ],
    ),
    (
        "code_intent_inference",
        7,
        [
            "app purpose inference",
            "code-derived intent",
            "evidence paths",
            "confidence",
        ],
    ),
    (
        "ordered_operations_and_ux_rules",
        6,
        [
            "ordered user operations",
            "ux sequencing rule",
            "open",
            "discover",
            "act",
            "verify",
            "manage",
        ],
    ),
    (
        "traceability_matrix",
        4,
        [
            "traceability matrix",
            "spec item",
            "test case",
            "code path",
            "ci result",
        ],
    ),
    (
        "ci_quality_gates",
        4,
        [
            "ci quality-gate",
            "golden-flow",
            "state coverage",
            "visual regression",
            "accessibility",
        ],
    ),
    (
        "execution_continuity",
        4,
        [
            "execution mode",
            "uninterrupted pass",
            "do not stop",
            "what next",
            "hard blocker",
            "step 0",
            "step 10",
        ],
    ),
    (
        "method_selection_policy",
        4,
        [
            "method selection policy",
            "default methods",
            "do not ask the user to choose methodology",
            "jtbd",
            "state-first",
            "token-first",
        ],
    ),
    (
        "validation_timing_policy",
        4,
        [
            "validation timing policy",
            "do not run scoring",
            "step 0",
            "post step 8",
            "step 9",
            "never run score scripts immediately after step 0",
        ],
    ),
    (
        "step_output_contract",
        1,
        [
            "step output contract",
            "run-artifacts/<run-id>/",
            "required step artifacts",
            "execution report",
            "do not mark any step complete without its artifact",
            "consistency keys",
            "cross-artifact consistency",
        ],
    ),
    (
        "planning_horizon_policy",
        1,
        [
            "planning horizon policy",
            "immediate implementation",
            "do not output week-by-week",
            "unless user explicitly requests timeline planning",
        ],
    ),
    (
        "design_direction_alignment",
        2,
        [
            "design direction alignment policy",
            "2 to 3 design direction options",
            "recommended default option",
            "one concise alignment question",
        ],
    ),
    (
        "execution_agent_handoff",
        2,
        [
            "execution agent handoff",
            "build_execution_manifest.py",
            "12-execution-manifest.md",
            "execution-agent-playbook",
            "execution-agent-prompt-template",
            "never silently skip",
            "13-architecture-delta-report.md",
            "14-implementation-completeness-matrix.md",
            "check_implementation_completeness.py",
            "check_artifact_consistency.py",
            "15-artifact-intake.md",
            "16-execution-batch-plan.md",
            "17-implementation-change-log.md",
            "check_execution_readiness.py",
        ],
    ),
]


def has_keywords(text: str, keywords: List[str], min_hits: Optional[int] = None) -> bool:
    hits = sum(1 for keyword in keywords if keyword in text)
    if min_hits is None:
        min_hits = max(1, len(keywords) // 2)
    return hits >= min_hits


def score_content(content: str) -> Tuple[int, List[Tuple[str, int, bool]]]:
    text = content.lower()
    total = 0
    results = []
    for name, points, keywords in CHECKS:
        passed = has_keywords(text, keywords)
        if passed:
            total += points
        results.append((name, points, passed))
    return total, results


def load_content(path: Path) -> Tuple[str, str]:
    if path.is_file():
        return path.read_text(encoding="utf-8", errors="ignore"), str(path)

    if not path.is_dir():
        raise ValueError("Path must be a markdown file or directory.")

    md_files = sorted(
        [p for p in path.rglob("*.md") if p.is_file()],
        key=lambda p: str(p.relative_to(path)).lower(),
    )
    if not md_files:
        raise ValueError("Directory contains no markdown files (*.md).")

    sections = []
    for md_file in md_files:
        rel = md_file.relative_to(path)
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        sections.append("## FILE: {0}\n\n{1}".format(rel, text))
    combined = "\n\n".join(sections)
    target = "{0} (combined {1} markdown files)".format(path, len(md_files))
    return combined, target


def main() -> int:
    parser = argparse.ArgumentParser(description="Score a UX markdown spec.")
    parser.add_argument("spec_path", help="Path to markdown spec file or artifact directory")
    parser.add_argument("--min-score", type=int, default=80, help="Minimum passing score")
    args = parser.parse_args()

    path = Path(args.spec_path)
    if not path.exists():
        print(f"ERROR: File not found: {path}")
        return 2

    try:
        content, target = load_content(path)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    score, results = score_content(content)

    print(f"Spec: {target}")
    print(f"Score: {score}/100")
    print(f"Threshold: {args.min_score}")
    print("")
    for name, points, passed in results:
        status = "PASS" if passed else "FAIL"
        print(f"- {name}: {status} ({points} pts)")

    if score >= args.min_score:
        print("\nResult: PASS")
        return 0

    print("\nResult: FAIL")
    return 1


if __name__ == "__main__":
    sys.exit(main())
