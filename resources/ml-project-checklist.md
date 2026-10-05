[← Back to AI/ML Track home](../README.md)

# ✅ ML Project Checklist

Review any project against this list before you share it, and again before demo day. Tick what is true, fix what is not. For fairness, privacy and safety, also use the [Responsible AI checklist](responsible-ai-checklist.md).

## 🎯 Problem

- [ ] I can state the problem and the user in **one sentence**
- [ ] I asked whether ML is the right tool, or whether a simple rule would do
- [ ] I know **what success looks like** and how it will be measured
- [ ] I know who is affected if it is wrong

## 📊 Data

- [ ] I know **where the data came from** and have the right to use it
- [ ] The **licence** is recorded in the [data card](../projects/_template/DATA_CARD.md)
- [ ] There is **no personal data** in the repo (and I have consent where it is used)
- [ ] I looked at the data with my own eyes: missing values, duplicates, odd rows
- [ ] I know who or what is **missing** from it
- [ ] Raw data is **not** committed. It is linked, and the download is documented.

## 🧪 Modelling and evaluation

- [ ] I have a **baseline**, and my model clearly beats it
- [ ] The **test set** was kept aside and used **once**
- [ ] All preprocessing is inside a **pipeline** (no leakage)
- [ ] I report **more than accuracy**, and the metric fits the real cost of mistakes
- [ ] I looked at **real mistakes**, not just averages
- [ ] I evaluated on **slices**, and I report gaps honestly
- [ ] I tried a simple model before a complicated one

## 🔁 Reproducibility

- [ ] **Seeds** are set
- [ ] `requirements.txt` is complete, and a teammate can install it from scratch
- [ ] **One command** reruns the main result
- [ ] Notebooks run **top to bottom**, and are committed without outputs
- [ ] Experiments are noted down: what I changed and what happened

## 🧰 Code quality

- [ ] Code moved from notebook cells into a small, importable package
- [ ] **Tests** exist and run in CI: shapes, sanity checks, edge cases
- [ ] Lint and format pass (`make check`)
- [ ] Functions are small, named well and documented

## 🚢 Delivery

- [ ] A **demo** runs, with a recorded **backup**
- [ ] The README lets a stranger understand and run the project
- [ ] The [model card](../projects/_template/MODEL_CARD.md) and data card are filled in truthfully
- [ ] **No secrets** in code, notebooks or history
- [ ] Hosted services have a **budget alert**, rate limits and a plan to shut them down
- [ ] A **licence** is chosen, and data and models credit their sources

## 🎤 Telling the story

- [ ] I can explain the project to a non-technical person in two minutes
- [ ] I can explain **what it gets wrong**, and what I would fix next
- [ ] My write-up includes what **did not** work
