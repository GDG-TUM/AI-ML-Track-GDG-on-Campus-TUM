[← Back to AI/ML Track home](../../README.md)

# Week 9: Responsible AI

**When:** Phase 2 (draft), week 9. Time and venue are posted in the track channel.

**Goal:** Review your own project for fairness, privacy and safety, document it honestly and test another team's work.

This whole session is the Responsible AI moment, and it is **Gate C** for every project. Read the full [Responsible AI guide](../../docs/responsible-ai.md) beforehand.

## Learning objectives

By the end you should be able to:

- Map where harm can enter: data, labels, model, deployment and misuse
- Evaluate a model on **slices** and read gaps honestly
- Write a **model card** and a **data card** that tell the truth
- **Red-team** a project: try to break it, and report findings kindly
- Decide what you would change, limit or refuse to build

## Before the session

- [ ] Read the [Responsible AI guide](../../docs/responsible-ai.md) and the [checklist](../../resources/responsible-ai-checklist.md)
- [ ] Bring your **project repo** with a working baseline or model
- [ ] Skim [Stage 5: Responsible AI](../../learning-path/05-responsible-ai.md)

## Agenda

1. Arrive and set up (10 min)
2. Goal and recap (5 min)
3. Concept: harm map, slices, cards (15 min)
4. Workshop in teams: checklist, slice evaluation, model and data cards (30 min)
5. **Red-team swap:** another team tries to break your project (20 min)
6. Wrap-up: findings, outcomes and next steps (10 min)

## Hands-on reference

### 1. The harm map (5 minutes)

On paper, list: **Who uses it? Who is affected but is not a user? What if it is wrong? What if it is misused? What data about whom does it touch?**

### 2. Slice evaluation

Overall accuracy hides who the model fails. Measure by group:

```python
import pandas as pd

report = pd.DataFrame({"group": groups_test, "correct": preds == y_test})
print(report.groupby("group")["correct"].agg(["mean", "count"]))
```

Report the **gap** between your best and worst group, and the **count** in each (small groups give noisy numbers). Slices to try: language, region, gender where ethically collected, device, lighting, accent, input length.

### 3. Model and data cards

Copy [`MODEL_CARD.md`](../../projects/_template/MODEL_CARD.md) and [`DATA_CARD.md`](../../projects/_template/DATA_CARD.md) into your project, and fill them in **truthfully**. Limitations are not an admission of failure. They are the most useful part.

### 4. Red-team swap

Swap projects with another team. For 20 minutes try: **odd and extreme inputs, inputs from groups the model may have missed, misuse, prompt injection** (for LLM apps), and **leaks of private data**. Record each finding as an issue in their repo: what you tried, what happened, why it matters. Be kind and specific.

## 🛡️ The review

Each team then meets two maintainers or mentors for 15 minutes. Outcomes: **Approved**, **Approved with conditions** or **Needs changes**. See [how the review works](../../docs/responsible-ai.md#review).

## 🏁 Take-home challenge

- [ ] Fix the **top three** red-team findings, or write down why you will not
- [ ] Finish the model card, data card and checklist and merge them to your project's `main`
- [ ] If conditions were set, put dates on them in your project issue
- [ ] Write a three-sentence personal reflection: *what is one thing I will always ask before I ship a model?*

## 📝 Session notes

Add slides, links, recordings and key takeaways here after the session (via pull request).

- Slides: *to be added*
- Recording: *to be added*
- Extra resources: *to be added*

---
[← Week 8](../week-08-rag-and-agents-study-jam/README.md) | [All sessions](../README.md) | [Week 10 →](../week-10-from-notebook-to-app/README.md)
