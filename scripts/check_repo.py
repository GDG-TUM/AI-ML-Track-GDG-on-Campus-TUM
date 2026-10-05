#!/usr/bin/env python3
"""Repository checks that run in CI (standard library only, so there is nothing to install).

What it checks, and why:

* Markdown links and anchors   - a broken link is the most common way a docs repo rots
                                 (placeholders such as week-NN-title or NNNN-title.md in
                                 templates are recognised and skipped)
* Colab badges                 - the badge must point at a notebook that really exists
* Weekly session folders       - consistent names, numbering and required sections
* Member profiles              - one file per person, named after their GitHub username
* Notebooks are committed clean - no outputs or execution counts (they bloat and can leak)
* Issue form labels            - GitHub silently ignores labels that do not exist
* Repo health files            - the files a well-run project is expected to have
* Obvious secrets and big files - a cheap safety net on top of gitleaks

Run it with:  python scripts/check_repo.py      (or: make repo-check)
"""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", ".ipynb_checkpoints", "__pycache__"}
MAX_BYTES = 1024 * 1024

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "SECURITY.md",
    "SUPPORT.md",
    "CHANGELOG.md",
    ".github/CODEOWNERS",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/labels.yml",
    ".github/workflows/ci.yml",
]

SESSION_HEADINGS = [
    "learning objectives",
    "before the session",
    "agenda",
    "take-home challenge",
    "session notes",
]

SECRET_PATTERNS = {
    "Google API key": re.compile(r"AIza[0-9A-Za-z_\-]{35}"),
    "GitHub token": re.compile(r"gh[pousr]_[A-Za-z0-9]{36,}"),
    "Private key block": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9]{32,}\b"),
}

LINK_RE = re.compile(r"!?\[(?:[^\]\\]|\\.)*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
REF_DEF_RE = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*<?(\S+?)>?(?:\s+.*)?$")
HTML_SRC_RE = re.compile(r"""<(?:img|a|source)\b[^>]*?\b(?:src|href)=["']([^"']+)["']""")
HEADING_RE = re.compile(r"^ {0,3}(#{1,6})\s+(.*?)\s*#*\s*$")
HTML_ID_RE = re.compile(r"""\b(?:id|name)=["']([^"']+)["']""")
COLAB_RE = re.compile(
    r"colab\.research\.google\.com/github/[^/\s]+/[^/\s]+/blob/[^/\s]+/([^)\s\"']+\.ipynb)"
)
PLACEHOLDER_RE = re.compile(r"(?<![A-Za-z])N{2,4}(?![A-Za-z])")  # NN or NNNN in template links
USERNAME_RE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?$")


class Report:
    """Collects problems so we can show all of them at once instead of stopping at the first."""

    def __init__(self) -> None:
        self.problems: dict[str, list[str]] = defaultdict(list)

    def add(self, check: str, where: str, message: str) -> None:
        self.problems[check].append(f"{where}: {message}")

    def count(self) -> int:
        return sum(len(v) for v in self.problems.values())


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def iter_files(*suffixes: str) -> list[Path]:
    found = []
    for path in sorted(ROOT.rglob("*")):
        skipped = set(path.relative_to(ROOT).parts) & SKIP_DIRS
        if path.is_file() and not skipped and (not suffixes or path.suffix in suffixes):
            found.append(path)
    return found


# --------------------------------------------------------------------------- markdown parsing
def strip_code(text: str) -> str:
    """Blank out fenced code, HTML comments and inline code, keeping line numbers intact."""
    lines, in_fence, fence_char = [], False, ""
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            marker = stripped[:3]
            if not in_fence:
                in_fence, fence_char = True, marker
            elif marker == fence_char:
                in_fence = False
            lines.append("")
            continue
        lines.append("" if in_fence else line)
    text = "\n".join(lines)
    text = re.sub(r"<!--.*?-->", lambda m: "\n" * m.group().count("\n"), text, flags=re.S)
    return "\n".join(re.sub(r"`[^`\n]*`", "", line) for line in text.splitlines())


def slugify(heading: str) -> str:
    """GitHub's heading anchor rules: strip markup, lower-case, drop punctuation and emoji."""
    heading = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", heading)
    heading = re.sub(r"<[^>]+>", "", heading)
    heading = re.sub(r"[`*~]", "", heading).strip().lower()
    heading = re.sub(r"[^\w\- ]", "", heading)
    return heading.replace(" ", "-")


def anchors_in(text: str) -> set[str]:
    cleaned = strip_code(text)
    anchors: set[str] = set(HTML_ID_RE.findall(cleaned))
    seen: dict[str, int] = defaultdict(int)
    for line in cleaned.splitlines():
        match = HEADING_RE.match(line)
        if not match:
            continue
        slug = slugify(match.group(2))
        anchors.add(slug if seen[slug] == 0 else f"{slug}-{seen[slug]}")
        seen[slug] += 1
    return anchors


def is_external(target: str) -> bool:
    return bool(re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target)) or target.startswith("//")


