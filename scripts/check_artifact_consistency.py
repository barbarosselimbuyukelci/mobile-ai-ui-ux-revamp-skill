#!/usr/bin/env python3
"""
Validate cross-artifact consistency in run-artifacts output.
Compatible with Python 3.9+.
"""

import argparse
import re
from pathlib import Path
from typing import Dict, List, Set


REQUIRED_ARTIFACTS = [
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

REQUIRED_KEYS_BY_FILE: Dict[str, Set[str]] = {
    "01-intent-inference.md": {"app_purpose_hypothesis", "primary_operation_sequence"},
    "04-mobile-flows.md": {"navigation_model"},
    "05-screen-specs.md": {
        "platform_runtime",
        "design_system_strategy",
        "ui_library_stack",
        "navigation_model",
    },
    "06-visual-system.md": {"visual_concept"},
    "07-ux-copy.md": {"navigation_model", "copy_terminology_contract"},
    "09-handoff-package.md": {
        "platform_runtime",
        "design_system_strategy",
        "ui_library_stack",
        "navigation_model",
    },
    "10-verification.md": {"navigation_model"},
    "11-release-summary.md": {"navigation_model", "visual_concept"},
}

CRITICAL_KEYS = [
    "app_purpose_hypothesis",
    "primary_operation_sequence",
    "platform_runtime",
    "design_system_strategy",
    "ui_library_stack",
    "navigation_model",
    "visual_concept",
    "copy_terminology_contract",
]

KEY_ALIASES: Dict[str, str] = {
    "app purpose hypothesis": "app_purpose_hypothesis",
    "app_purpose_hypothesis": "app_purpose_hypothesis",
    "primary operation sequence": "primary_operation_sequence",
    "primary_operation_sequence": "primary_operation_sequence",
    "platform runtime": "platform_runtime",
    "platform_runtime": "platform_runtime",
    "design system strategy": "design_system_strategy",
    "design_system_strategy": "design_system_strategy",
    "ui library stack": "ui_library_stack",
    "ui_library_stack": "ui_library_stack",
    "navigation model": "navigation_model",
    "navigation_model": "navigation_model",
    "visual concept": "visual_concept",
    "visual_concept": "visual_concept",
    "copy terminology contract": "copy_terminology_contract",
    "copy_terminology_contract": "copy_terminology_contract",
}


def normalize_key(raw: str) -> str:
    key = re.sub(r"[\s\-]+", "_", raw.strip().lower())
    return KEY_ALIASES.get(key, KEY_ALIASES.get(raw.strip().lower(), key))


def normalize_value(key: str, raw: str) -> str:
    value = raw.strip().lower()
    value = re.sub(r"\s+", " ", value)
    if key == "primary_operation_sequence":
        value = value.replace(" -> ", "->").replace(" - > ", "->")
        value = value.replace("\u2192", "->")
    return value


def extract_consistency_keys(text: str) -> Dict[str, str]:
    lines = text.splitlines()
    in_section = False
    keys: Dict[str, str] = {}

    for line in lines:
        if re.match(r"^\s{0,3}#{2,3}\s+Consistency Keys\s*$", line.strip(), flags=re.IGNORECASE):
            in_section = True
            continue

        if in_section and re.match(r"^\s{0,3}#{1,6}\s+\S+", line.strip()):
            break

        if not in_section:
            continue

        bullet_match = re.match(r"^\s*[-*]\s*([^:]+):\s*(.+?)\s*$", line)
        if not bullet_match:
            continue

        raw_key = bullet_match.group(1)
        raw_value = bullet_match.group(2)
        key = normalize_key(raw_key)
        if key in CRITICAL_KEYS:
            keys[key] = normalize_value(key, raw_value)

    return keys


def load_artifacts(artifact_dir: Path) -> Dict[str, str]:
    files: Dict[str, str] = {}
    for name in REQUIRED_ARTIFACTS:
        path = artifact_dir / name
        if path.exists():
            files[name] = path.read_text(encoding="utf-8", errors="ignore")
    return files


def validate_required_files(files: Dict[str, str], allow_missing: bool) -> List[str]:
    issues: List[str] = []
    if allow_missing:
        return issues

    for name in REQUIRED_ARTIFACTS:
        if name not in files:
            issues.append("Missing required artifact: {0}".format(name))
    return issues


def validate_required_keys(parsed: Dict[str, Dict[str, str]]) -> List[str]:
    issues: List[str] = []
    for filename, required_keys in REQUIRED_KEYS_BY_FILE.items():
        if filename not in parsed:
            continue
        found = parsed[filename]
        missing = sorted([k for k in required_keys if not found.get(k)])
        if missing:
            issues.append(
                "{0}: missing Consistency Keys -> {1}".format(filename, ", ".join(missing))
            )
    return issues


def validate_value_consistency(parsed: Dict[str, Dict[str, str]]) -> List[str]:
    issues: List[str] = []
    for key in CRITICAL_KEYS:
        values_by_file: Dict[str, str] = {}
        for filename, keys in parsed.items():
            value = keys.get(key, "").strip()
            if value:
                values_by_file[filename] = value

        distinct = sorted(set(values_by_file.values()))
        if len(distinct) > 1:
            details = "; ".join(
                "{0}='{1}'".format(filename, value)
                for filename, value in sorted(values_by_file.items())
            )
            issues.append("Cross-artifact conflict for '{0}': {1}".format(key, details))
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate consistency across run artifacts.")
    parser.add_argument("artifact_dir", help="Path to run-artifacts/<run-id> folder")
    parser.add_argument(
        "--allow-missing-artifacts",
        action="store_true",
        help="Skip missing file check (useful for partial runs).",
    )
    args = parser.parse_args()

    artifact_dir = Path(args.artifact_dir)
    if not artifact_dir.exists() or not artifact_dir.is_dir():
        print("ERROR: artifact_dir is invalid: {0}".format(artifact_dir))
        return 2

    files = load_artifacts(artifact_dir)
    if not files:
        print("ERROR: no known artifact files found in {0}".format(artifact_dir))
        return 2

    parsed: Dict[str, Dict[str, str]] = {}
    for filename, text in files.items():
        parsed[filename] = extract_consistency_keys(text)

    issues: List[str] = []
    issues.extend(validate_required_files(files, args.allow_missing_artifacts))
    issues.extend(validate_required_keys(parsed))
    issues.extend(validate_value_consistency(parsed))

    if issues:
        print("Artifact consistency: FAIL")
        for issue in issues:
            print("- {0}".format(issue))
        return 1

    print("Artifact consistency: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
