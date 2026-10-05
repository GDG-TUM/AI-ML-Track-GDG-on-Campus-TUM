[← Back to AI/ML Track home](../../README.md)

# 📝 Decision Records

A decision record is a short note that captures **what we decided, why, and what we gave up**. Student communities turn over every year. Without records, the next lead inherits *what* we do but not *why*, and may undo a good decision by accident or keep a bad one out of habit.

## Index

| # | Decision | Status |
|---|---|---|
| [0001](0001-record-decisions.md) | We record decisions | Accepted |
| [0002](0002-free-compute-first.md) | Free, browser-first compute for everything | Accepted |
| [0003](0003-conventional-commits-and-squash-merge.md) | Conventional Commits, squash merge and PR-title checks | Accepted |
| [0004](0004-framework-policy.md) | scikit-learn, then Keras for guided labs, PyTorch welcome | Accepted, revisit each semester |
| [0005](0005-notebooks-committed-clean.md) | Notebooks are committed clean and run in CI | Accepted |

## When to write one

Write a record when a decision is **hard to reverse**, **affects many people**, or **someone will later ask "why did we do it this way?"**. Examples: the tools we teach, the shape of the curriculum, workflow rules, governance.

## How to write one

1. Copy [`0000-template.md`](0000-template.md) to the next number, such as `0006-short-title.md`.
2. Fill it in. **Short is good**: one page.
3. Open a pull request titled `docs(repo): add decision 0006 on <topic>`.
4. Discuss for the period set in [GOVERNANCE.md](../../GOVERNANCE.md). The Track Lead accepts it.
5. Add it to the index above.

## Changing a decision

Never edit history. Write a **new** record that says *"Supersedes 000X"*, and change the old record's status to *"Superseded by 000Y"*.
