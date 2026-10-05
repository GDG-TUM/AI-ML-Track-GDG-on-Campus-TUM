[← Back to AI/ML Track home](../README.md)

# 🧰 Maintainers Guide

For the Track Lead, co-leads and maintainers. It covers launching the repo, the settings that make the workflow work, routine chores, releases and the yearly handover. Settings names below match GitHub's current interface, but menus move occasionally, so adjust if something has been renamed.

[Launch checklist](#launch) · [Settings](#settings) · [Routine chores](#routine) · [Releases](#releases) · [Handover](#handover) · [Troubleshooting](#troubleshooting)

---

<a id="launch"></a>

## 🚀 Launch checklist (day 0)

Do these once, in order, when the repository first goes live.

**Repository**

- [ ] Repo name `AI-ML-Track-GDG-on-Campus-TUM` in the `GDG-TUM` organization (so all links in the docs work)
- [ ] Description: *AI & ML Track of GDG on Campus TUM: learn it, build it, ship it responsibly.*
- [ ] Topics: `gdg`, `google-developer-groups`, `machine-learning`, `artificial-intelligence`, `deep-learning`, `generative-ai`, `responsible-ai`, `education`, `student-community`, `kenya`
- [ ] Upload [`assets/social-preview.png`](../assets/social-preview.png) under **Settings → General → Social preview**
- [ ] Decide visibility. Colab badges and GitHub Pages work best when the repo is **public**.

**Settings** (details in the next section)

- [ ] Merge settings, branch ruleset, Actions permissions, security features

**People**

- [ ] Create teams `ai-ml-track-leads` and `ai-ml-track-maintainers` and point [CODEOWNERS](../.github/CODEOWNERS) at the leads team
- [ ] Ensure **at least two people have admin access**
- [ ] Invite maintainers with **Write**, mentors with **Triage**
- [ ] Update the team note in [GOVERNANCE.md](../GOVERNANCE.md)

**Automation and content**

- [ ] Run the **Sync labels** workflow once (Actions tab, then *Run workflow*)
- [ ] Turn on **Discussions** with categories: Announcements, Q&A, Ideas, Show and tell
- [ ] Add the repo to the [chapter board](https://github.com/orgs/GDG-TUM/projects/1) and turn on its built-in workflows
- [ ] Open and **pin** a welcome issue linking to Getting Started
- [ ] Open starter issues labelled `good first issue` (fix a glossary entry, add a resource, add your profile)
- [ ] Publish the first release (see [Releases](#releases))
- [ ] Update the track table in the organization's `profile/README.md` and `README.md` to link here and mark AI/ML as open
- [ ] Announce in the channel and on LinkedIn

---

<a id="settings"></a>

## ⚙️ Settings that make the workflow work

### Pull requests (Settings → General → Pull Requests)

- [x] Allow **squash merging** only (turn off merge commits and rebase merging)
- [x] Default commit message: **Pull request title and description**
- [x] **Automatically delete head branches**
- [x] Allow auto-merge (optional, handy for Dependabot)

### Branch ruleset (Settings → Rules → Rulesets → New branch ruleset)

Target the default branch (`main`), enforcement **Active**:

- [x] Restrict deletions
- [x] Block force pushes
- [x] Require linear history
- [x] **Require a pull request before merging**
  - [x] Required approvals: **1**
  - [x] Dismiss stale approvals when new commits are pushed
  - [x] Require review from Code Owners
  - [x] Require conversation resolution
- [x] **Require status checks to pass**: add **`CI passed`** and **`Conventional Commit title`**
- [x] Add the Track Lead role to the bypass list **only for emergencies**, and use it rarely

> [!TIP]
> Requiring the single `CI passed` job means you can add or rename CI jobs without touching the ruleset.

### Actions (Settings → Actions → General)

- **Workflow permissions:** *Read repository contents and packages permissions*. Each workflow asks for the extra rights it needs.
- **Fork pull request workflows:** require approval for first-time contributors
- Leave "Allow GitHub Actions to create and approve pull requests" **off**

### Security (Settings → Code security)

- [x] **Dependabot alerts** and **Dependabot security updates**
- [x] **Secret scanning** and **Push protection**
- [x] **Private vulnerability reporting** (powers the "Report a vulnerability" button in [SECURITY.md](../SECURITY.md))

### Website (Settings → Pages)

Source: **Deploy from a branch**, branch `main`, folder `/ (root)`. The docsify site in `index.html` goes live at `https://gdg-tum.github.io/AI-ML-Track-GDG-on-Campus-TUM/`. Pages for a private repository needs a paid plan, so make the repo public first.

---

<a id="routine"></a>

## 🔁 Routine chores

| When | Chore |
|---|---|
| **Weekly (Mon)** | Triage new issues, check the board, confirm the session host and helper |
| **Weekly (Fri)** | 20-minute maintainer sync, merge ready PRs, plan next week |
| **Weekly (auto)** | Read the link-check issue if one is opened, and fix or exclude the links |
| **Monthly** | Merge Dependabot PRs, run `pre-commit autoupdate`, member check-ins |
| **Semester start** | Check the [roadmap](../roadmap/semester-roadmap.md), post session times and venues in the track channel, welcome new members, archive last cohort's projects |
| **End of Phase 1 (Week 6)** | Retrospective, attendance check, finalise Phase 2 in the roadmap |
| **Semester end** | Retrospective, release, update the showcase, thank mentors, run the handover |

---

<a id="releases"></a>

## 🏷️ Releases

1. Make sure `main` is green and the [changelog](../CHANGELOG.md) is up to date.
2. Open **Releases**. [Release Drafter](../.github/release-drafter.yml) has already drafted notes from merged PR titles and picked the next version.
3. Check the version: **MAJOR** for a new curriculum year or link-breaking restructure, **MINOR** for new content, **PATCH** for fixes.
4. Edit the notes if needed (add a sentence on the highlights) and click **Publish release**.
5. Move `[Unreleased]` entries in the changelog under the new version in a small `docs:` PR.

Release at the end of each phase (week 6 and week 11) and at the end of the year.

---

<a id="handover"></a>

## 🤝 Handover checklist (every academic year)

Run this at least a month before a lead or co-lead leaves.

**People and access**

- [ ] Name the **successor**, and let them shadow the lead for a month
- [ ] Transfer **admin** access. Keep **two admins** at all times.
- [ ] Remove access for people who have left. Move inactive maintainers to Member, with thanks.
- [ ] Update [GOVERNANCE.md](../GOVERNANCE.md) and [CODEOWNERS](../.github/CODEOWNERS)

**Accounts and secrets**

- [ ] List every account, API key and service used. Keys are owned by a **shared chapter account**, not a personal one.
- [ ] **Rotate** any key the outgoing lead has seen
- [ ] Check that the organization has at least two owners

**Knowledge**

- [ ] Write or update [decision records](decisions/README.md) for choices made this year
- [ ] Update the [roadmap](../roadmap/semester-roadmap.md) for the next academic year
- [ ] Hold a **60-minute walkthrough**: repo, board, sessions, mentors, partners, what to do first
- [ ] Share the contact details of mentors, speakers and venue contacts (with their consent)

**Content**

- [ ] Publish a final release for the year
- [ ] Archive finished projects (README says "what we learned")
- [ ] Open the next year's milestone and issues

---

<a id="troubleshooting"></a>

## 🩺 Troubleshooting

| Symptom | Likely cause and fix |
|---|---|
| **CI passed** never appears as a required check | A status check only shows in the ruleset list after it has run once. Open a PR, let CI finish, then add it. |
| PR title check fails on a good title | The summary must start with a lower-case letter, and the type must be one of the allowed ones. See [CONTRIBUTING](../CONTRIBUTING.md#commits-and-pull-request-titles). |
| Labels do not appear on a PR | The labeler needs `pull_request_target`. Check the workflow ran and that the labels exist (run **Sync labels**). |
| Issue form labels are missing | Labels must exist first. Run **Sync labels**. |
| A notebook passes locally but fails in CI | A library version differs. Look at the failing cell. Pin the version at the top of the notebook if needed, and open an issue. |
| `nbstripout` rewrites a file on every commit | Run `make format` once and commit the cleaned file. Check your Jupyter version is not adding extra metadata. |
| Link checker reports a site that is fine | The site blocks bots. Add it to `exclude` in [`.lychee.toml`](../.lychee.toml). |
| Colab badge opens a 404 | The repository is private. Make it public or download the notebook. |
| Pages shows a 404 | Pages is not enabled, or the repo is private on a free plan. Check Settings → Pages. |
