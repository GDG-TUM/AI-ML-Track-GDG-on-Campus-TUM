[← Back to AI/ML Track home](../README.md)

# 💡 Project Ideas

Pick one, adapt one, or propose your own. Smaller and finished beats bigger and abandoned. Every idea below should pass the **"who could be harmed?"** question, and each has a note on what to watch for.

> [!NOTE]
> Dataset names are starting points to search for, not guarantees. **Always check the licence and the source**, and use public, synthetic or properly consented data.

## 🌱 Beginner-friendly

- **Campus tabular predictor:** forecast something simple from a small table you collect yourselves (such as daily cafeteria sales) and compare a baseline with a model.
  *Watch for:* privacy if the data is about people, and leakage from "future" columns.
- **Digit or letter reader:** extend the Week 2 notebook to a webcam or photo demo.
  *Watch for:* it works on your handwriting, but whose else?
- **Objects classifier:** three kinds of local fruit, tools or crops from photos you take (the Week 5 approach).
  *Watch for:* photos of objects only, no people.
- **Kaggle starter squad:** a team that enters a Getting Started competition, documents everything and writes the best beginner walkthrough.
  *Watch for:* leaderboard overfitting.

## 🌿 Intermediate

- **Swahili text classifier:** sentiment, topic or spam detection on Swahili text from open community datasets (see [Masakhane](https://www.masakhane.io)).
  *Watch for:* dialects, code-switching with English and Sheng, and who wrote the training data.
- **Crop-disease photo classifier:** recognise leaf diseases from photos using a public plant-disease dataset (search Kaggle for *PlantVillage*), then test on **your own photos** to see the gap.
  *Watch for:* lab photos versus field photos, and never presenting it as expert advice.
- **Campus study assistant (RAG):** answer questions from notes and public documents you are allowed to use, **with citations**.
  *Watch for:* copyright, hallucinations and prompt injection.
- **Time series from open data:** forecast something like rainfall, prices or traffic from a public dataset, with a naive baseline first.
  *Watch for:* data quality, and over-trusting a forecast.
- **Model audit:** take a public model (sentiment, translation, image tagging) and test it across names, languages and groups. Publish what you find.
  *Watch for:* being fair and specific, and sharing findings kindly.

## 🔥 Advanced

- **Speech to text for Swahili:** fine-tune or evaluate an open speech model on public Swahili recordings (for example, [Common Voice](https://commonvoice.mozilla.org) has Swahili).
  *Watch for:* consent for voice data, accents and noise.
- **Small on-device model:** shrink an image or text model so it runs on a phone, and measure the accuracy you give up.
  *Watch for:* testing on real, low-end hardware.
- **Agent with tools and guardrails:** an assistant that can search, calculate and draft, with a human approving every action.
  *Watch for:* prompt injection, runaway cost and unsafe actions.
- **Active learning for local data:** build a labelling tool that picks the most useful examples to label next.
  *Watch for:* labeller wellbeing and label quality.

## 🌍 Local impact (talk to us first)

These touch higher-stakes domains. **Prototypes and audits are welcome. Deployment to real decisions is not.** See [high-stakes domains](../docs/responsible-ai.md).

- **Know-your-rights assistant:** answer questions from public legal texts with citations and a clear "this is not legal advice" notice.
- **Fraud-pattern explorer:** study mobile-money fraud patterns using a **synthetic** dataset (search Kaggle for *PaySim*), never real customer data.
- **Health information bot:** a retrieval bot over public health guidance, with strong disclaimers and a "see a professional" path.

## What makes a good project

- Solves a real problem for real people
- Can be built in about **5 weeks of part-time work**
- Has a **baseline** and a metric you can defend
- Has an honest answer to "who could be harmed?"
- Uses at least 3 skills from the track: honest evaluation, deep learning or LLMs, responsible AI, tests, a demo
- Can be demoed in **5 minutes**
