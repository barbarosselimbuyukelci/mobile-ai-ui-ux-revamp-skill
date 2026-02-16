#!/usr/bin/env python3
"""
Validate implementation completeness matrix (markdown table or csv).
Compatible with Python 3.9+.
"""

import argparse
import csv
from pathlib import Path
from typing import Dict, List, Set, Tuple


REQUIRED_COLUMNS: Set[str] = {
    "requirement_id",
    "design_feature",
    "status",
    "code_path",
    "evidence",
    "architecture_change",
    "reason",
    "owner",
}

VALID_STATUS: Set[str] = {"implemented", "blocked", "deferred"}


def parse_markdown_table(text: str) -> List[Dict[str, str]]:
    lines = [line.strip() for line in text.splitlines() if line.strip().startswith("|")]
    if len(lines) < 2:
        return []

    header = [col.strip() for col in lines[0].strip("|").split("|")]
    rows: List[Dict[str, str]] = []
    for line in lines[2:]:
        cols = [col.strip() for col in line.strip("|").split("|")]
        if len(cols) != len(header):
            continue
        rows.append({header[i]: cols[i] for i in range(len(header))})
    return rows


def parse_csv(text: str) -> List[Dict[str, str]]:
    reader = csv.DictReader(text.splitlines())
    rows: List[Dict[str, str]] = []
    for row in reader:
        clean = {}
        for key, value in row.items():
            if key is None:
                continue
            clean[key.strip()] = (value or "").strip()
        rows.append(clean)
    return rows


def validate_rows(rows: List[Dict[str, str]]) -> Tuple[bool, List[str]]:
    issues: List[str] = []
    if not rows:
        return False, ["No completeness rows detected."]

    header_keys = set(rows[0].keys())
    missing = REQUIRED_COLUMNS - header_keys
    if missing:
        issues.append("Missing columns: {0}".format(", ".join(sorted(missing))))

    seen_req: Set[str] = set()
    for idx, row in enumerate(rows, start=1):
        req_id = row.get("requirement_id", "").strip()
        status = row.get("status", "").strip().lower()
        evidence = row.get("evidence", "").strip()
        owner = row.get("owner", "").strip()
        reason = row.get("reason", "").strip()

        if not req_id:
            issues.append("Row {0}: missing requirement_id".format(idx))
            continue
        if req_id in seen_req:
            issues.append("Row {0} ({1}): duplicate requirement_id".format(idx, req_id))
        seen_req.add(req_id)

        if status not in VALID_STATUS:
            issues.append("Row {0} ({1}): invalid status '{2}'".format(idx, req_id, status))
            continue

        if status == "implemented":
            if not evidence:
                issues.append("Row {0} ({1}): implemented item missing evidence".format(idx, req_id))

        if status in {"blocked", "deferred"}:
            if not reason:
                issues.append("Row {0} ({1}): {2} item missing reason".format(idx, req_id, status))
            if not owner:
                issues.append("Row {0} ({1}): {2} item missing owner".format(idx, req_id, status))
            if not evidence:
                issues.append("Row {0} ({1}): {2} item missing evidence".format(idx, req_id, status))

    return len(issues) == 0, issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate implementation completeness matrix.")
    parser.add_argument("matrix_path", help="Path to markdown or csv matrix")
    args = parser.parse_args()

    path = Path(args.matrix_path)
    if not path.exists():
        print("ERROR: file not found: {0}".format(path))
        return 2

    text = path.read_text(encoding="utf-8", errors="ignore")
    if path.suffix.lower() in {".md", ".markdown"}:
        rows = parse_markdown_table(text)
    else:
        rows = parse_csv(text)

    ok, issues = validate_rows(rows)
    if ok:
        print("Implementation completeness: PASS")
        return 0

    print("Implementation completeness: FAIL")
    for issue in issues:
        print("- {0}".format(issue))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
