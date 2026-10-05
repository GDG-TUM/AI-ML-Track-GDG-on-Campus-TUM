[← Back to decision records](README.md)

# 0002. Free, browser-first compute for everything

- **Status:** Accepted
- **Date:** 2026-10-05
- **Deciders:** Track Lead

## Context

Members join with very different hardware and internet access. Many have older laptops, limited storage and expensive mobile data. Requiring a GPU, a local installation or paid cloud credits would exclude exactly the students who stand to gain most.

## Decision

Everything in the core curriculum **must run for free in a browser**, on Google Colab or Kaggle Notebooks. Local installation is **optional** and documented. Datasets are **small** or ship with libraries, and each session has an offline fallback.

## Alternatives considered

- **Local-only setup:** the most "professional", but fails on old laptops and burns session time on installation problems.
- **Paid cloud credits:** powerful, but unsustainable, and it creates a cost-risk for members (see the Cloud Track's warning about surprise bills).
- **A shared lab machine:** a single point of failure, and not available out of hours.

## Consequences

- **Good:** nobody is excluded for lack of hardware. Setup takes minutes. Everyone sees the same environment.
- **Bad:** free tiers have limits that change, sessions can disconnect, and we cannot train large models.
- **Mitigations:** use transfer learning and small models, keep offline copies on USB, teach people to save work often, and link to official pages instead of quoting limits.
- **Revisit when:** free-tier terms change materially, or the chapter gains sustainable compute sponsorship.
