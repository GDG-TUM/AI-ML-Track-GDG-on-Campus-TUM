# Model Card

> A model card tells people what a model is for, how well it works and where it fails. Fill it in **truthfully**: limitations are the most useful part. Format inspired by [Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993).

## Model details

- **Name and version:**
- **Date:**
- **Authors:**
- **Model type:** (for example, logistic regression, fine-tuned image model, prompted LLM)
- **Libraries and versions:**
- **Licence:**
- **Contact:**

## Intended use

- **Primary intended use:** *What is it for, and who is it for?*
- **Intended users:**
- **Out-of-scope uses:** *What should it NOT be used for?* Be specific.

## Training data

- *Where it came from, how much of it there is and what it covers. Link the [data card](DATA_CARD.md).*

## Evaluation

- **Task and metric:** (and why this metric)
- **Baseline:** (what a simple approach scores)
- **How we evaluated:** (split, cross-validation, test set used once)

| Model | Metric | Score |
|-------|--------|-------|
| Baseline | | |
| This model | | |

### Results by group

Overall scores hide who the model fails. Report results by the slices that matter for this project (language, region, device, lighting, accent, input length and so on).

| Group | Number of examples | Score |
|-------|:-:|-------|
| | | |
| | | |

**Largest gap between groups:**

## Ethical considerations

- **Who could be harmed if it is wrong, and how?**
- **Personal data and consent:**
- **Bias risks we know about:**
- **How we tried to reduce them:**

## Caveats and recommendations

- **Known failure modes:** *Real examples of what goes wrong.*
- **Conditions where it should not be trusted:**
- **What a user should do when unsure:** (for example, check with a person)
- **Ideas to improve it:**
