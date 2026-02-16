#!/usr/bin/env python3
"""
Infer mobile app purpose and ordered user operations from code evidence.
"""

import argparse
import re
from collections import Counter, defaultdict
from pathlib import Path


ALLOWED_EXTENSIONS = {
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".py",
    ".java",
    ".kt",
    ".kts",
    ".swift",
    ".m",
    ".mm",
    ".dart",
    ".xml",
    ".gradle",
}

ALLOWED_FILENAMES = {
    "package.json",
    "pubspec.yaml",
    "pubspec.lock",
    "build.gradle",
    "build.gradle.kts",
    "settings.gradle",
    "settings.gradle.kts",
    "podfile",
    "cartfile",
    "package.swift",
}

SKIP_DIRS = {
    ".git",
    "node_modules",
    "dist",
    "build",
    "scripts",
    "ios/Pods",
    "android/build",
    ".gradle",
}

SKIP_FILENAMES = {
    "infer_app_intent.py",
}

APP_DIR_HINTS = {
    "src",
    "app",
    "lib",
    "ios",
    "android",
    "features",
    "feature",
    "screens",
    "screen",
    "pages",
    "page",
    "modules",
    "module",
}

RUNTIME_SIGNALS = {
    "react_native": ["react-native", "@react-navigation", "native-base", "react native paper"],
    "flutter": ["flutter", "materialapp", "cupertinoapp", "go_router"],
    "android_native": ["jetpack compose", "composable(", "androidx.compose", "navhost"],
    "ios_native": ["swiftui", "uiviewcontroller", "navigationstack", "uikit"],
    "ionic": ["@ionic", "capacitor"],
}

DESIGN_SYSTEM_SIGNALS = {
    "material_3": ["material 3", "materialtheme", "md3", "materialapp"],
    "apple_hig": ["swiftui", "uikit", "cupertino"],
    "custom": ["theme", "design token", "tokens", "brand color"],
}

UI_LIBRARY_SIGNALS = {
    "react-native-paper": ["react-native-paper"],
    "nativebase": ["native-base", "nativebase"],
    "ui-kitten": ["@ui-kitten", "ui kitten"],
    "react-native-elements": ["react-native-elements"],
    "tamagui": ["tamagui"],
    "gluestack": ["gluestack"],
    "jetpack-compose": ["androidx.compose", "composable("],
    "swiftui": ["swiftui", "navigationstack"],
    "uikit": ["uiviewcontroller", "uikit"],
    "flutter-material": ["materialapp", "material"],
    "flutter-cupertino": ["cupertinoapp", "cupertino"],
    "ionic-ui": ["@ionic/react", "ionpage", "ioncontent"],
}

OPERATION_KEYWORDS = {
    "onboard_or_auth": ["onboarding", "login", "signup", "sign in", "auth", "session", "otp"],
    "discover": ["home", "feed", "search", "discover", "browse", "catalog"],
    "detail": ["detail", "profile", "item", "product", "card", "view"],
    "act": ["create", "book", "checkout", "pay", "submit", "add to cart", "place order"],
    "verify": ["confirm", "success", "receipt", "done", "completed"],
    "manage": ["settings", "history", "orders", "account", "profile", "manage"],
}


def should_skip(path: Path) -> bool:
    text = str(path).replace("\\", "/").lower()
    return any(skip in text for skip in SKIP_DIRS) or path.name.lower() in SKIP_FILENAMES


def iter_source_files(root: Path):
    candidates = []
    for path in root.rglob("*"):
        if path.is_dir():
            continue
        if should_skip(path):
            continue
        if path.suffix.lower() in ALLOWED_EXTENSIONS or path.name.lower() in ALLOWED_FILENAMES:
            candidates.append(path)

    hinted = []
    for path in candidates:
        try:
            parts = [part.lower() for part in path.relative_to(root).parts[:-1]]
        except Exception:
            parts = [part.lower() for part in path.parts[:-1]]
        if any(part in APP_DIR_HINTS for part in parts):
            hinted.append(path)

    if hinted:
        return hinted
    return candidates


