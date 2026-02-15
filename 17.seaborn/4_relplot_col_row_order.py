import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Key takeaways (relplot + subplots):
# - `relplot()` is figure-level and supports subplots via `col`/`row`.
# - `col` splits one plot into multiple columns by category; `row` splits into rows.
# - Use `col_wrap` to wrap many columns; `col_order`/`row_order` to control order.
# - `scatterplot()` draws one chart on one axes.
# - `relplot()` can draw one chart or a grid of small charts.
# - If you need faceting (`col`/`row`), use `relplot()`.

# Small tips-like dataset.
df = pd.DataFrame(
    {
        "total_bill": [10.2, 18.5, 24.0, 35.2, 12.3, 28.0, 16.8, 40.0, 22.1, 30.5],
        "tip": [1.5, 3.0, 3.6, 5.0, 2.0, 4.2, 2.1, 6.1, 3.4, 4.6],
        "smoker": ["No", "Yes", "No", "Yes", "No", "No", "Yes", "Yes", "No", "Yes"],
        "time": [
            "Lunch",
            "Dinner",
            "Lunch",
            "Dinner",
            "Lunch",
            "Dinner",
            "Dinner",
            "Dinner",
            "Lunch",
            "Dinner",
        ],
        "day": ["Thur", "Fri", "Sat", "Sat", "Sun", "Sun", "Fri", "Sat", "Thur", "Sun"],
    }
)
# print(df)
#    total_bill  tip smoker    time   day
# 0        10.2  1.5     No   Lunch  Thur
# 1        18.5  3.0    Yes  Dinner   Fri
# 2        24.0  3.6     No   Lunch   Sat
# 3        35.2  5.0    Yes  Dinner   Sat
# 4        12.3  2.0     No   Lunch   Sun
# 5        28.0  4.2     No  Dinner   Sun
# 6        16.8  2.1    Yes  Dinner   Fri
# 7        40.0  6.1    Yes  Dinner   Sat
# 8        22.1  3.4     No   Lunch  Thur
# 9        30.5  4.6    Yes  Dinner   Sun

# Basic relational plot (scatter).
sns.relplot(x="total_bill", y="tip", kind="scatter", data=df)
plt.show()

# Subplots in columns by a categorical variable.
sns.relplot(x="total_bill", y="tip", kind="scatter", col="smoker", data=df)
plt.show()

# Subplots by row and column (two categorical variables).
sns.relplot(
    x="total_bill",
    y="tip",
    kind="scatter",
    col="smoker",
    row="time",
    data=df,
)
plt.show()

# Wrap columns and control order.
sns.relplot(
    x="total_bill",
    y="tip",
    kind="scatter",
    col="day",
    col_wrap=2,
    col_order=["Thur", "Fri", "Sat", "Sun"],
    data=df,
)
plt.show()

# Final example: use both col and row with explicit row order.
sns.relplot(
    x="total_bill",
    y="tip",
    kind="scatter",
    col="smoker",
    row="time",
    row_order=["Dinner", "Lunch"],
    data=df,
)
plt.show()
