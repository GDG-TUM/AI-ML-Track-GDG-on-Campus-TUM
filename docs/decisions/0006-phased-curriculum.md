[← Back to decision records](README.md)

# 0006. A phased curriculum: six weeks on how machines learn, first

- **Status:** Accepted
- **Date:** 2026-10-05
- **Deciders:** Track Lead

## Context

The first draft of the curriculum was a single ten-week block with dates attached. It covered Python, classical ML, evaluation, neural networks, computer vision, language models, RAG, agents, responsible AI and deployment, with team projects starting in Week 4. That is many fields for beginners in ten sessions. Members would touch everything and understand little, and team projects would start before members had the basics to evaluate their own work. Fixed dates also went stale whenever a session moved for exams or campus events.

## Decision

- The track runs in **phases**, each with its own finish line.
- **Phase 1 is six weeks** and covers **three fields only**: data, classical ML and neural networks. Every Phase 1 session opens with **why the idea matters**. Phase 1 ends with a small **pair mini-project** presented at a showcase in Week 6.
- **Phase 2** (generative AI, responsible AI review, shipping, team projects and demo day) is planned **after** the Phase 1 retrospective, using what we learned.
- Plans list **week numbers, not dates**. A lost week simply pushes the sequence back.

## Alternatives considered

- **Keep the ten-week block:** more topics, but shallower, and the plan cannot respond to how the cohort is actually doing.
- **Start with generative AI because members are excited about it:** more exciting at first, but members cannot judge whether an LLM app works without the evaluation habits from Weeks 2 and 3.
- **Keep dates in the plan:** easier to read at a glance, but every rescheduled session makes the repo wrong.

## Consequences

- **Good:** deeper understanding of the fundamentals, a clear early win for members at Week 6, and a natural checkpoint to adjust the plan. The repo stays correct when sessions move.
- **Bad:** members wait until Week 7 for language models, and team projects get about four weeks instead of five.
- **Mitigations:** Week 4 and Week 5 explicitly connect the fundamentals to how LLMs work, and the Phase 1 mini-project gives everyone hands-on project practice before team projects start.
- **Revisit when:** after the Phase 1 retrospective, and at the start of each academic year.
