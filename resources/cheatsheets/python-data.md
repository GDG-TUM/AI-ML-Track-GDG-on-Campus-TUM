[← Back to AI/ML Track home](../../README.md)

# Python for Data Cheat Sheet

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

## NumPy

```python
a = np.array([1, 2, 3])            # make an array
np.arange(0, 10, 2)                # 0, 2, 4, 6, 8
np.linspace(0, 1, 5)               # 5 evenly spaced numbers from 0 to 1
np.zeros((2, 3))                   # 2 rows x 3 columns of zeros
a.shape, a.dtype                   # size and type

a + 5; a * 2; a ** 2               # maths on every element at once
a.mean(); a.std(); a.sum()         # summaries
a > 1                              # True/False for each element
a[a > 1]                           # keep only matching elements

X.mean(axis=0)                     # mean of each column
X.sum(axis=1)                      # sum of each row
X @ W                              # matrix multiplication
X.reshape(-1, 8)                   # change shape (-1 = work it out)

rng = np.random.default_rng(0)     # repeatable randomness
rng.normal(0, 1, size=100)         # 100 numbers from a normal distribution
```

## pandas

```python
df = pd.read_csv("file.csv")       # load a table
df.head(); df.tail()               # first / last rows
df.shape                           # (rows, columns)
df.info()                          # columns, types, missing values
df.describe()                      # summary statistics

df["col"]                          # one column (a Series)
df[["a", "b"]]                     # several columns
df[df["age"] > 18]                 # filter rows
df.loc[row_label, "col"]           # by label
df.iloc[0:5, 0:2]                  # by position

df["new"] = df["a"] * 2            # add a column
df.drop(columns=["col"])           # remove a column
df.rename(columns={"old": "new"})

df.isna().sum()                    # missing values per column
df.dropna(); df.fillna(0)          # drop or fill missing values
df.duplicated().sum()              # how many duplicate rows

df["col"].value_counts()           # count each value
df.groupby("group")["score"].mean()                 # average by group
df.groupby("group")["score"].agg(["mean", "count"]) # several summaries
df.sort_values("score", ascending=False)
df.corr(numeric_only=True)         # correlations

pd.get_dummies(df, columns=["category"])            # one-hot encode
df.to_csv("out.csv", index=False)  # save
```

## matplotlib

```python
plt.figure(figsize=(6, 4))
plt.plot(x, y)                     # line
plt.scatter(x, y, alpha=0.6)       # points
plt.hist(values, bins=20)          # distribution
plt.bar(labels, heights)           # bars
plt.xlabel("x label"); plt.ylabel("y label"); plt.title("Title")
plt.legend()
plt.tight_layout()
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(10, 4))     # side by side
axes[0].scatter(x, y)
axes[1].hist(values)
```

## Good habits

- **Look at the data first**: `head()`, `describe()`, a plot. Always.
- **Set seeds** so results repeat.
- **Never trust a number you have not plotted.**
- Keep raw data untouched. Do cleaning in code you can rerun.
