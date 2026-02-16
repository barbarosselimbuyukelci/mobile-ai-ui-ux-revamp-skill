#!/usr/bin/env python3
"""
Validate a traceability matrix (markdown table or csv) for critical completeness.
"""

import argparse
import csv
from pathlib import Path

REQUIRED_COLUMNS = {
    "requirement_id",
    "requirement_summary",
    "screen_or_flow",
    "given_when_then_id",
    "test_case_id",
    "automated_test_path",
    "code_path",
    "ci_job_name",
    "ci_run_url",
    "status",
}

VALID_STATUS = {"pass", "fail", "blocked", "not_run"}


def parse_markdown_table(text: str) -> list[dict[str, str]]:
    lines = [line.strip() for line in text.splitlines() if line.strip().startswith("|")]
    if len(lines) < 2:
        return []

    header = [col.strip() for col in lines[0].strip("|").split("|")]
    rows = []
    for line in lines[2:]:
        cols = [col.strip() for col in line.strip("|").split("|")]
        if len(cols) != len(header):
            continue
        row = {header[i]: cols[i] for i in range(len(header))}
        rows.append(row)
    return rows


def parse_csv(text: str) -> list[dict[str, str]]:
    reader = csv.DictReader(text.splitlines())
    return [dict((k.strip(), (v or "").strip()) for k, v in row.items()) for row in reader]


def validate_rows(rows: list[dict[str, str]]) -> tuple[bool, list[str]]:
    issues = []
    if not rows:
        return False, ["No traceability rows detected."]

    header_keys = set(rows[0].keys())
    missing = REQUIRED_COLUMNS - header_keys
    if missing:
        issues.append(f"Missing columns: {', '.join(sorted(missing))}")

    critical_rows = [r for r in rows if r.get("requirement_id", "").upper().startswith("REQ-")]
    if not critical_rows:
        issues.append("No REQ-* rows found.")

    for i, row in enumerate(rows, start=1):
        rid = row.get("requirement_id", "").strip()
        status = row.get("status", "").strip().lower()
        test_path = row.get("automated_test_path", "").strip()
        code_path = row.get("code_path", "").strip()
        ci_url = row.get("ci_run_url", "").strip()

        if rid.upper().startswith("REQ-"):
            if not test_path:
                issues.append(f"Row {i} ({rid}): missing automated_test_path")
            if not code_path:
                issues.append(f"Row {i} ({rid}): missing code_path")
            if not ci_url:
                issues.append(f"Row {i} ({rid}): missing ci_run_url")

        if status and status not in VALID_STATUS:
            issues.append(f"Row {i} ({rid}): invalid status '{status}'")

    return len(issues) == 0, issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate traceability matrix file.")
    parser.add_argument("matrix_path", help="Path to markdown or csv matrix")
    args = parser.parse_args()

    path = Path(args.matrix_path)
    if not path.exists():
        print(f"ERROR: file not found: {path}")
        return 2

    text = path.read_text(encoding="utf-8", errors="ignore")
    rows = parse_markdown_table(text) if path.suffix.lower() in {".md", ".markdown"} else parse_csv(text)

    ok, issues = validate_rows(rows)
    if ok:
        print("Traceability matrix: PASS")
        return 0

    print("Traceability matrix: FAIL")
    for issue in issues:
        print(f"- {issue}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
