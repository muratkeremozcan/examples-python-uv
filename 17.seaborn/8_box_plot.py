import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Key takeaways (box plots):
# - The box spans the 25th–75th percentiles (IQR); the line inside is the median.
# - Whiskers show spread beyond the box; points beyond whiskers are outliers.
# - Use `catplot(kind="box")` to compare a quantitative variable across categories.
# - `order` controls category order; `showfliers=False` hides outliers.
# - `whis` changes whisker rules (IQR multiplier, percentiles, or min/max).

# Small tips-like dataset.
df = pd.DataFrame(
    {
        "time": [
            "Lunch",
            "Dinner",
            "Lunch",
            "Dinner",
            "Lunch",
            "Dinner",
            "Dinner",
            "Lunch",
            "Dinner",
        ],
        "total_bill": [10.2, 28.0, 12.3, 35.2, 8.5, 40.0, 22.1, 16.8, 120.0],
    }
)
# print(df)
#      time  total_bill
# 0   Lunch        10.2
# 1  Dinner        28.0
# 2   Lunch        12.3
# 3  Dinner        35.2
# 4   Lunch         8.5
# 5  Dinner        40.0
# 6  Dinner        22.1
# 7   Lunch        16.8
# 8  Dinner       100.0

# Basic box plot.
sns.catplot(data=df, x="time", y="total_bill", kind="box")
plt.show()

# Change category order.
sns.catplot(
    data=df,
    x="time",
    y="total_bill",
    kind="box",
    order=["Dinner", "Lunch"],
)
plt.show()

# Hide outliers.
sns.catplot(
    data=df,
    x="time",
    y="total_bill",
    kind="box",
    showfliers=False,
)
plt.show()

# Whiskers at min/max % (no outliers shown).
sns.catplot(
    data=df,
    x="time",
    y="total_bill",
    kind="box",
    whis=[5, 95],  # whis=0.5 would mean 50% of the data
)
plt.show()
