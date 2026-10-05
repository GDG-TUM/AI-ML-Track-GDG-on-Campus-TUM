[← Back to AI/ML Track home](../../README.md)

# Week 4: Neural networks from scratch

**When:** Phase 1, week 4. Time and venue are posted in the track channel.

**Field:** 🧠 Neural networks

**Goal:** Remove the magic from deep learning by training a neural network with nothing but NumPy, then start your mini-project.

## 💡 Why this matters

Every modern neural network learns with the same loop: **measure how wrong you are, work out which way to nudge each number, nudge, repeat.** That includes the large language models behind Gemini and ChatGPT. They have billions of numbers instead of a few dozen, but the idea is identical. Once you have written this loop yourself, AI stops being magic: "training", "parameters" and "learning rate" become things you understand, and when a real training run fails you will know where to look.

## Learning objectives

By the end you should be able to:

- Explain weights, biases, activation functions, loss and gradients in plain words
- Describe backpropagation as "the chain rule, applied backwards"
- Use a **gradient check** to verify that your maths is right
- See what the learning rate, network size and activation do to training
- Choose a partner and a dataset for your Phase 1 mini-project

## Before the session

- [ ] Finish [Week 3](../week-03-evaluate-honestly/README.md)
- [ ] Optional but great: watch the first video of [3Blue1Brown's neural network series](https://www.3blue1brown.com/topics/neural-networks)
- [ ] Think of **one small dataset** you would like to use for your mini-project (or plan to reuse your Week 3 Titanic model)

## Agenda

1. Arrive and set up (10 min)
2. Goal and recap (5 min)
3. Concept: from a line to a network, loss, gradient, backprop (15 min)
4. Notebook in pairs: build, check and train a network (35 min)
5. **Mini-project kickoff:** pick a partner and a dataset (15 min)
6. 🛡️ Responsible AI moment (5 min)
7. Wrap-up and take-home challenge (5 min)

## Hands-on reference

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GDG-TUM/AI-ML-Track-GDG-on-Campus-TUM/blob/main/weekly-sessions/week-04-neural-networks-from-scratch/neural_net_from_scratch.ipynb)

Notebook: [`neural_net_from_scratch.ipynb`](neural_net_from_scratch.ipynb). A two-layer network learns two interlocking moons. The notebook includes a **numerical gradient check**: the trick that saves careers.

### The Phase 1 mini-project

In pairs, you will run the whole Phase 1 workflow on one small dataset and present it in [Week 6](../week-06-phase-1-showcase/README.md). About **3 hours of work in total**. Good choices:

- Your **Titanic** model from Week 3, improved and honestly evaluated
- The **photo classifier** you will build next week
- A small [Kaggle dataset](https://www.kaggle.com/datasets) (under about 10,000 rows) about something you care about

The five things your project must show are listed on the [Week 6 page](../week-06-phase-1-showcase/README.md#the-mini-project). Need inspiration? See the [project ideas](../../projects/ideas.md) (the beginner ones fit).

## 🛡️ Responsible AI moment

For your mini-project dataset: **who or what is in that data, and who is missing?** If it is about people, would they be happy to know how it is used?

## 🏁 Take-home challenge

- [ ] Try the five experiments at the bottom of the notebook. **Predict first, then run.**
- [ ] Post your mini-project pair and dataset in the track channel
- [ ] Mini-project steps 1 and 2: explore the data (one chart) and get a **baseline** score

## 📝 Session notes

Add slides, links, recordings and key takeaways here after the session (via pull request).

- Slides: *to be added*
- Recording: *to be added*
- Extra resources: *to be added*

---
[← Week 3](../week-03-evaluate-honestly/README.md) | [All sessions](../README.md) | [Week 5 →](../week-05-deep-learning-in-practice/README.md)
