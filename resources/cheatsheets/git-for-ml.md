[← Back to AI/ML Track home](../../README.md)

# Git for ML Cheat Sheet

## Everyday commands

```bash
git status                         # what changed?
git diff                           # show unstaged changes
git add path/to/file               # stage a file
git commit -m "feat(sessions): add week 6 notebook"
git log --oneline -10              # recent history
git switch -c feat/my-change       # new branch
git switch main                    # go back to main
```

## The contribution flow

```bash
# One-time setup, after forking on GitHub
git clone https://github.com/<you>/AI-ML-Track-GDG-on-Campus-TUM.git
cd AI-ML-Track-GDG-on-Campus-TUM
git remote add upstream https://github.com/GDG-TUM/AI-ML-Track-GDG-on-Campus-TUM.git

# Every change
git fetch upstream
git switch -c docs/fix-glossary-typo upstream/main
# ...make changes...
make check                         # lint, notebooks, repo checks
git add -A
git commit -m "docs(resources): fix typo in glossary"
git push -u origin docs/fix-glossary-typo
# then open a pull request on GitHub. The title is a Conventional Commit.
```

Commit message types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `ci`. Details in [CONTRIBUTING](../../CONTRIBUTING.md).

## Staying up to date

```bash
git fetch upstream
git rebase upstream/main           # replay your work on top of the latest main
```

## Undo and recover

| I want to... | Command |
|---|---|
| Discard changes to a file | `git restore path/to/file` |
| Unstage a file | `git restore --staged path/to/file` |
| Fix my last commit message (not pushed) | `git commit --amend` |
| Undo my last commit but keep the changes | `git reset --soft HEAD~1` |
| Save work without committing | `git stash`, later `git stash pop` |
| See everything I did, even lost commits | `git reflog` |

## Notebooks and Git

Notebooks are JSON, so they need a little care.

- **Commit them clean** (no outputs). `make setup` installs a hook that does this for you. Or run `nbstripout notebook.ipynb`.
- **Restart and run all** before you commit, to be sure it works top to bottom.
- Merge conflicts in notebooks are painful. Keep **one person per notebook** at a time, and pull before you start.
- Outputs can leak keys and data, which is one more reason to strip them.

## What not to commit

| Never commit | Instead |
|---|---|
| API keys, tokens, passwords, `.env` | Environment variables, Colab Secrets, a `.env.example` |
| Personal data | Anonymise, use synthetic or public data |
| Large datasets (more than a few MB) | Link to Kaggle, Hugging Face, Drive, and document the download |
| Model weights (`.pt`, `.h5`, `.ckpt`) | Host on Hugging Face Hub or Drive and link |
| Notebook outputs | `nbstripout` |
| `.venv/`, `__pycache__/` | Already in `.gitignore` |

## Oops, I committed a secret

1. **Revoke the key at the provider first.** This is what actually protects you.
2. Tell a maintainer.
3. Create a new key and store it safely.
4. Only then clean the history (a maintainer will help). Deleting the file is **not** enough.

See [SECURITY.md](../../SECURITY.md).
