[← Back to decision records](README.md)

# 0004. scikit-learn, then Keras for guided labs, PyTorch welcome

- **Status:** Accepted, revisit each semester
- **Date:** 2026-10-05
- **Deciders:** Track Lead

## Context

Deep learning has several good frameworks. Teaching all of them at once would confuse beginners, but locking members into one would limit them, since PyTorch is dominant in research and many job listings. We are a Google Developer Group chapter and want a gentle on-ramp.

## Decision

- **Classical ML:** scikit-learn throughout (Weeks 2 and 3).
- **Understanding:** one neural network from scratch in NumPy (Week 4), so no framework feels like magic.
- **Guided deep learning labs:** **Keras 3** (Week 5). It has a gentle API and, in Keras 3, runs on JAX, TensorFlow or PyTorch backends.
- **Projects:** teams may use **any framework**, including PyTorch. Mentors help where they can.
- **Generative AI:** the Gemini API and open Gemma models, plus Hugging Face tools.

## Alternatives considered

- **PyTorch only:** the strongest industry and research signal, but a steeper first hour. We keep it fully supported for projects.
- **TensorFlow only:** more tied to one vendor's ecosystem, and its role has shifted over time.
- **No default:** every session would spend its time on setup choices.

## Consequences

- **Good:** a single, gentle path for beginners, with freedom for those who want more.
- **Bad:** members who want PyTorch in the guided labs wait until projects or self-study. Some mentors may not know Keras.
- **Revisit when:** each semester, using session feedback, project choices and the job landscape. This record is expected to be **superseded** as tools evolve.
