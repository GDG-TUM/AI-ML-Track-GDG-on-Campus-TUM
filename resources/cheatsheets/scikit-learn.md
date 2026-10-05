[← Back to AI/ML Track home](../../README.md)

# scikit-learn Cheat Sheet

## The standard workflow

```python
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import classification_report

# 1. Split. Hide the test set until the very end.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=0
)

# 2. Baseline first
baseline = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)

# 3. A real model, with preprocessing INSIDE the pipeline (no leakage)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))
model.fit(X_train, y_train)

# 4. Evaluate on the test set once
print(baseline.score(X_test, y_test), model.score(X_test, y_test))
print(classification_report(y_test, model.predict(X_test)))
```

## The three verbs

| Verb | Does |
|---|---|
| `model.fit(X, y)` | Learn from training data |
| `model.predict(X)` | Guess for new data |
| `model.score(X, y)` | Default score (accuracy for classifiers, R² for regressors) |

## Cross-validation and tuning

```python
from sklearn.model_selection import cross_val_score, GridSearchCV

scores = cross_val_score(model, X, y, cv=5)
print(scores.mean(), scores.std())

grid = GridSearchCV(model, {"logisticregression__C": [0.1, 1, 10]}, cv=5)
grid.fit(X_train, y_train)        # tunes using only the training data
grid.best_params_
```

## Which model to try first?

| Task | Start with | Then try |
|---|---|---|
| Classification | `LogisticRegression` | `RandomForestClassifier`, `HistGradientBoostingClassifier` |
| Regression | `LinearRegression` or `Ridge` | `RandomForestRegressor`, `HistGradientBoostingRegressor` |
| Clustering | `KMeans` | `DBSCAN`, `AgglomerativeClustering` |
| Text | `TfidfVectorizer` + `LogisticRegression` | An embedding model |

## Choosing a metric

| Situation | Look at |
|---|---|
| Balanced classes, equal cost of errors | Accuracy |
| Rare positive class | Precision, recall, F1, PR curve |
| Missing a case is very costly | **Recall** |
| False alarms are very costly | **Precision** |
| Regression | MAE (easy to explain), RMSE (punishes big errors) |
| Always | The **confusion matrix** and real mistakes |

```python
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, confusion_matrix, ConfusionMatrixDisplay,
                             mean_absolute_error)
ConfusionMatrixDisplay.from_estimator(model, X_test, y_test)
```

## Common mistakes

| Mistake | Fix |
|---|---|
| Scaling or selecting features on **all** data before splitting | Put it in a `Pipeline` |
| Tuning on the test set | Use cross-validation on the training set |
| Reporting only accuracy on imbalanced data | Add precision, recall and F1 |
| Random split when data has time or groups | Split by time or use `GroupKFold` |
| Forgetting `random_state` | Set it so results repeat |
| Using the label (or a stand-in for it) as a feature | Ask of every column: *would I know this at prediction time?* |
