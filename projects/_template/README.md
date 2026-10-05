> **How to use this template:** copy this whole folder to start your project, then replace the text below. Delete this box when you are done. Everything runs as it is, so you start with a working, tested skeleton, and **change one thing at a time**.
>
> 1. Copy the folder: `cp -r projects/_template ../my-project-name`
> 2. Replace `load_data()` in [`src/train.py`](src/train.py) with your own data loading
> 3. Keep the **baseline**. It is the number your model must beat.
> 4. Fill in the [model card](MODEL_CARD.md) and [data card](DATA_CARD.md) as you go, not at the end
> 5. Keep tests green: `pytest`

# Project Name

One sentence: what it does and who it is for.

## Demo

Link to the live app and/or a short recording.

## Problem

Who has this problem, and why does it matter to them?

## Approach

Plain-English description of the data, the model and why you chose it.

## Results

After you run `python -m src.train`, paste the numbers from `reports/metrics.json` here.

| Model | Accuracy | Macro F1 |
|-------|:-:|:-:|
| Baseline (most frequent) | | |
| Our model | | |

What does the model get wrong, and for whom?

## Run it

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python -m src.train              # trains the baseline and the model, writes reports/metrics.json
pytest                           # runs the tests
```

A teammate should be able to reproduce your main result from a fresh clone with exactly these commands.

## Project layout

```text
.
├── README.md          ← you are here
├── MODEL_CARD.md      ← what the model is for, how it was evaluated, its limits
├── DATA_CARD.md       ← where the data came from and what is in it
├── requirements.txt   ← the libraries you need
├── .env.example       ← names of secrets (never commit a real .env)
├── src/
│   └── train.py       ← load data, train baseline and model, evaluate, save metrics
├── tests/
│   └── test_train.py  ← tests that run in CI
└── reports/           ← metrics and figures written by the training script (not committed)
```

## Responsible AI

- **Who could be harmed if it is wrong?**
- **What data about people does it touch, and how is consent handled?**
- **Limits and what it should not be used for:** see the [model card](MODEL_CARD.md)
- **Review outcome and conditions:**

## Team

- Name ([@github-username](https://github.com/github-username)): role

## What we learned

Three to five bullet points, including what did not work.

## Next steps

What you would build next.

## Licence

MIT. Data and models carry their own licences, listed in the [data card](DATA_CARD.md) and [model card](MODEL_CARD.md).
