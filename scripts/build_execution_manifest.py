#!/usr/bin/env python3
"""
Build an implementation-ready execution manifest from run artifacts.
Compatible with Python 3.9+.
"""

import argparse
from pathlib import Path
from typing import Dict, List


REQUIRED = [
    "01-intent-inference.md",
    "02-problem-frame.md",
    "03-user-task-model.md",
    "04-mobile-flows.md",
    "05-screen-specs.md",
    "06-visual-system.md",
    "07-ux-copy.md",
    "08-quality-gates.md",
    "09-handoff-package.md",
    "10-verification.md",
    "11-release-summary.md",
]


def detect_stack(files: Dict[str, str]) -> str:
    text = "\n".join(files.values()).lower()
    if "react native" in text:
        return "React Native"
    if "flutter" in text:
        return "Flutter"
    if "swiftui" in text or "uikit" in text:
        return "iOS Native"
    if "jetpack compose" in text or "android views" in text:
        return "Android Native"
    return "Unknown (check 01/05 artifacts)"


def short_extract(markdown: str, label: str, limit: int = 240) -> str:
    idx = markdown.lower().find(label.lower())
    if idx < 0:
        return "Not found"
    snippet = markdown[idx : idx + limit].replace("\n", " ").strip()
    return snippet


def build_manifest(artifact_dir: Path, files: Dict[str, str]) -> str:
    stack = detect_stack(files)
    intent = short_extract(files.get("01-intent-inference.md", ""), "Purpose statement")
    flows = short_extract(files.get("04-mobile-flows.md", ""), "flow")
    quality = short_extract(files.get("08-quality-gates.md", ""), "heuristic")

    lines: List[str] = []
    lines.append("# Execution Manifest")
    lines.append("")
    lines.append("## Metadata")
    lines.append("")
    lines.append(f"- Artifact directory: {artifact_dir}")
    lines.append(f"- Detected stack: {stack}")
    lines.append(f"- Intent summary: {intent}")
    lines.append("")
    lines.append("## Source Artifacts")
    lines.append("")
    for name in REQUIRED:
        status = "present" if name in files else "missing"
        lines.append(f"- {name}: {status}")
    lines.append("")
    lines.append("## Implementation Batches")
    lines.append("")
    lines.append("### Batch A: Foundation")
    lines.append("- Apply navigation and shell structure from `04-mobile-flows.md`.")
    lines.append("- Apply global tokens/theming rules from `06-visual-system.md`.")
    lines.append("- Align library/component constraints from `05-screen-specs.md`.")
    lines.append("")
    lines.append("### Batch B: Core Flows")
    lines.append("- Implement primary user journey screens from `05-screen-specs.md`.")
    lines.append("- Implement state behavior: loading, empty, error, success, offline.")
    lines.append("- Integrate critical microcopy from `07-ux-copy.md`.")
    lines.append("")
    lines.append("### Batch C: Quality Hardening")
    lines.append("- Apply accessibility fixes listed in `08-quality-gates.md`.")
    lines.append("- Resolve heuristic/usability issues with high severity first.")
    lines.append("- Confirm copy consistency and interaction feedback behavior.")
    lines.append("")
    lines.append("### Batch D: Verification")
    lines.append("- Update traceability matrix with implemented code paths.")
    lines.append("- Run CI quality gates and collect outputs.")
    lines.append("- Produce final verification summary in `10-verification.md`.")
    lines.append("")
    lines.append("## Quality Targets")
    lines.append("")
    lines.append(f"- Quality gate context: {quality}")
    lines.append("- Golden flow test coverage: required")
    lines.append("- State coverage: required")
    lines.append("- Accessibility checks: required")
    lines.append("")
    lines.append("## Mandatory Tracking Artifacts")
    lines.append("")
    lines.append("- 13-architecture-delta-report.md")
    lines.append("- 14-implementation-completeness-matrix.md")
    lines.append("- traceability-matrix.md or csv")
    lines.append("")
    lines.append("## Handoff Contract For Coding Agent")
    lines.append("")
    lines.append("- Follow dependency order. Do not skip batches.")
    lines.append("- Do not request routine approval between batches.")
    lines.append("- Escalate only hard blockers.")
    lines.append("- Keep changes traceable to artifact requirements.")
    lines.append("- Never silently drop requirements. Mark implemented/blocked/deferred explicitly.")
    lines.append("- Use templates: architecture-delta-template.md and implementation-completeness-template.md.")
    lines.append("")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Build execution manifest from artifact folder.")
    parser.add_argument("artifact_dir", help="Path to run-artifacts/<run-id> folder")
    parser.add_argument("--output", help="Output file path (default: <artifact_dir>/12-execution-manifest.md)")
    args = parser.parse_args()

    artifact_dir = Path(args.artifact_dir)
    if not artifact_dir.exists() or not artifact_dir.is_dir():
        print("ERROR: artifact_dir is invalid: {0}".format(artifact_dir))
        return 2

    files: Dict[str, str] = {}
    for name in REQUIRED:
        path = artifact_dir / name
        if path.exists():
            files[name] = path.read_text(encoding="utf-8", errors="ignore")

    if not files:
        print("ERROR: no required artifact files found in {0}".format(artifact_dir))
        return 2

    manifest = build_manifest(artifact_dir, files)
    out = Path(args.output) if args.output else artifact_dir / "12-execution-manifest.md"
    out.write_text(manifest, encoding="utf-8")
    print("Wrote execution manifest: {0}".format(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
