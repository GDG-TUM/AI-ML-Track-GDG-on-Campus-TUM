[← Back to AI/ML Track home](../README.md)

# 🛡️ Responsible AI Checklist

Complete this for **every project** before the [Week 8 review](../docs/responsible-ai.md#review), and keep it updated. Answer honestly: **a ticked box with a thoughtful note beats a perfect-looking list**. Where a box does not apply, write "N/A" and why.

Project: ______________________  Team: ______________________  Date: ____________

## 🎯 Purpose

- [ ] I can say who this is for and how it helps them
- [ ] I considered whether a simpler, non-ML approach would do
- [ ] I wrote down **who could be harmed if it is wrong**, and how badly
- [ ] I checked the [high-stakes domains](../docs/responsible-ai.md) list, and my project is a prototype or an audit if it touches one
- [ ] I considered **misuse**: how could someone use this to cause harm?

## 📊 Data and consent

- [ ] I have the **right** to use all the data, and recorded licences and sources
- [ ] The data has **no personal information**, or I have clear, documented **consent** and a plan to protect it
- [ ] I have not committed personal data, secrets or large files
- [ ] I considered Kenya's Data Protection Act, 2019, and talked to a maintainer if personal data is involved
- [ ] I know **who is missing or over-represented** in the data, and wrote it in the [data card](../projects/_template/DATA_CARD.md)

## ⚖️ Fairness

- [ ] I chose **slices** that matter (language, region, gender where ethically available, device, lighting, accent, input length)
- [ ] I evaluated the model on **each slice** and counted the examples in each
- [ ] I recorded the **largest gap** and what I did, or could do, about it
- [ ] I did not assume that removing a sensitive column makes the model fair (other columns can stand in for it)
- [ ] I tested names, languages and examples **from outside my own group**

## 🔍 Transparency

- [ ] I wrote a [model card](../projects/_template/MODEL_CARD.md) with **intended use, out-of-scope use and limitations**
- [ ] The README says clearly **what the system is** and what it cannot do
- [ ] AI-generated content and AI interactions are **labelled** as such
- [ ] I credited datasets, models, libraries and people

## 🧯 Safety and reliability

- [ ] I tested **odd, extreme and empty inputs**
- [ ] I looked at **real failure cases** and listed the main failure modes
- [ ] A **human can review or override** decisions where the stakes are real
- [ ] The system **says when it is unsure** (or declines), instead of guessing confidently
- [ ] I considered cost, rate limits and abuse of any public demo

## ✨ If it uses a language model

- [ ] Answers are **grounded in sources** and **cite** them, or I explain why not
- [ ] I tested for **hallucination** with questions that have no answer
- [ ] I tested **prompt injection**, including text inside retrieved documents
- [ ] The model cannot take **irreversible or high-impact actions** without human approval
- [ ] No secrets or private data are placed in prompts that I do not control the destination of
- [ ] I tested prompts across **different names, languages and groups**

## 🧑‍🤝‍🧑 Accountability

- [ ] Named **owners** are responsible for the project and its documentation
- [ ] There is a way for a user to **report a problem**
- [ ] I know how to **shut it down**, and I wrote down when I would
- [ ] The team did a **red-team swap** and recorded the findings as issues

## 🗒️ Review outcome (filled in by reviewers)

| | |
|---|---|
| **Reviewers** | |
| **Date** | |
| **Outcome** | ☐ Approved  ☐ Approved with conditions  ☐ Needs changes |
| **Conditions and deadlines** | |
| **Notes** | |