# --------------------------------------------------------------------------- the checks
def check_links(report: Report) -> None:
    anchor_cache: dict[Path, set[str]] = {}

    def anchors_of(path: Path) -> set[str]:
        if path not in anchor_cache:
            anchor_cache[path] = anchors_in(path.read_text(encoding="utf-8"))
        return anchor_cache[path]

    for md in iter_files(".md"):
        text = strip_code(md.read_text(encoding="utf-8"))
        targets: list[tuple[int, str]] = []
        for number, line in enumerate(text.splitlines(), start=1):
            targets += [(number, t) for t in LINK_RE.findall(line)]
            targets += [(number, t) for t in HTML_SRC_RE.findall(line)]
            ref = REF_DEF_RE.match(line)
            if ref:
                targets.append((number, ref.group(1)))

        for number, target in targets:
            if is_external(target) or target == "#" or PLACEHOLDER_RE.search(target):
                continue
            path_part, _, fragment = target.partition("#")
            path_part = path_part.split("?")[0]
            where = f"{rel(md)}:{number}"

            if not path_part:  # a same-file anchor like (#goals)
                destination = md
            elif path_part.startswith("/"):
                destination = ROOT / path_part.lstrip("/")
            else:
                destination = (md.parent / path_part).resolve()

            if not destination.exists():
                report.add("links", where, f"broken link: {target}")
                continue
            if fragment and destination.suffix == ".md" and fragment not in anchors_of(destination):
                report.add("links", where, f"missing anchor #{fragment} in {rel(destination)}")


def check_colab_badges(report: Report) -> None:
    for path in iter_files(".md", ".ipynb"):
        if "_template" in path.parts:
            continue
        for match in COLAB_RE.finditer(path.read_text(encoding="utf-8")):
            notebook = match.group(1)
            if not (ROOT / notebook).exists():
                report.add(
                    "colab", rel(path), f"Colab badge points at a missing notebook: {notebook}"
                )


def check_sessions(report: Report) -> None:
    sessions_dir = ROOT / "weekly-sessions"
    overview = (sessions_dir / "README.md").read_text(encoding="utf-8")
    folders = sorted(p for p in sessions_dir.iterdir() if p.is_dir() and not p.name.startswith("_"))
    numbers = []
    for folder in folders:
        match = re.fullmatch(r"week-(\d{2})-[a-z0-9]+(?:-[a-z0-9]+)*", folder.name)
        if not match:
            report.add(
                "sessions", rel(folder), "folder must be named week-NN-short-title (lower case)"
            )
            continue
        numbers.append(int(match.group(1)))
        readme = folder / "README.md"
        if not readme.exists():
            report.add("sessions", rel(folder), "missing README.md")
            continue
        headings = [
            m.group(2).lower()
            for line in strip_code(readme.read_text(encoding="utf-8")).splitlines()
            if (m := HEADING_RE.match(line))
        ]
        for required in SESSION_HEADINGS:
            if not any(required in heading for heading in headings):
                report.add("sessions", rel(readme), f"missing a '{required}' section")
        if f"{folder.name}/README.md" not in overview:
            report.add(
                "sessions", rel(sessions_dir / "README.md"), f"does not link to {folder.name}"
            )
    if numbers and numbers != list(range(1, len(numbers) + 1)):
        report.add(
            "sessions", "weekly-sessions", f"week numbers should run 01..NN without gaps: {numbers}"
        )


