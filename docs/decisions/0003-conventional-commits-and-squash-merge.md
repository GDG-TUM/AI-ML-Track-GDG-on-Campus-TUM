[← Back to decision records](README.md)

# 0003. Conventional Commits, squash merge and PR-title checks

- **Status:** Accepted
- **Date:** 2026-10-05
- **Deciders:** Track Lead

## Context

The chapter's organization-level guide asks for `<type>: <short summary>` commit messages. We also want readable history, automatic release notes and a low barrier for beginners who are still learning Git.

## Decision

- We **extend the organization convention** to [Conventional Commits](https://www.conventionalcommits.org): optional scope, plus a `ci` type.
- We enforce the format **only on the pull request title**, and we **squash-merge**, so the PR title becomes the commit on `main`.
- Individual commits on a branch can be informal.
- Release notes are generated from PR titles by Release Drafter.

## Alternatives considered

- **Lint every commit (commitlint):** teaches discipline, but is discouraging for beginners and punishes normal "work in progress" commits.
- **No convention:** easiest today, but the history and release notes become noise.
- **Merge commits or rebase merging:** keep every small commit, but make `main` harder to read.

## Consequences

- **Good:** a clean, searchable history. Automatic release notes. A single rule beginners can follow (write a good PR title).
- **Bad:** one more thing to learn. Fine-grained commit history is lost on `main` (it stays visible in the PR).
- **Revisit when:** the check causes frequent frustration, or we move to a flow that needs per-commit messages.
