import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Key takeaways (count plots & bar plots):
# - Categorical plots compare groups; use `catplot()` for flexible subplots.
# - Count plots show the number of observations per category.
# - Bar plots show the mean of a quantitative variable per category (with CI by default).
# - Use `order` to control category order and `errorbar=None` to hide confidence intervals.

# Small, reproducible dataset.
df = pd.DataFrame(
    {
        "how_masculine": [
            "not at all",
            "somewhat",
            "very",
            "somewhat",
            "very",
            "not very",
        ],
        "day": ["Thur", "Fri", "Sat", "Sun", "Sun", "Fri"],
        "total_bill": [10.2, 18.5, 24.0, 35.2, 12.3, 28.0],
    }
)
# print(df)
#   how_masculine   day  total_bill
# 0    not at all  Thur        10.2
# 1      somewhat   Fri        18.5
# 2          very   Sat        24.0
# 3      somewhat   Sun        35.2
# 4          very   Sun        12.3
# 5      not very   Fri        28.0

# Count plot via catplot().
order = ["not at all", "not very", "somewhat", "very"]
sns.catplot(data=df, x="how_masculine", kind="count", order=order)
plt.show()

# Bar plot via catplot(): mean total_bill by day (CI shown by default).
sns.catplot(data=df, x="day", y="total_bill", kind="bar")
plt.show()

# Turn off confidence intervals.
sns.catplot(data=df, x="day", y="total_bill", kind="bar", errorbar=None)
plt.show()

# Horizontal bar plot (swap axes).
sns.catplot(data=df, y="day", x="total_bill", kind="bar")
plt.show()

# Facet into columns with col (one count plot per day).
sns.catplot(data=df, x="how_masculine", kind="count", col="day")
plt.show()

# same with row
sns.catplot(data=df, x="how_masculine", kind="count", row="day")
plt.show()
