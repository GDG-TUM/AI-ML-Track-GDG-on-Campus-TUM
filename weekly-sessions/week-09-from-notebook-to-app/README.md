[← Back to AI/ML Track home](../../README.md)

# Week 9: From notebook to app

**Date:** Wed 9 Dec (draft; confirm time and venue in the track channel)

**Goal:** Make your project reproducible, tested and demo-ready, with a review from a mentor.

## Learning objectives

By the end you should be able to:

- Make a result **reproducible**: environment, seeds, one command
- Move code out of notebook cells into a small, importable package
- Write a few **useful tests** for an ML project
- Wrap a model in a demo app with Gradio (or Streamlit or FastAPI)
- Choose a way to share your demo, and keep it safe

## Before the session

- [ ] Finish [Week 8](../week-08-responsible-ai/README.md) and the review follow-ups
- [ ] Read [Stage 6: Ship it](../../learning-path/06-ship-it.md)
- [ ] Look at the [starter template](../../projects/_template/README.md) and its tests
- [ ] Come with your project open and one specific question for the clinic

## Agenda

1. Arrive and set up (10 min)
2. Goal and recap (5 min)
3. Concept: reproducibility, tests for ML, serving (10 min)
4. Build in teams: package, tests, demo (30 min)
5. **Project clinic:** each team gets about 10 minutes with a mentor, in rotation, while others keep building (25 min)
6. 🛡️ Responsible AI moment (5 min)
7. Wrap-up and take-home challenge (5 min)

## Hands-on reference

### Reproducible in one command

A teammate should be able to run `pip install -r requirements.txt` and then one command, and see your main result. The [starter template](../../projects/_template/README.md) does exactly that with `python -m src.train`.

### Tests that are worth writing

| Test | Example |
|---|---|
| **Shapes** | The model returns one prediction per input |
| **Sanity** | It beats the baseline, so a broken pipeline fails loudly |
| **Invariance** | Predictions don't change when irrelevant things change (case, whitespace) |
| **Edge cases** | An empty input, a very long input and unseen categories do not crash it |
| **Regression** | Today's score is not far below last week's |

### A demo app in a few lines

```python
import gradio as gr


def predict(text):
    # call your model here and return a label
    return "positive"


gr.Interface(fn=predict, inputs="text", outputs="label").launch()
```

### Where to host it

| Option | Good for |
|---|---|
| **A recorded demo** | Zero risk, always works. A great backup. |
| **[Hugging Face Spaces](https://huggingface.co/docs/hub/spaces)** | Free hosting for Gradio and Streamlit demos |
| **[Cloud Run](https://cloud.google.com/run/docs)** | Container services, taught in the [Cloud Track](https://github.com/GDG-TUM/Cloud-Track-GDG-on-Campus-TUM) |

> [!WARNING]
> Public demos can be abused and hosted services can cost money. Keep API keys in secrets, set a **budget alert**, rate-limit where you can and shut things down after demo day.

## 🛡️ Responsible AI moment

Once your demo is public, strangers will use it in ways you did not plan. **What is the worst realistic misuse, and what is the smallest change that makes it harder?**

## 🏁 Take-home challenge

- [ ] Your project runs from a **fresh clone** with one command (ask a teammate to try it)
- [ ] At least **three tests** pass in CI
- [ ] README follows the [template](../../projects/project-template.md), including model card links
- [ ] A **demo** is live, or a clear recording exists as a backup
- [ ] Prepare your **5-minute demo** and rehearse it twice

## 📝 Session notes

Add slides, links, recordings and key takeaways here after the session (via pull request).

- Slides: *to be added*
- Recording: *to be added*
- Extra resources: *to be added*

---
[← Week 8](../week-08-responsible-ai/README.md) | [All sessions](../README.md) | [Week 10 →](../week-10-demo-day/README.md)
