import pandas as pd

df = pd.DataFrame(
    {
        "y1_gpa": [3.2, 3.8, 2.9, 3.5, 3.0],
        "y2_gpa": [3.3, 3.7, 3.1, 3.6, 2.8],
        "y3_gpa": [3.4, 3.6, 3.0, 3.7, 2.9],
        "y4_gpa": [3.5, 3.9, 3.2, 3.8, 3.0],
    }
)


def standardize(column: pd.Series) -> pd.Series:
    """Standardize the values in a column."""

    return (column - column.mean()) / column.std()


df["y1_z"] = standardize(df["y1_gpa"])
df["y2_z"] = standardize(df["y2_gpa"])
df["y3_z"] = standardize(df["y3_gpa"])
df["y4_z"] = standardize(df["y4_gpa"])


# ——— Inspect results ———
print(df)