def safe_read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def collect_routes(text: str) -> list[str]:
    patterns = [
        r"navigate\(\s*['\"]([^'\"]+)['\"]",
        r"name:\s*['\"]([^'\"]+)['\"]",
        r"path:\s*['\"]([^'\"]+)['\"]",
        r"route\(\s*['\"]([^'\"]+)['\"]",
        r"GoRoute\(\s*path:\s*['\"]([^'\"]+)['\"]",
        r"composable\(\s*['\"]([^'\"]+)['\"]",
    ]
    routes = []
    for pattern in patterns:
        routes.extend(re.findall(pattern, text, flags=re.IGNORECASE))
    cleaned = []
    for route in routes:
        value = route.strip()
        if not value:
            continue
        if len(value) > 64:
            continue
        if not re.match(r"^[a-zA-Z0-9_/\-:. ]+$", value):
            continue
        cleaned.append(value)
    return cleaned


def detect_from_signals(
    entries: list[tuple[Path, str]], signals: dict[str, list[str]]
) -> list[tuple[str, int, list[str]]]:
    results = []
    for key, keys in signals.items():
        matched_files = set()
        for path, text in entries:
            lowered = text.lower()
            if any(term in lowered for term in keys):
                matched_files.add(str(path))
        count = len(matched_files)
        if count > 0:
            results.append((key, count, sorted(matched_files)))
    return sorted(results, key=lambda x: x[1], reverse=True)


def confidence_from_hits(hit_count: int) -> str:
    if hit_count >= 8:
        return "high"
    if hit_count >= 3:
        return "medium"
    return "low"


def infer_operations(all_text: str, evidence_map: dict[str, list[str]]) -> list[tuple[str, str]]:
    lowered = all_text.lower()
    present = []
    for op, keywords in OPERATION_KEYWORDS.items():
        hits = sum(lowered.count(keyword) for keyword in keywords)
        if hits > 0:
            present.append((op, hits))
    ordered = ["onboard_or_auth", "discover", "detail", "act", "verify", "manage"]
    present_ops = {op for op, _ in present}
    results = []
    for op in ordered:
        if op in present_ops:
            evidence = evidence_map.get(op, [])
            results.append((op, confidence_from_hits(len(evidence))))
    return results


def op_label(op: str) -> str:
    labels = {
        "onboard_or_auth": "Open and access account",
        "discover": "Discover or search options",
        "detail": "Inspect detail and decide",
        "act": "Perform core action",
        "verify": "Verify outcome",
        "manage": "Manage account or history",
    }
    return labels.get(op, op)


def op_rule(op: str) -> str:
    rules = {
        "onboard_or_auth": "Purpose first and shortest viable path",
        "discover": "Progressive disclosure with low cognitive load",
        "detail": "Trust checkpoint before commitment",
        "act": "Reversible and explicit high-impact action",
        "verify": "Clear system status and next step",
        "manage": "Continuity and easy recovery",
    }
    return rules.get(op, "Purpose first")


def purpose_from_terms(term_counter: Counter) -> str:
    domain_terms = [term for term, _ in term_counter.most_common(20) if len(term) > 3]
    if not domain_terms:
        return "The app exists to help users complete core mobile tasks efficiently."
    top = ", ".join(domain_terms[:3])
    return f"The app likely exists to help users manage {top} through mobile flows."


