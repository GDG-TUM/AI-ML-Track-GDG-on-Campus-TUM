[← Back to AI/ML Track home](../../README.md)

# Week 2: Your first model

**Date:** Wed 21 Oct (draft; confirm time and venue in the track channel)

**Goal:** Train a model that reads handwriting, and prove it is better than guessing.

## Learning objectives

By the end you should be able to:

- Explain supervised learning, features and labels
- Split data into train and test sets, and say why we keep a "secret exam"
- Set a **baseline** and compare models against it
- Use scikit-learn's `fit`, `predict` and `score`
- Read a confusion matrix and look at a model's real mistakes

## Before the session

- [ ] Finish [Week 1](../week-01-welcome-and-python-for-data/README.md) and its notebook
- [ ] Read the first half of [Stage 2: Core ML](../../learning-path/02-core-ml.md)
- [ ] Make sure you can open a notebook in Colab and save a copy

## Agenda

1. Arrive and set up (10 min)
2. Goal and recap of Week 1 (5 min)
3. Concept: learning from examples, train and test, baselines (20 min)
4. Notebook in pairs: a digit reader (40 min)
5. 🛡️ Responsible AI moment (5 min)
6. Share-out and take-home challenge (10 min)

## Hands-on reference

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GDG-TUM/AI-ML-Track-GDG-on-Campus-TUM/blob/main/weekly-sessions/week-02-your-first-model/first_model.ipynb)

Notebook: [`first_model.ipynb`](first_model.ipynb). The dataset ships with scikit-learn, so nothing needs downloading.

The three verbs you will use for almost every model in this track:

```python
model.fit(X_train, y_train)          # learn from examples
model.predict(X_test)                # guess on new data
model.score(X_test, y_test)          # how good were the guesses?
```

## 🛡️ Responsible AI moment

A digit reader trained on neat handwriting may fail on someone else's. **Whose handwriting is in the training data, and whose is not?** Imagine the same model reading forms at a campus office.

## 🏁 Take-home challenge

- [ ] Change `n_neighbors` (try 1, 3, 15, 50). What happens to train and test accuracy?
- [ ] Add a fourth model, such as `RandomForestClassifier`, to the results table
- [ ] Remove `StandardScaler` from the logistic regression pipeline. Does it matter here?
- [ ] Write **five sentences**: which model would you use, and what would worry you about real handwriting from campus forms?

Post your table and your five sentences in the track channel.

## 📝 Session notes

Add slides, links, recordings and key takeaways here after the session (via pull request).

- Slides: *to be added*
- Recording: *to be added*
- Extra resources: *to be added*

---
[← Week 1](../week-01-welcome-and-python-for-data/README.md) | [All sessions](../README.md) | [Week 3 →](../week-03-evaluate-honestly/README.md)