def check_members(report: Report) -> None:
    for profile in sorted((ROOT / "members").glob("*.md")):
        if profile.name in {"README.md", "_template.md"}:
            continue
        username = profile.stem
        if not USERNAME_RE.fullmatch(username):
            report.add(
                "members", rel(profile), "file name must be a valid GitHub username: <username>.md"
            )
            continue
        github_line = next(
            (ln for ln in profile.read_text(encoding="utf-8").splitlines() if "**GitHub:**" in ln),
            "",
        )
        if f"@{username}".lower() not in github_line.lower():
            report.add("members", rel(profile), f"the **GitHub:** line must mention @{username}")


def check_notebooks_clean(report: Report) -> None:
    for path in iter_files(".ipynb"):
        try:
            notebook = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            report.add("notebooks", rel(path), f"not valid JSON: {error}")
            continue
        for index, cell in enumerate(notebook.get("cells", [])):
            if cell.get("cell_type") != "code":
                continue
            if cell.get("outputs") or cell.get("execution_count") is not None:
                report.add(
                    "notebooks",
                    f"{rel(path)} (cell {index})",
                    "has outputs or an execution count. Run `make format` (nbstripout) to clear them",
                )
                break


def check_issue_form_labels(report: Report) -> None:
    labels_file = ROOT / ".github" / "labels.yml"
    defined = {
        m.group(1).strip().strip("\"'")
        for line in labels_file.read_text(encoding="utf-8").splitlines()
        if (m := re.match(r"^- name:\s*(.+?)\s*$", line))
    }
    for form in sorted((ROOT / ".github" / "ISSUE_TEMPLATE").glob("*.yml")):
        for match in re.finditer(r"^labels:\s*\[(.*?)\]", form.read_text(encoding="utf-8"), re.M):
            for label in re.findall(r"\"([^\"]+)\"|'([^']+)'", match.group(1)):
                name = label[0] or label[1]
                if name not in defined:
                    report.add(
                        "labels", rel(form), f"label '{name}' is not defined in .github/labels.yml"
                    )


def check_health_files(report: Report) -> None:
    for name in REQUIRED_FILES:
        if not (ROOT / name).exists():
            report.add("health", name, "required file is missing")


def check_secrets_and_size(report: Report) -> None:
    for path in iter_files():
        if path.stat().st_size > MAX_BYTES:
            report.add("size", rel(path), f"larger than {MAX_BYTES // 1024} KB. Link to it instead")
        if path.suffix in {".png", ".jpg", ".jpeg", ".gif", ".ico"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                report.add("secrets", rel(path), f"looks like a {label}. Revoke it, then remove it")


CHECKS = [
    ("Repo health files", check_health_files),
    ("Markdown links and anchors", check_links),
    ("Colab badges", check_colab_badges),
    ("Weekly sessions", check_sessions),
    ("Member profiles", check_members),
    ("Notebooks are committed clean", check_notebooks_clean),
    ("Issue form labels", check_issue_form_labels),
    ("Secrets and file sizes", check_secrets_and_size),
]


def main() -> int:
    report = Report()
    for title, check in CHECKS:
        before = report.count()
        check(report)
        failed = report.count() - before
        print(
            f"{'✅' if not failed else '❌'} {title}"
            + (f" ({failed} problem(s))" if failed else "")
        )

    if report.count():
        print(f"\n{report.count()} problem(s) found:\n")
        for check, problems in report.problems.items():
            print(f"[{check}]")
            for problem in problems:
                print(f"  - {problem}")
        return 1
    print("\nAll repo checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
