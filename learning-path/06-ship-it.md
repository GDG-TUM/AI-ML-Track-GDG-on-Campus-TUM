[← Back to AI/ML Track home](../README.md)

# Stage 6: Ship It

**Goal:** Turn a notebook into something other people can run, test and use.

**Matching sessions:** [Week 10: From notebook to app](../weekly-sessions/week-10-from-notebook-to-app/README.md) and [Week 11: Demo day](../weekly-sessions/week-11-demo-day/README.md)

## What you will learn

- **Reproducibility**: environments, seeds, one command to rerun your result
- **Project structure**: moving code from notebook cells into a small package
- **Tests for ML**: shape checks, sanity checks and small regression tests
- **Demo apps** with Gradio or Streamlit, and APIs with FastAPI
- **Deploying**: Hugging Face Spaces for demos, containers and Cloud Run for services
- **Monitoring**: what changes after launch (drift, cost, misuse)
- **Telling the story**: a README, a model card and a five-minute demo

## Hands-on

1. Start from the [project starter template](../projects/_template/README.md): it already has tests and a one-command run.
2. Wrap your model in a small demo app.
3. Deploy it, or record a clear demo, and practise your five-minute talk.

## Free resources

| Resource | What it is |
|---|---|
| [Made With ML](https://madewithml.com) | Production ML, from design to deployment |
| [Full Stack Deep Learning](https://fullstackdeeplearning.com) | The whole life cycle of an ML project |
| [Gradio quickstart](https://www.gradio.app/guides/quickstart) | A demo app in a few lines |
| [Hugging Face Spaces](https://huggingface.co/docs/hub/spaces) | Free hosting for demos |
| [FastAPI documentation](https://fastapi.tiangolo.com) | Serve a model as an API |
| [Cloud Run documentation](https://cloud.google.com/run/docs) | Run containers on Google Cloud |
| [Cloud Track](https://github.com/GDG-TUM/Cloud-Track-GDG-on-Campus-TUM) | Docker, Cloud Run, CI/CD and cost control, taught step by step |
| [Rules of Machine Learning (Google)](https://developers.google.com/machine-learning/guides/rules-of-ml) | The "ML engineering" half is the most useful here |

> [!WARNING]
> Hosted services can cost money if left running, and public demos can be abused. Set a **budget alert**, keep API keys out of the code, and shut things down after demo day.

## 🛡️ Responsible AI moment

Once your demo is public, strangers will use it in ways you did not plan. Ask: **what is the worst realistic misuse, and what is the smallest change that reduces it?**

## ✅ Checkpoint

- Could a teammate reproduce my main result with one command?
- Which three behaviours of my model have I tested automatically?
- What would I need to monitor after launch?
- Where do my API keys live, and what happens if they leak?
- Can I explain my project to a non-technical person in two minutes?

[← Stage 5](05-responsible-ai.md) · [Learning path overview](README.md)
