[← Back to AI/ML Track home](../../README.md)

# Week 3: Evaluate honestly

**When:** Phase 1, week 3. Time and venue are posted in the track channel.

**Field:** 🧮 Classical ML

**Goal:** Learn to tell when a score deserves to be believed.

## 💡 Why this matters

This is the most important week of Phase 1. Most ML failures in the real world are not bad models. They are **bad evaluations**: the model was never as good as the team believed. Today you will watch a careful-looking workflow "discover" a pattern in pure random noise. If it can fool you on coin flips, it can fool you on real data about real people. Learning to catch overfitting, leakage and the accuracy trap is what separates someone who can *run* ML from someone who can be *trusted* with it. AI coding assistants make these mistakes too, and you will be the one who has to catch them.

## Learning objectives

By the end you should be able to:

- Recognise **overfitting** on a validation curve
- Use **cross-validation**, and read both the average and the spread
- Explain **data leakage** and prevent it with a `Pipeline`
- Explain why **accuracy can mislead**, and use precision, recall and F1 instead
- Submit a first entry to a Kaggle competition

## Before the session

- [ ] Finish the [Week 2](../week-02-your-first-model/README.md) notebook
- [ ] Create a free [Kaggle](https://www.kaggle.com) account and verify your phone number if Kaggle asks (needed for some features)
- [ ] Read the rest of [Stage 2: Core ML](../../learning-path/02-core-ml.md)

## Agenda

1. Arrive and set up (10 min)
2. Goal and recap of Week 2 (5 min)
3. Concept: three traps (overfitting, leakage, the accuracy trap) (20 min)
4. Notebook in pairs, then start your Titanic submission (40 min)
5. 🛡️ Responsible AI moment (5 min)
6. Share-out and take-home challenge (10 min)

## Hands-on reference

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GDG-TUM/AI-ML-Track-GDG-on-Campus-TUM/blob/main/weekly-sessions/week-03-evaluate-honestly/evaluate_honestly.ipynb)

Notebook: [`evaluate_honestly.ipynb`](evaluate_honestly.ipynb). The leakage demo uses pure random noise: the honest score is about 50%, yet the leaky workflow reports a "discovery". It is the most important result of Phase 1.

**The honest evaluation checklist:**

- [ ] A baseline to beat
- [ ] Settings chosen on validation data, never on the test set
- [ ] Every preprocessing step inside a `Pipeline`
- [ ] More than accuracy
- [ ] Real mistakes inspected by eye

## 🛡️ Responsible AI moment

Think of a system that screens people: a loan app, exam proctoring, a fraud filter. **Who pays for its false alarms, and who pays when it misses?** The right metric depends on the answer, and the answer is a human one, not a mathematical one.

## 🏁 Take-home challenge

- [ ] Make your **first Kaggle submission** on the [Titanic competition](https://www.kaggle.com/competitions/titanic) using a `Pipeline`. Report your cross-validation score *and* your leaderboard score. Are they close? If not, why?
- [ ] In the leakage demo, change `k=20` to `k=5` and `k=200`. What happens to the leaky score?
- [ ] Write three sentences about a real-life model where accuracy alone would mislead

## 📝 Session notes

Add slides, links, recordings and key takeaways here after the session (via pull request).

- Slides: *to be added*
- Recording: *to be added*
- Extra resources: *to be added*

---
[← Week 2](../week-02-your-first-model/README.md) | [All sessions](../README.md) | [Week 4 →](../week-04-neural-networks-from-scratch/README.md)
