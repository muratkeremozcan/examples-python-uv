import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Key takeaways (point plots):
# - Point plots show a summary (mean by default) of a quantitative variable per category.
# - They include confidence intervals by default and make subgroup comparisons easy.
# - Unlike line plots, point plots use a categorical axis.
# - Use `linestyle="none"` to disconnect points; `estimator` to switch to median.
# - Use `capsize` to add CI caps; `errorbar=None` to hide CIs.
# median is more robust to outliers vs mean

# Small tips-like dataset.
df = pd.DataFrame(
    {
        "smoker": ["No", "Yes", "No", "Yes", "No", "No", "Yes", "Yes"],
        "day": ["Thur", "Fri", "Sat", "Sat", "Sun", "Sun", "Fri", "Sat"],
        "total_bill": [10.0, 22.5, 18.0, 35.2, 28.0, 12.3, 40.0, 16.8],
        "how_masculine": ["No", "Yes", "No", "Yes", "No", "Yes", "No", "Yes"],
        "age_group": [
            "18-25",
            "26-35",
            "18-25",
            "26-35",
            "36-45",
            "36-45",
            "26-35",
            "18-25",
        ],
        "important": [0.2, 0.6, 0.3, 0.7, 0.4, 0.5, 0.8, 0.25],
    }
)
# print(df)
#   smoker   day  total_bill how_masculine age_group  important
# 0     No  Thur        10.0            No     18-25       0.20
# 1    Yes   Fri        22.5           Yes     26-35       0.60
# 2     No   Sat        18.0            No     18-25       0.30
# 3    Yes   Sat        35.2           Yes     26-35       0.70
# 4     No   Sun        28.0            No     36-45       0.40
# 5     No   Sun        12.3           Yes     36-45       0.50
# 6    Yes   Fri        40.0            No     26-35       0.80
# 7    Yes   Sat        16.8           Yes     18-25       0.25

# Basic point plot (mean with CI).
sns.catplot(data=df, x="smoker", y="total_bill", kind="point")
plt.show()

# Point plot with subgroups: easier to compare slopes than bars.
sns.catplot(
    data=df,
    x="age_group",
    y="important",
    hue="how_masculine",
    kind="point",
)
plt.show()

# Disconnect points.
sns.catplot(
    data=df,
    x="smoker",
    y="total_bill",
    kind="point",
    linestyle="none",
)
plt.show()

# Use median estimator (robust to outliers) and add CI caps.
sns.catplot(
    data=df,
    x="smoker",
    y="total_bill",
    kind="point",
    estimator=np.median,
    capsize=0.2,
)
plt.show()

# Turn off confidence intervals.
sns.catplot(data=df, x="smoker", y="total_bill", kind="point", errorbar=None)
plt.show()
