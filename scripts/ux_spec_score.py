#!/usr/bin/env python3
"""
Score a markdown UX spec against this skill's mandatory quality criteria.
"""

import argparse
import sys
from pathlib import Path


CHECKS = [
    (
        "problem_framing",
        5,
        ["business goal", "user goal", "success metric"],
    ),
    (
        "concept_layer",
        5,
        ["concept layer", "experience", "visual direction"],
    ),
    (
        "production_layer",
        7,
        ["production layer", "screen", "flow"],
    ),
    (
        "mobile_scope",
        5,
        ["mobile", "ios", "android"],
    ),
    (
        "flow_coverage",
        7,
        ["happy path", "fallback", "error"],
    ),
    (
        "state_coverage",
        5,
        ["loading", "empty", "success", "offline"],
    ),
    (
        "accessibility_gate",
        9,
        ["wcag", "focus", "screen reader", "touch target"],
    ),
    (
        "heuristic_gate",
        7,
        ["heuristic", "score", "severity"],
    ),
    (
        "usability_test_gate",
        7,
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
        6,
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
        6,
        [
            "ci quality-gate",
            "golden-flow",
            "state coverage",
            "visual regression",
            "accessibility",
        ],
    ),
]


def has_keywords(text: str, keywords: list[str], min_hits: int | None = None) -> bool:
    hits = sum(1 for keyword in keywords if keyword in text)
    if min_hits is None:
        min_hits = max(1, len(keywords) // 2)
    return hits >= min_hits


def score_content(content: str) -> tuple[int, list[tuple[str, int, bool]]]:
    text = content.lower()
    total = 0
    results = []
    for name, points, keywords in CHECKS:
        passed = has_keywords(text, keywords)
        if passed:
            total += points
        results.append((name, points, passed))
    return total, results


def main() -> int:
    parser = argparse.ArgumentParser(description="Score a UX markdown spec.")
    parser.add_argument("spec_path", help="Path to markdown spec file")
    parser.add_argument("--min-score", type=int, default=80, help="Minimum passing score")
    args = parser.parse_args()

    path = Path(args.spec_path)
    if not path.exists():
        print(f"ERROR: File not found: {path}")
        return 2

    content = path.read_text(encoding="utf-8", errors="ignore")
    score, results = score_content(content)

    print(f"Spec: {path}")
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
