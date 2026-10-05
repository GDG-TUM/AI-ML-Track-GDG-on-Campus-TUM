"""Train a baseline and a model, evaluate them honestly and save the results.

Run from the project root:

    python -m src.train

This is a starter. The digits dataset below is a stand-in: replace ``load_data`` with your
own data loading, and keep everything else's shape (one function per job, fixed seed, a
baseline next to the model, metrics written to ``reports/``).
"""

from __future__ import annotations

import json
from pathlib import Path

from sklearn.datasets import load_digits
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

SEED = 0
REPORTS_DIR = Path(__file__).resolve().parent.parent / "reports"


def load_data():
    """Return features X and labels y.

    TODO: replace this with your own data. Read from a path or a download you document in
    DATA_CARD.md. Never commit personal data or large files.
    """
    return load_digits(return_X_y=True)


def build_baseline():
    """The dumbest sensible model. Your real model must clearly beat it."""
    return DummyClassifier(strategy="most_frequent")


def build_model():
    """Your model. Preprocessing lives inside the pipeline so nothing leaks from the test set."""
    return make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))


def evaluate(model, X_test, y_test) -> dict[str, float]:
    """Report more than one metric. Accuracy alone can mislead."""
    predictions = model.predict(X_test)
    return {
        "accuracy": round(float(accuracy_score(y_test, predictions)), 4),
        "macro_f1": round(float(f1_score(y_test, predictions, average="macro")), 4),
    }


def run(seed: int = SEED) -> dict[str, dict[str, float]]:
    """Split the data, fit the baseline and the model on the same split, and score both."""
    X, y = load_data()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, stratify=y, random_state=seed
    )
    results = {}
    for name, model in {"baseline": build_baseline(), "model": build_model()}.items():
        model.fit(X_train, y_train)
        results[name] = evaluate(model, X_test, y_test)
    return results


def main() -> None:
    results = run()
    REPORTS_DIR.mkdir(exist_ok=True)
    (REPORTS_DIR / "metrics.json").write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(results, indent=2))
    print(f"\nSaved to {REPORTS_DIR / 'metrics.json'}")


if __name__ == "__main__":
    main()
