[← Back to AI/ML Track home](../README.md)

# 📖 Glossary

Plain-English definitions. Missing a term? [Open a pull request](../CONTRIBUTING.md) and add it. Explaining a term in Swahili as well is very welcome.

| Term | Meaning |
|------|---------|
| **Accuracy** | The share of predictions that are correct. Easy to understand, easy to be fooled by (see *Baseline*). |
| **Activation function** | A small bend (like tanh or ReLU) applied between layers so a network can learn curves, not just straight lines. |
| **Agent** | A system where a language model decides which tool to use, uses it, reads the result, and repeats until the task is done. |
| **Attention** | The mechanism in a transformer that lets the model weigh which parts of the input matter for each part of the output. |
| **Backpropagation** | How a neural network works out how to adjust every weight: the chain rule applied backwards from the loss. |
| **Baseline** | A deliberately simple model, such as "always guess the most common answer". Your real model must clearly beat it. |
| **Bias** | Two meanings. In **statistics**, a systematic error. In **fairness**, a model performing worse or unfairly for some groups. Say which one you mean. |
| **Classification** | Predicting a category: spam or not spam, which digit, which disease. |
| **Confusion matrix** | A table of true labels against predictions, showing exactly which classes get mixed up. |
| **Context window** | The amount of text a language model can consider at once, measured in tokens. |
| **Cross-validation** | Splitting data several ways, training on some parts and testing on the rest, then averaging. A fairer exam than a single split. |
| **Data card** | A short document describing a dataset: source, licence, consent, contents and known gaps. |
| **Data leakage** | When information from the test set (or the future) sneaks into training, making scores look better than they really are. |
| **Dataset** | A collection of examples a model learns from or is tested on. |
| **Deep learning** | Machine learning with neural networks that have many layers. |
| **Embedding** | A list of numbers that represents the meaning of a word, sentence or image, so similar things end up close together. |
| **Epoch** | One full pass through the training data. |
| **F1 score** | One number that balances precision and recall. |
| **Feature** | One measurement or input column the model learns from (for example, the rain in millimetres). |
| **Fine-tuning** | Taking a pretrained model and training it a little more on your own data. |
| **Generative AI** | Models that create new content, such as text, images, audio or code. |
| **Gradient** | The direction and size of the change that would most reduce the loss, for each weight. |
| **Gradient descent** | Repeatedly nudging weights against the gradient to reduce the loss. |
| **Hallucination** | When a language model states something false in a confident, fluent way. |
| **Hyperparameter** | A setting you choose before training (like learning rate or tree depth), as opposed to a weight the model learns. |
| **Inference** | Using a trained model to make predictions. |
| **Label** | The correct answer for an example, which the model tries to predict. |
| **Learning rate** | How big a step gradient descent takes. Too big and training explodes. Too small and it crawls. |
| **LLM (large language model)** | A very large neural network trained on huge amounts of text to predict the next token. |
| **Loss** | A single number measuring how wrong the model is. Training tries to make it smaller. |
| **Machine learning** | Getting computers to find patterns in examples instead of following rules written by hand. |
| **Model** | The thing that has learned from data and can make predictions. |
| **Model card** | A short document describing a model: what it is for, how it was tested, its limits and risks. |
| **Neural network** | A model made of layers of simple units whose connections (weights) are learned from data. |
| **Overfitting** | A model that memorises its training data and fails on new data. Training score high, validation score low. |
| **Parameter (weight)** | A number inside the model that is learned during training. |
| **Pipeline** | A chain of steps (scaling, selecting, modelling) treated as one unit, which stops leakage between training and testing. |
| **Precision** | When the model says "yes", how often is it right? |
| **Prompt** | The instructions and input you give a language model. |
| **Prompt injection** | Hidden or malicious text that tricks a language model into ignoring its instructions. |
| **RAG (retrieval-augmented generation)** | Looking up relevant documents first, then asking the model to answer using them, ideally with citations. |
| **Recall** | Of all the real "yes" cases, how many did the model catch? |
| **Regression** | Predicting a number: a price, a temperature, a score. |
| **Slice** | A subset of your data (for example, one language or region) used to check whether the model works for everyone. |
| **Supervised learning** | Learning from examples that come with the right answers (labels). |
| **Temperature** | A setting that controls how adventurous a language model's word choices are. Low is predictable, high is varied. |
| **Test set** | Data hidden until the very end, used once to estimate how the model will do on new data. |
| **Token** | A piece of text (a word or part of a word) that a language model reads and writes. Cost and limits are counted in tokens. |
| **Training set** | The data a model learns from. |
| **Transfer learning** | Starting from a model already trained on a big task, then adapting it to yours. |
| **Transformer** | The neural network design behind modern language models, built around attention. |
| **Underfitting** | A model too simple to capture the pattern. It does poorly even on training data. |
| **Unsupervised learning** | Finding structure in data without labels, such as grouping similar items. |
| **Validation set** | Data used to choose settings and compare models during development, kept separate from the test set. |
