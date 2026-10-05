# Contributing to the AI/ML Track

Thanks for wanting to contribute! 🎉 This track is a student community where we learn by building together. Every contribution counts: a fixed typo, a better explanation, a new notebook, a project, a review. You don't need to be an expert. You just need to be willing to learn.

This guide **adds track-specific rules on top of** the [GDG on Campus TUM contributing guide](https://github.com/GDG-TUM/.github/blob/main/CONTRIBUTING.md). Where they differ, this page wins for this repository.

By taking part you agree to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## Ways to contribute

| You could... | Example | Good first? |
|---|---|:-:|
| **Fix or improve docs** | Fix a typo, clarify a confusing paragraph | ✅ |
| **Add your profile** | Your first pull request: [members/](members/README.md) | ✅ |
| **Add a resource** | A great tutorial, with one line on why it helps | ✅ |
| **Translate or simplify** | Explain a glossary term in Swahili or in plainer English | ✅ |
| **Take session notes** | Slides, links and takeaways after a session | ✅ |
| **Improve a notebook** | A clearer plot, a better exercise, a bug fix | 🟡 |
| **Write a session** | Propose and draft a new week or study jam | 🟡 |
| **Build a project** | A team project with a model card and a demo | 🟡 |
| **Review a pull request** | Read someone's PR and leave kind, specific feedback | 🟡 |
| **Improve automation** | CI, labels, scripts | 🔴 |

Look for issues labelled **`good first issue`** or **`help wanted`**.

---

## Before you start

1. **Search existing issues and pull requests** so you don't duplicate work.
2. **Open an issue first** for anything bigger than a small fix. Use an issue form: it asks the right questions.
3. **Comment to claim it.** One person per issue keeps things clear. If you go quiet for two weeks, we will gently free it up.
4. **Ask questions early.** Nobody expects you to figure everything out alone.

---

## Set up

```bash
# Fork on GitHub, then:
git clone https://github.com/<your-username>/AI-ML-Track-GDG-on-Campus-TUM.git
cd AI-ML-Track-GDG-on-Campus-TUM
git remote add upstream https://github.com/GDG-TUM/AI-ML-Track-GDG-on-Campus-TUM.git

make setup        # creates .venv, installs tools, enables pre-commit
make check        # run everything CI runs (lint, notebooks, repo checks)
```

`make help` lists every command. Full setup notes (including Windows without `make`) are in [GETTING-STARTED.md](GETTING-STARTED.md).

---

## Branches

`main` is always in a releasable state. **Never work directly on `main`.** Make a short-lived branch, change one thing, open a pull request, delete the branch.

```bash
git fetch upstream
git checkout -b <type>/<short-description> upstream/main
```

Examples: `feat/week-05-transfer-learning-notebook`, `fix/broken-colab-link`, `docs/glossary-embeddings`

---

## Commits and pull request titles

We follow [Conventional Commits](https://www.conventionalcommits.org). This is the standard in most professional teams, and it lets us generate release notes automatically.

```text
<type>(<optional scope>): <short summary in present tense>
```

| Type | Use for |
|------|---------|
| `feat` | New content or capability (a session, notebook, project template) |
| `fix` | A bug or error fix (broken link, wrong explanation, failing notebook) |
| `docs` | Documentation only |
| `style` | Formatting, no meaning change |
| `refactor` | Restructuring without changing behaviour |
| `test` | Adding or fixing tests and checks |
| `chore` | Maintenance, dependencies, config |
| `ci` | GitHub Actions and automation |

**Scopes** (optional, pick the closest): `curriculum`, `sessions`, `projects`, `competitions`, `members`, `resources`, `docs`, `repo`, `deps`.

**Rules of thumb**

- Present tense, lower case, no full stop: `feat(sessions): add week 6 notebook`
- Under about 72 characters
- Add `!` for a breaking change, such as renaming a folder others link to: `refactor(sessions)!: rename week folders`
- **Your pull request title must follow this format.** We squash-merge, so the PR title becomes the commit on `main`. A check enforces it.

Your individual commits on a branch can be informal. Only the PR title matters on `main`.

---

## Notebook standards

Notebooks are the heart of this track, so they are held to a standard.

- [ ] **Runs top to bottom** on a fresh kernel (*Kernel → Restart and run all*). CI executes every notebook.
- [ ] **Committed clean:** no outputs, no execution counts. The `nbstripout` pre-commit hook does this for you.
- [ ] **Seeds set** (`np.random.default_rng(0)`, `random_state=0`) so everyone sees the same results.
- [ ] **Small and offline-friendly:** prefer datasets that ship with scikit-learn or are generated in the notebook. If you must download, keep it small, say how big it is, and link the source and licence.
- [ ] **Explains the why**, not just the code. Short markdown cells before each step.
- [ ] **Ends with a take-home challenge** and "what to try next".
- [ ] **No secrets, no personal data.** Read keys from environment variables or Colab Secrets.
- [ ] Includes an **Open in Colab** badge (copy one from an existing notebook).

## Writing standards

- Plain English, short sentences, one idea per paragraph.
- Define jargon the first time, and add it to the [glossary](resources/glossary.md).
- Use examples from our context: campus life, Kenyan data, local problems.
- Add alt text to images.
- Prefer commas and colons to long dashes, and keep emoji for headings and signposts, not decoration.
- Link to official docs for anything that changes quickly (free-tier limits, model names).

## Code standards

- Python formatted and linted with [Ruff](https://docs.astral.sh/ruff/) (`make lint`, `make format`).
- Pin nothing you don't have to, but test on the latest versions.
- Don't commit data files, model weights or large binaries. Link to them (Kaggle, Hugging Face Hub, Drive) instead.
- Never `pickle.load` or `torch.load` a file you don't trust. See [SECURITY.md](SECURITY.md).

---

## Pull requests

A good pull request:

- Has a **title in Conventional Commit format** and a description of **what** changed and **why**
- Links the related issue (for example `Closes #12`)
- Is **small enough to review in one sitting**. One pull request does one thing.
- Includes screenshots for visual changes
- Passes the automated checks
- Is opened as a **draft** if you want early feedback

```bash
make check                        # before you push
git push origin <your-branch-name>
```

**What happens next**

1. Automated checks run: lint, notebooks, repo structure, links.
2. A maintainer reviews, **usually within 3 days** (we are students with exams, so please be patient).
3. They may request changes. This is normal and part of learning, not a judgment on you.
4. Once approved and green, a maintainer **squash-merges** it and the branch is deleted.

### Reviewing other people's work

Reviewing is one of the best ways to learn. You do not need to be a maintainer to leave a review.

- Be **kind and specific**: say what is good, then what to improve and why.
- Prefix small suggestions with `nit:` and questions with `question:`, so the author knows what is blocking.
- Critique the work, never the person.
- Approve when it is good enough, not when it is perfect.

---

<a id="ai-assisted"></a>

## AI-assisted contributions

AI tools are a normal part of how people learn and code today, and we welcome their use. We ask for two things:

1. **You understand it.** You must be able to explain every line you submit. If a reviewer asks "why?", "the AI wrote it" is not an answer.
2. **You say so.** Tick the AI box in the pull request template and say briefly what you used it for.

You are responsible for the correctness, licensing and safety of what you submit. Never paste private data, secrets or other people's unpublished work into an AI tool. For university coursework, follow your lecturers' rules.

---

## Licence and credit

This repository is under the [MIT License](LICENSE). By contributing you confirm that:

- the work is yours, or you have the right to share it under the MIT License
- anything you copy from elsewhere is **credited** and its licence allows reuse (datasets and images often do not)

## Reporting bugs and ideas

Open an issue with the matching form: **bug report**, **session proposal**, **project proposal**, **resource suggestion** or **question**. For security problems, **do not open a public issue**. Follow [SECURITY.md](SECURITY.md).

## Recognition

Contributors are credited in project READMEs, highlighted at demo day and shared in our community channels. Your contributions are public on your GitHub profile, which makes them a good part of your portfolio.

## Need help?

- Ask a **maintainer** or the **Track Lead**
- Comment on the relevant issue
- Read [SUPPORT.md](SUPPORT.md)

Thank you for helping us build a stronger AI community at TUM. 💙
