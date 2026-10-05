[← Back to AI/ML Track home](../../README.md)

# Week 7: Language models and Gemini

**When:** Phase 2 (draft), week 7. Time and venue are posted in the track channel.

**Goal:** Understand how language models behave, prompt them well and call the Gemini API without leaking a key.

## Learning objectives

By the end you should be able to:

- Explain tokens, context windows and temperature, and why they matter for cost and quality
- Use prompting patterns: role, examples, constraints and output format
- Create an API key and store it **safely** (Colab Secrets or an environment variable)
- Call the Gemini API from Colab
- Test a prompt with a small, honest test set instead of trusting one good answer

## Before the session

- [ ] Finish [Phase 1](../week-06-phase-1-showcase/README.md)
- [ ] Skim [Stage 4: Generative AI](../../learning-path/04-generative-ai.md)
- [ ] Have your Google account ready for [Google AI Studio](https://aistudio.google.com). **Do not create a key yet.** We do it together, with safe storage.

## Agenda

1. Arrive and set up (10 min)
2. Goal and recap (5 min)
3. Concept: how language models work at a high level, and how to prompt (20 min)
4. Hands-on in pairs: AI Studio, then the same prompt in Colab via the API (40 min)
5. 🛡️ Responsible AI moment: the hallucination test (5 min)
6. Share-out and take-home challenge (10 min)

## Hands-on reference

1. **Play in [Google AI Studio](https://aistudio.google.com).** Try the same task with a vague prompt, then a precise one. Change the temperature and watch what happens.
2. **Create an API key** in AI Studio.
3. **Store it safely** in Colab: open the **🔑 Secrets** panel in the left sidebar, add a secret named `GEMINI_API_KEY`, and read it in code. Never paste a key into a cell.
4. **Follow the current [Gemini API quickstart](https://ai.google.dev/gemini-api/docs)** in Colab. Model names and SDK details change often, so use the official docs rather than an old tutorial.
5. Build a **test set**: 10 inputs with the answers you would accept, and score the model's outputs.

**A prompt template to start from:**

```text
You are a <role> helping <audience>.
Task: <what to do>
Rules: <constraints, tone, length>
Format: <exactly how the answer should look>
Examples: <one or two input and output pairs>
Input: <the thing to process>
```

More patterns in the [prompting cheat sheet](../../resources/cheatsheets/prompting.md).

> [!WARNING]
> **If a key ever lands in GitHub, revoke it immediately.** See the [security policy](../../SECURITY.md). Check current free-tier limits on the official site before you rely on them.

## 🛡️ Responsible AI moment

**The hallucination test.** Ask the model about something that *does not exist*, such as a made-up campus event or a fake research paper. Does it admit it does not know, or invent a confident answer? How would a user tell the difference?

## 🏁 Take-home challenge

- [ ] Write a prompt for a task you care about (for example, summarising lecture notes into questions) and a **10-case test set**. Score your outputs and improve the prompt. Did your score go up?
- [ ] Find **one failure** and explain why you think it happened
- [ ] **Team projects:** post your idea in the track channel, form a team of 3 to 5 and open a [Project proposal](https://github.com/GDG-TUM/AI-ML-Track-GDG-on-Campus-TUM/issues/new/choose) issue (**Gate A**)
- [ ] Run `git grep -i "AIza"` in any repo you have been working in, to make sure no key is hiding. Then check `.gitignore` includes `.env`.

## 📝 Session notes

Add slides, links, recordings and key takeaways here after the session (via pull request).

- Slides: *to be added*
- Recording: *to be added*
- Extra resources: *to be added*

---
[← Week 6](../week-06-phase-1-showcase/README.md) | [All sessions](../README.md) | [Week 8 →](../week-08-rag-and-agents-study-jam/README.md)
