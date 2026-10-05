[← Back to AI/ML Track home](../README.md)

# Stage 2: Core Machine Learning

**Goal:** Train a model with scikit-learn and be able to *defend* its score.

**Matching sessions:** [Week 2: Your first model](../weekly-sessions/week-02-your-first-model/README.md) and [Week 3: Evaluate honestly](../weekly-sessions/week-03-evaluate-honestly/README.md)

## What you will learn

- Supervised versus unsupervised learning, classification versus regression
- Features, labels and the **train, validation and test** split
- Why every project starts with a **baseline**
- scikit-learn's three verbs: `fit`, `predict`, `score`
- Metrics beyond accuracy: precision, recall, F1, the confusion matrix
- **Overfitting and underfitting**, and how cross-validation helps you see them
- **Data leakage**: how people accidentally cheat, and how a `Pipeline` prevents it
- Looking at real mistakes with your own eyes

## Hands-on

1. Run the [Week 2 notebook](../weekly-sessions/week-02-your-first-model/first_model.ipynb) and the [Week 3 notebook](../weekly-sessions/week-03-evaluate-honestly/evaluate_honestly.ipynb).
2. Make your **first Kaggle submission** on the [Titanic competition](https://www.kaggle.com/competitions/titanic).
3. Write five sentences: which model did you choose, and how do you know the score is honest?

## Free resources

| Resource | What it is |
|---|---|
| [Machine Learning Crash Course (Google)](https://developers.google.com/machine-learning/crash-course) | Clear, visual, with exercises |
| [Kaggle Learn: Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) | Short hands-on lessons |
| [Kaggle Learn: Intermediate Machine Learning](https://www.kaggle.com/learn/intermediate-machine-learning) | Pipelines, cross-validation, leakage |
| [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html) | The reference. Read the sections as you need them. |
| [Rules of Machine Learning (Google)](https://developers.google.com/machine-learning/guides/rules-of-ml) | Practical wisdom from people who ship ML |
| [Machine Learning Specialization (DeepLearning.AI)](https://www.deeplearning.ai/courses/machine-learning-specialization/) | A well-known, structured course. Check the current terms for free access. |

## 🛡️ Responsible AI moment

Accuracy hides who the model fails. Whenever you report a score, ask: *which people or cases is it worst for?*

## ✅ Checkpoint

- Why do we need a test set, and why must we touch it only once?
- My model scores 97%. What are three questions I should ask before I believe it?
- A model for a rare problem (5% of cases) gets 95% accuracy. Is it good?
- What is data leakage? Give an example of how it can sneak in.
- When would I use recall as my main metric, and when precision?

[← Stage 1](01-foundations.md) · [Learning path overview](README.md) · [Stage 3 →](03-deep-learning.md)
