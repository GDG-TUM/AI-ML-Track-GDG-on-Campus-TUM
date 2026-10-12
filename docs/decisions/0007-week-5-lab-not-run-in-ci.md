[← Back to decision records](README.md)

# 0007. The Week 5 photo lab is not run in CI

- **Status:** Accepted
- **Date:** 2026-10-12
- **Deciders:** Track Lead
- **Amends:** [0005](0005-notebooks-committed-clean.md)

## Context

[Decision 0005](0005-notebooks-committed-clean.md) runs every teaching notebook top to bottom in CI. The Week 5 notebook, `photo_classifier.ipynb`, is different from the others:

- It needs **Keras** and a backend (preinstalled in Colab), which our CI does not install.
- It downloads a **pretrained model** (about 15 MB) and, when learners bring no photos, a **sample photo set** (about 220 MB).
- Its main input is **each learner's own photos**, which CI cannot have.
- Training is meant for a GPU; on a CI runner it would take several minutes.

## Decision

- CI and `make notebooks` skip the `week-05-deep-learning-in-practice` folder (`--ignore` in `pytest --nbmake`).
- Everything else in 0005 still applies to it: committed **clean**, an **Open in Colab** badge, seeds where they help.
- To make up for the lost safety net, the Week 5 host guide requires a **dry run on a fresh Colab** before every session, with and without uploaded photos.

## Alternatives considered

- **Run it in CI anyway:** add Keras and a backend to CI and download the model and sample photos on every run. Fully tested, but it adds about 250 MB of downloads per run, makes CI slower, and fails whenever a download does.
- **No notebook for Week 5:** follow the Keras guide live, as before. Nothing to test, but beginners lose the step-by-step bridge from Week 4.

## Consequences

- **Good:** Week 5 gets a real, step-by-step notebook, and CI stays fast and reliable.
- **Bad:** a Keras or Colab change can break the notebook without CI noticing.
- **Revisit when:** CI gains a cheap way to run Keras with cached downloads, or the notebook breaks in a session despite the dry run.
