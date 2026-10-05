[← Back to AI/ML Track home](../../README.md)

# Week 5: Deep learning in practice

**Date:** Wed 11 Nov (draft; confirm time and venue in the track channel)

**Goal:** Fine-tune a pretrained image model on a free GPU, with a dataset you collect yourselves.

## Learning objectives

By the end you should be able to:

- Explain what a convolutional network looks for in an image
- Explain **transfer learning**: why we start from a pretrained model
- Turn on a free GPU in Colab, and train within its limits
- Load images from folders, train, evaluate and look at the mistakes
- Submit a project proposal

## Before the session

- [ ] Finish [Week 4](../week-04-neural-networks-from-scratch/README.md)
- [ ] Skim [Stage 3: Deep learning](../../learning-path/03-deep-learning.md) and the [Keras transfer learning guide](https://keras.io/guides/transfer_learning/)
- [ ] Take **30 photos each of 3 kinds of objects** with your phone (for example, three kinds of fruit, shoes or tools). **Objects, not people.** Bring them on your phone or a USB drive.

## Agenda

1. Arrive and set up: GPU runtime on, photos uploaded (10 min)
2. Goal and recap (5 min)
3. Concept: convolutions, pretrained models, fine-tuning (20 min)
4. Hands-on in pairs: train and evaluate your 3-class model (40 min)
5. 🛡️ Responsible AI moment (5 min)
6. Share-out, project proposal reminder, take-home challenge (10 min)

## Hands-on reference

We follow the official [Keras transfer learning and fine-tuning guide](https://keras.io/guides/transfer_learning/) and adapt it live. The outline:

1. In Colab: **Runtime → Change runtime type → GPU**. Availability and limits vary, so have a CPU plan too.
2. Put your photos in folders named after each class (`class_a/`, `class_b/`, `class_c/`).
3. Load them as a dataset with Keras, and split into training and validation.
4. Start from a **pretrained image model**, freeze it, and train a small new "head" on top.
5. Evaluate on photos the model has never seen. Look at the confusion matrix and the mistakes.
6. Optional: unfreeze a few top layers and **fine-tune** with a very small learning rate.

> [!TIP]
> Keep images small and the model small. A free GPU is generous but not unlimited, and **a session that is allowed to finish beats a clever one that times out**. See the [compute guide](../../resources/compute-guide.md).

## 🛡️ Responsible AI moment

Why do we collect photos of **objects, not people**? Faces and bodies are personal data, and pretrained models can carry biases from the data they learned from. **If a model works on your phone's photos, whose photos might it fail on?**

## 🏁 Take-home challenge

- [ ] Finish your 3-class model. How accurate is it on **new photos taken in different light**?
- [ ] Try one improvement (more photos, augmentation, fine-tuning) and report whether it helped
- [ ] **Submit your project proposal** by the end of this week using the [Project proposal form](https://github.com/GDG-TUM/AI-ML-Track-GDG-on-Campus-TUM/issues/new/choose)
- [ ] Optional: the Cloud Track is preparing for the Google Kenya hackathon on 13 Nov. If you want to join a team, check the official rules and talk to the leads.

## 📝 Session notes

Add slides, links, recordings and key takeaways here after the session (via pull request).

- Slides: *to be added*
- Recording: *to be added*
- Extra resources: *to be added*

---
[← Week 4](../week-04-neural-networks-from-scratch/README.md) | [All sessions](../README.md) | [Week 6 →](../week-06-language-models-and-gemini/README.md)