def build_report(repo: Path) -> str:
    files = list(iter_source_files(repo))
    entries: list[tuple[Path, str]] = []
    combined_text_parts = []
    routes = []
    token_counter = Counter()
    evidence_by_operation: dict[str, list[str]] = defaultdict(list)
    route_files = set()

    for path in files:
        content = safe_read(path)
        if not content:
            continue

        entries.append((path, content))
        combined_text_parts.append(content)

        found_routes = collect_routes(content)
        if found_routes:
            route_files.add(str(path))
            routes.extend(found_routes)

        lowered = content.lower()
        words = re.findall(r"[a-z][a-z0-9_-]{2,}", lowered)
        token_counter.update(words)

        for op, keywords in OPERATION_KEYWORDS.items():
            if any(keyword in lowered for keyword in keywords):
                evidence_by_operation[op].append(str(path))

    all_text = "\n".join(combined_text_parts)
    runtime_rank = detect_from_signals(entries, RUNTIME_SIGNALS)
    design_rank = detect_from_signals(entries, DESIGN_SYSTEM_SIGNALS)
    library_rank = detect_from_signals(entries, UI_LIBRARY_SIGNALS)
    op_sequence = infer_operations(all_text, evidence_by_operation)

    runtime = runtime_rank[0][0] if runtime_rank else "unknown"
    design_system = design_rank[0][0] if design_rank else "unknown"
    library = library_rank[0][0] if library_rank else "unknown"

    runtime_conf = confidence_from_hits(runtime_rank[0][1]) if runtime_rank else "low"
    design_conf = confidence_from_hits(design_rank[0][1]) if design_rank else "low"
    library_conf = confidence_from_hits(library_rank[0][1]) if library_rank else "low"

    purpose = purpose_from_terms(token_counter)
    purpose_conf = confidence_from_hits(len(routes) + len(op_sequence))

    route_preview = sorted(set(routes))[:12]
    route_evidence_preview = sorted(route_files)[:6]
    runtime_evidence_preview = runtime_rank[0][2][:3] if runtime_rank else []
    design_evidence_preview = design_rank[0][2][:3] if design_rank else []
    library_evidence_preview = library_rank[0][2][:3] if library_rank else []

    lines = []
    lines.append("# App Intent Inference")
    lines.append("")
    lines.append("## Runtime Detection")
    lines.append("")
    lines.append(f"- Platform/runtime: {runtime}")
    lines.append(f"- Design system: {design_system}")
    lines.append(f"- UI library stack: {library}")
    lines.append(
        f"- Confidence: runtime={runtime_conf}, design_system={design_conf}, ui_library={library_conf}"
    )
    lines.append(
        "- Runtime evidence paths: "
        + (", ".join(runtime_evidence_preview) if runtime_evidence_preview else "None")
    )
    lines.append(
        "- Design-system evidence paths: "
        + (", ".join(design_evidence_preview) if design_evidence_preview else "None")
    )
    lines.append(
        "- UI-library evidence paths: "
        + (", ".join(library_evidence_preview) if library_evidence_preview else "None")
    )
    lines.append("")
    lines.append("## App Purpose Inference")
    lines.append("")
    lines.append(f"- Purpose statement: {purpose}")
    lines.append("- Primary user: inferred from code context")
    lines.append("- Primary outcome: completion of core task with clear feedback")
    lines.append(f"- Confidence: {purpose_conf}")
    lines.append("")
    lines.append("## Ordered User Operations")
    lines.append("")
    if not op_sequence:
        lines.append("1. Operation: Unknown (insufficient evidence)")
        lines.append("   - User intent: Unknown")
        lines.append("   - UX sequencing rule: Purpose first")
        lines.append("   - Evidence: No strong operation keywords found")
        lines.append("   - Confidence: low")
    else:
        for idx, (op, conf) in enumerate(op_sequence, start=1):
            evidence = sorted(set(evidence_by_operation.get(op, [])))[:3]
            evidence_text = ", ".join(evidence) if evidence else "No direct file evidence"
            lines.append(f"{idx}. Operation: {op_label(op)}")
            lines.append("   - User intent: Complete this stage with minimal friction")
            lines.append(f"   - UX sequencing rule: {op_rule(op)}")
            lines.append(f"   - Evidence: {evidence_text}")
            lines.append(f"   - Confidence: {conf}")
    lines.append("")
    lines.append("## Supporting Evidence")
    lines.append("")
    lines.append(f"- Scanned source files: {len(entries)}")
    lines.append(
        "- Route samples: "
        + (", ".join(route_preview) if route_preview else "No route patterns detected")
    )
    lines.append(
        "- Route evidence files: "
        + (", ".join(route_evidence_preview) if route_evidence_preview else "No route files detected")
    )
    lines.append("")
    lines.append("## Gaps And Unknowns")
    lines.append("")
    if runtime == "unknown":
        lines.append("- Runtime could not be inferred confidently from static code signals.")
    if not op_sequence:
        lines.append("- Core user operation sequence is incomplete; inspect navigation and API layers manually.")
    if purpose_conf == "low":
        lines.append("- Purpose inference is low confidence; add product copy or route naming clarity.")
    if runtime != "unknown" and op_sequence and purpose_conf != "low":
        lines.append("- No major inference blockers detected from static analysis.")

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Infer app intent from codebase.")
    parser.add_argument("repo_path", help="Path to repository root")
    parser.add_argument("--output", help="Optional output markdown path")
    args = parser.parse_args()

    repo = Path(args.repo_path)
    if not repo.exists() or not repo.is_dir():
        print(f"ERROR: repo path is invalid: {repo}")
        return 2

    report = build_report(repo)
    if args.output:
        out_path = Path(args.output)
        out_path.write_text(report, encoding="utf-8")
        print(f"Wrote report: {out_path}")
    else:
        print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
