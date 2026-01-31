import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Key takeaways (hue):
# - `hue` adds a third variable via color and auto-builds a legend.
# - `hue_order` controls legend/category order.
# - `palette` maps category values to colors (names or hex codes).

# Small, reproducible DataFrame (tips-like).
df = pd.DataFrame(
    {
        "total_bill": [10.0, 22.5, 18.0, 35.2, 28.0, 12.3, 40.0, 16.8],
        "tip": [1.5, 3.6, 2.4, 5.0, 4.2, 2.0, 6.1, 2.1],
        "smoker": ["No", "Yes", "No", "Yes", "No", "No", "Yes", "Yes"],
    }
)
# print(df)
#    total_bill  tip smoker
# 0        10.0  1.5     No
# 1        22.5  3.6    Yes
# 2        18.0  2.4     No
# 3        35.2  5.0    Yes
# 4        28.0  4.2     No
# 5        12.3  2.0     No
# 6        40.0  6.1    Yes
# 7        16.8  2.1    Yes

# Basic scatter plot.
sns.scatterplot(x="total_bill", y="tip", data=df)
plt.title("Total bill vs tip")
plt.show()

# Add a third variable with hue (auto legend).
sns.scatterplot(x="total_bill", y="tip", hue="smoker", data=df)
plt.title("Total bill vs tip (smoker)")
plt.show()

# Control order and colors.
hue_colors = {"Yes": "black", "No": "red"}
sns.scatterplot(
    x="total_bill",
    y="tip",
    hue="smoker",
    hue_order=["Yes", "No"],
    palette=hue_colors,
    data=df,
)
plt.title("Total bill vs tip (custom hues)")
plt.show()
