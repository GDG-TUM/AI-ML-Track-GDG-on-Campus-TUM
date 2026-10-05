[← Back to AI/ML Track home](../README.md)

# 🚀 Projects

From week 4, members form teams of **3 to 5** and build a project that is **reproducible, honestly evaluated, reviewed for responsible AI and demoed** on demo day (16 Dec).

Smaller and finished beats bigger and abandoned.

## What every project needs

- [ ] A public repo in the GDG-TUM org (or a member's account, linked in the showcase)
- [ ] A clear `README` (use the [project template](project-template.md) or start from the [starter template](_template/README.md))
- [ ] A **baseline** and an honest evaluation against it
- [ ] A **model card** and a **data card**
- [ ] A completed [responsible AI checklist](../resources/responsible-ai-checklist.md) and a passed review
- [ ] A reproducible environment and **tests** that run in CI
- [ ] A **demo**: a live app, a hosted demo or a recording
- [ ] No secrets, no personal data and no large files in the repo
- [ ] A short write-up of what the team learned, including what did not work

The full checklist, with the three review gates, is in the [project lifecycle](../docs/project-lifecycle.md).

## How to start

1. Read the [project ideas](ideas.md) and pitch yours in [Week 4](../weekly-sessions/week-04-neural-networks-from-scratch/README.md)
2. Form a team (week 4 to 5)
3. Open a **Project proposal** issue: [propose a project](https://github.com/GDG-TUM/AI-ML-Track-GDG-on-Campus-TUM/issues/new/choose). The form asks about data, metric, baseline and risks.
4. Two maintainers review it within a week (**Gate A**)
5. Create your repo from the [starter template](_template/README.md) and start building
6. Meet your mentor weekly (see [mentorship](../docs/mentorship.md))

## Timeline

| Week | Milestone |
|------|-----------|
| 4 | Pitch given, team forming |
| 5 | Proposal approved (**Gate A**), repo created |
| 6 | Data in hand, data card started |
| 7 | Baseline and honest evaluation (**Gate B**) |
| 8 | Model card, checklist and red-team (**Gate C**) |
| 9 | Tests pass in CI, demo works, project clinic |
| 10 | Demo day |

## The starter template

[`_template/`](_template/README.md) is a small, working project: a data-to-metrics script, a baseline versus a model, a test that runs in CI, a model card and a data card. Copy the folder, replace the data loading, and you already have a reproducible skeleton.

```bash
cp -r projects/_template ../my-project-name
cd ../my-project-name
pip install -r requirements.txt
python -m src.train
pytest
```

## Showcase

Finished projects are listed in the [showcase](showcase.md).

## Ground rules

- Read the [Responsible AI guide](../docs/responsible-ai.md) before you choose your data
- Credit data, models and people. Check licences.
- Never commit secrets or personal data
