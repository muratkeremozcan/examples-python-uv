import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Key takeaways (custom scatter plots):
# - Add a third variable with point size (`size`), style (`style`), or transparency (`alpha`).
# - Combining `size` with `hue` improves readability for quantitative size variables.
# - Use `alpha` < 1 when points overlap heavily.

# Small tips-like dataset.
df = pd.DataFrame(
    {
        "total_bill": [10.2, 18.5, 24.0, 35.2, 12.3, 28.0, 16.8, 40.0, 22.1, 30.5],
        "tip": [1.5, 3.0, 3.6, 5.0, 2.0, 4.2, 2.1, 6.1, 3.4, 4.6],
        "smoker": ["No", "Yes", "No", "Yes", "No", "No", "Yes", "Yes", "No", "Yes"],
        "size": [2, 2, 3, 4, 2, 4, 3, 5, 2, 4],
    }
)
# print(df)
#    total_bill  tip smoker  size
# 0        10.2  1.5     No     2
# 1        18.5  3.0    Yes     2
# 2        24.0  3.6     No     3
# 3        35.2  5.0    Yes     4
# 4        12.3  2.0     No     2
# 5        28.0  4.2     No     4
# 6        16.8  2.1    Yes     3
# 7        40.0  6.1    Yes     5
# 8        22.1  3.4     No     2
# 9        30.5  4.6    Yes     4

# Size by party size.
sns.relplot(data=df, x="total_bill", y="tip", kind="scatter", size="size")
plt.show()

# Size + hue for better contrast with quantitative size.
sns.relplot(
    data=df,
    x="total_bill",
    y="tip",
    kind="scatter",
    size="size",
    hue="size",
)
plt.show()

# Style for categorical subgroup + transparency for overlap.
sns.relplot(
    data=df,
    x="total_bill",
    y="tip",
    kind="scatter",
    hue="smoker",
    style="smoker",
    alpha=0.5,
)
plt.show()
