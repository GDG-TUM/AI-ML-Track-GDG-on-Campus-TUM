[← Back to AI/ML Track home](../README.md)

# Stage 3: Deep Learning

**Goal:** Understand how a neural network learns, then fine-tune a pretrained one on a free GPU.

**Matching sessions:** [Week 4: Neural networks from scratch](../weekly-sessions/week-04-neural-networks-from-scratch/README.md) and [Week 5: Deep learning in practice](../weekly-sessions/week-05-deep-learning-in-practice/README.md)

## What you will learn

- Neurons, layers, weights and biases, and activation functions
- The **loss**, the **gradient** and **gradient descent**
- **Backpropagation**: the chain rule, in code
- Convolutional neural networks for images
- **Transfer learning**: standing on the shoulders of pretrained models
- Using a free GPU, and keeping training runs small and honest
- Overfitting in deep learning: augmentation, early stopping, regularisation

## Hands-on

1. Run the [Week 4 notebook](../weekly-sessions/week-04-neural-networks-from-scratch/neural_net_from_scratch.ipynb) and do the experiments in its challenge.
2. In Week 5, fine-tune a pretrained image model on a small dataset you collect yourself.
3. Start your Phase 1 mini-project (Week 4) and present it at the [Phase 1 showcase](../weekly-sessions/week-06-phase-1-showcase/README.md) (Week 6).

## Free resources

| Resource | What it is |
|---|---|
| [3Blue1Brown: Neural networks](https://www.3blue1brown.com/topics/neural-networks) | The best visual explanation of what a network is doing |
| [Neural Networks: Zero to Hero (Karpathy)](https://karpathy.ai/zero-to-hero.html) | Build backprop and a language model from scratch |
| [Keras: getting started](https://keras.io/getting_started/) | Our guided-lab framework |
| [Keras: transfer learning and fine-tuning](https://keras.io/guides/transfer_learning/) | The pattern you will use in Week 5 |
| [Practical Deep Learning for Coders (fast.ai)](https://course.fast.ai/) | Top-down, code first |
| [PyTorch tutorials](https://pytorch.org/tutorials/) | If you prefer PyTorch (welcome in projects) |
| [Dive into Deep Learning](https://d2l.ai) | A free interactive textbook |

## 🛡️ Responsible AI moment

Your photos are your dataset. Who is in them, and did they agree? **No photos of people without clear consent.** Pretrained models also carry the biases of the data they were trained on.

## ✅ Checkpoint

- What is a loss function, and what does the gradient tell me?
- Why does a network need an activation function between layers?
- What happens to training if the learning rate is far too big? Too small?
- Why is fine-tuning a pretrained model usually better than training from scratch with little data?
- How do I know my network is overfitting?

[← Stage 2](02-core-ml.md) · [Learning path overview](README.md) · [Stage 4 →](04-generative-ai.md)
