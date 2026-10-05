"""Tests for the starter project. Keep these green, and add your own as the project grows."""

from src.train import build_baseline, build_model, load_data, run


def test_data_has_matching_shapes():
    X, y = load_data()
    assert len(X) == len(y) > 0


def test_model_clearly_beats_the_baseline():
    # A broken pipeline fails loudly here instead of quietly reporting a bad score.
    results = run()
    assert results["model"]["macro_f1"] > results["baseline"]["macro_f1"] + 0.3


def test_results_are_reproducible():
    # Same seed, same answer. Anyone who clones the repo should see the same numbers.
    assert run(seed=0) == run(seed=0)


def test_model_returns_one_prediction_per_input():
    X, y = load_data()
    model = build_model().fit(X, y)
    assert len(model.predict(X[:7])) == 7


def test_baseline_is_not_secretly_good():
    # If the baseline is strong, the task may be too easy or the data may be leaking.
    X, y = load_data()
    baseline = build_baseline().fit(X, y)
    assert baseline.score(X, y) < 0.3
