[← Back to AI/ML Track home](../README.md)

# Stage 4: Generative AI

**Goal:** Build a useful, honest app on top of a large language model.

**Matching sessions:** [Week 6: Language models and Gemini](../weekly-sessions/week-06-language-models-and-gemini/README.md) and [Week 7: RAG and agents study jam](../weekly-sessions/week-07-rag-and-agents-study-jam/README.md)

## What you will learn

- How language models work at a high level: **tokens**, **embeddings**, **attention**, **context windows**
- **Prompting** patterns: role, examples, constraints, output format
- Settings that change behaviour, such as temperature
- Using the **Gemini API** safely (keys, costs and rate limits)
- **Retrieval-augmented generation (RAG)**: chunking, embeddings, search, citations
- **Agents**: a model plus tools, instructions and a loop
- **Evaluating** LLM apps with small test sets, not vibes
- Limits and risks: hallucination, prompt injection, cost, privacy

## Hands-on

1. Experiment in [Google AI Studio](https://aistudio.google.com), then export your prompt as code and run it in Colab.
2. Build a small question-answering bot over a few pages of course notes, **with citations**.
3. Write ten test questions and score your bot's answers. Where does it fail?

## Free resources

| Resource | What it is |
|---|---|
| [Google AI Studio](https://aistudio.google.com) | A playground and key manager for Gemini |
| [Gemini API documentation](https://ai.google.dev/gemini-api/docs) | Quickstarts, guides and current model names |
| [Prompt design strategies (Gemini API)](https://ai.google.dev/gemini-api/docs/prompting-strategies) | Practical prompting guidance |
| [Gemma open models](https://ai.google.dev/gemma) | Open-weight models you can run and study |
| [Hugging Face LLM course](https://huggingface.co/learn/llm-course) | How transformers and LLMs work, with code |
| [Hugging Face agents course](https://huggingface.co/learn/agents-course) | Building agents, step by step |
| [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | The paper that introduced the transformer (read the abstract and figures) |
| [Cloud Track: AI on the cloud](https://github.com/GDG-TUM/Cloud-Track-GDG-on-Campus-TUM/blob/main/learning-path/06-ai-on-cloud.md) | Agents and deployment on Google Cloud |

> [!NOTE]
> Model names, free-tier limits and SDK details change often. Always follow the **current** official documentation rather than a tutorial that is a few months old.

## 🛡️ Responsible AI moment

LLMs sound confident when they are wrong. Always ask: **how would a user know this answer is wrong?** Show sources, say when you are unsure, and never let a model take irreversible actions on its own.

## ✅ Checkpoint

- What is a token, and why does it matter for cost and limits?
- Why does RAG reduce hallucinations, and when does it not?
- What is prompt injection, and how could it affect my app?
- How would I measure whether my prompt change made the bot better?
- What could go wrong if an agent has too many permissions?

[← Stage 3](03-deep-learning.md) · [Learning path overview](README.md) · [Stage 5 →](05-responsible-ai.md)
