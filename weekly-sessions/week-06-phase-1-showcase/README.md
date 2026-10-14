[← Back to AI/ML Track home](../../README.md)

# Week 6: Phase 1 showcase

**When:** Phase 1, week 6. Time and venue are posted in the track channel.

**Field:** all three (📊 Data · 🧮 Classical ML · 🧠 Neural networks)

**Goal:** Present your mini-project, explain why you trust (or do not trust) your results, and close Phase 1.

**Today's question:** *Would you trust your own model with a real decision?*

## 💡 Why this matters

Running a notebook is not the same as understanding it. The moment someone asks *"why?"*, you find out which parts you really understand. Explaining your work proves to yourself that you learned it, and it is a skill you will use in every interview, report and team meeting.

## Learning objectives

By the end you should be able to:

- Walk through a complete ML workflow on your own data: data, baseline, model, honest evaluation, risk
- Explain **why** each step is there, not just what you did
- Ask good "why" questions about someone else's model
- Say what you want to build in Phase 2

## Before the session

- [ ] Finish your **mini-project** with your partner (see below)
- [ ] Prepare a **3-minute** presentation: your notebook on screen is enough, slides are optional
- [ ] Rehearse once with a timer
- [ ] Answer the [Stage 1](../../learning-path/01-foundations.md), [Stage 2](../../learning-path/02-core-ml.md) and [Stage 3](../../learning-path/03-deep-learning.md) checkpoint questions in your own words, on paper

## 🧭 Phase 1 in one picture

Every week added one idea to the one before. Your mini-project uses all of them:

| Week | The puzzle | The one idea to keep | In your mini-project |
|:-:|---|---|---|
| 1 | How much tea to make tomorrow? | A **model** has **knobs**; **training** turns them to lower the **loss** | The data and one chart |
| 2 | Can a computer read handwriting? | Test on examples the model **never saw**, and compare with a **baseline** | Baseline and model |
| 3 | How did a random guesser score 80%? | Choose on **validation**, touch the test set **once**, keep every step in a **Pipeline**, look beyond accuracy | Honest evaluation |
| 4 | How does a network with billions of knobs learn? | **Gradient descent** and **backpropagation**: feel the slope, step downhill | Knowing what `fit` really does |
| 5 | Can 90 photos train an image model? | Start from a **pretrained** model | (if you chose photos) |
| All | Who is missing from the data? | **Whatever is missing from the data is missing from the model**, and confidence is not knowledge | One risk |

## The mini-project

Pairs, one dataset, about **3 hours of work in total**, started in [Week 4](../week-04-neural-networks-from-scratch/README.md). Extending the Week 3 Titanic model or the Week 5 photo classifier is completely fine.

Your notebook (and your 3 minutes) must show these five things:

| # | Show | The question it answers |
|:-:|---|---|
| 1 | **The data:** what it is, where it came from, one chart | Do I understand what I am modelling? |
| 2 | **A baseline** score | What does "doing nothing smart" get? |
| 3 | **A model** that beats it | Did the model learn anything? |
| 4 | **Honest evaluation:** validation or cross-validation, more than accuracy, three real mistakes | Should anyone believe the score? |
| 5 | **One risk:** who could be hurt if this were used for real | Should this be used at all, and how? |

> [!TIP]
> A model that **did not** beat the baseline is a perfectly good mini-project, as long as you explain what you tried and what you learned. Honest beats impressive.

## Agenda

1. Arrive and set up: laptops connected, presentations in order (10 min)
2. Goal and how the session works (5 min)
3. **Mini-project presentations:** 3 minutes plus 2 minutes of questions per pair (about 45 min)
4. **"Why does it matter?"** Group discussion: what changed in how you think about AI since Week 1? (10 min)
5. 🛡️ Responsible AI moment (5 min)
6. **Phase 1 retrospective and a Phase 2 preview** (15 min)

## Hands-on reference

### The 3-minute presentation

| Time | What |
|:-:|---|
| 0:00 | The data and the question you asked of it |
| 0:30 | Your baseline, your model, and the gap between them |
| 1:15 | How you know the score is honest, and one mistake the model made |
| 2:15 | Who could be hurt, and what you would do about it |
| 2:45 | One thing you learned |

### Questions to ask other pairs

- What was your baseline, and how much did you beat it by?
- How do you know nothing leaked from the test data?
- Which mistake surprised you most?
- Would you trust this model with a real decision? Why or why not?

### Retrospective (the whole group)

| What helped you learn? | What got in the way? | What do you want in Phase 2? |
|---|---|---|
| | | |

Your answers shape [Phase 2](../../roadmap/semester-roadmap.md).

## 🛡️ Responsible AI moment

Look back at the five risks the pairs presented. **Which one worries you most, and what would it take to fix it?** Phase 2 includes a full responsible AI review of every team project.

## 🏁 Take-home challenge

- [ ] Push your mini-project notebook to your own GitHub, with a short README that covers the five things above
- [ ] Give [session feedback](https://github.com/GDG-TUM/AI-ML-Track-GDG-on-Campus-TUM/issues/new/choose) on Phase 1 as a whole
- [ ] Write down **one problem** you would like to work on in Phase 2. Team projects are pitched in [Week 7](../week-07-language-models-and-gemini/README.md).
- [ ] Update your Member Roadmap issue: tick Phase 1 and write one sentence on what you understand now that you did not in Week 1

<details>
<summary><b>🎤 Host guide: running the showcase</b></summary>

<br/>

**Before.** Collect notebook links the day before and open them all in tabs, so no time is lost switching laptops. Agree the order. Pairs who are nervous often prefer to go second or third.

**Set the tone (2 min).** Say it out loud: *"A model that didn't beat its baseline, explained honestly, is a great presentation. We're here to ask why, not to judge."*

**Timekeeping.** Show a visible timer. Give a gentle signal at 2:30 and stop at 3:00. Questions are 2 minutes, and the host asks one if the room is quiet.

**Questions the host can always ask**

| If they showed... | Ask |
|---|---|
| A high score | "What does guessing score? How do you know nothing leaked?" |
| A low score | "What did you try, and what would you try next?" |
| A chart | "What surprised you in it?" |
| A risk | "Who would notice if the model got this wrong?" |

**The "why does it matter?" discussion.** Put the Phase 1 in one picture table on screen and ask each person to point at the one idea that changed how they see AI.

**Retrospective.** Use three sticky notes per person (helped, got in the way, want in Phase 2), and group them on a wall. Photograph the wall for the notes PR.

</details>

## 📝 Session notes

Add slides, links, recordings and key takeaways here after the session (via pull request).

- Slides: *to be added*
- Recording: *to be added*
- Extra resources: *to be added*

---
[← Week 5](../week-05-deep-learning-in-practice/README.md) | [All sessions](../README.md) | [Week 7 →](../week-07-language-models-and-gemini/README.md)
