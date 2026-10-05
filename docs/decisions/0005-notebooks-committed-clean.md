[← Back to decision records](README.md)

# 0005. Notebooks are committed clean and run in CI

- **Status:** Accepted
- **Date:** 2026-10-05
- **Deciders:** Track Lead

## Context

Notebooks are our main teaching tool. They are also awkward for version control: outputs bloat the files, execution counts and cell IDs create noisy diffs, and outputs can leak API keys or personal data. Notebooks also silently rot when libraries change.

## Decision

- Notebooks are committed **without outputs or execution counts**, enforced by the `nbstripout` pre-commit hook and a check in `scripts/check_repo.py`.
- **Every teaching notebook is executed top to bottom in CI** (`pytest --nbmake`). A broken notebook blocks the pull request.
- Each notebook has an **Open in Colab** badge, so learners get outputs by running it.
- Notebooks use seeds, small or built-in datasets, and read secrets from the environment.

## Alternatives considered

- **Commit outputs for pretty previews on GitHub:** nice to read, but noisy diffs, big files and a real risk of leaking secrets and data.
- **Convert to scripts or Jupytext pairs:** cleaner diffs, but unfamiliar to beginners and breaks the "click to run" experience.
- **Do not test notebooks:** cheapest, until a session starts with a broken notebook.

## Consequences

- **Good:** small, reviewable diffs. No leaked outputs. Notebooks stay working.
- **Bad:** GitHub previews show code without results. CI takes a minute or two.
- **Revisit when:** notebooks become too heavy to run in CI, or a better review workflow for notebooks is available.
