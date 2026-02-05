import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Key takeaways (annotations):
# - Annotations add compact, direct explanations near points of interest.
# - Use them when you want to convey a message or the chart must stand alone.
# - For exploration by experts, extra annotations can add clutter or bias.
# - Use `plt.text()` for simple labels and `plt.annotate()` with arrows for crowded plots.

# Small example dataset.
df = pd.DataFrame(
    {
        "day": [10, 20, 30, 38, 45],
        "NO2": [18.5, 22.0, 25.5, 31.2, 28.8],
        "SO2": [12.0, 14.5, 16.2, 22.4, 18.1],
    }
)
print(df)
#    day   NO2   SO2
# 0   10  18.5  12.0
# 1   20  22.0  14.5
# 2   30  25.5  16.2
# 3   38  31.2  22.4
# 4   45  28.8  18.1

# Base scatter plot.
sns.scatterplot(data=df, x="NO2", y="SO2")
plt.title("NO2 vs SO2")
plt.xlabel("NO2")
plt.ylabel("SO2")
# Simple text annotation ( x, y is the anchor point, ha/va control text alignment to the anchor point).
plt.text(
    31.2, 22.4, "Day 38 spike", fontdict={"ha": "left", "va": "bottom", "size": "large"}
)
plt.show()

# Annotation with arrow to avoid crowding the point.
sns.scatterplot(data=df, x="NO2", y="SO2")
plt.title("NO2 vs SO2 (annotated)")
plt.xlabel("NO2")
plt.ylabel("SO2")
# same as ./16.matplotlib/6_annotating_time_series.py
plt.annotate(
    "Day 38 spike",
    xy=(31.2, 22.4),
    xytext=(26, 24),
    arrowprops={
        "arrowstyle": "->",
        "color": "gray",
        "lw": 2,
        "shrinkA": 4,
        "shrinkB": 4,
        "mutation_scale": 12,
    },
    ha="left",
)
plt.show()

# regplot = regression plot. It draws a scatter plus an optional best‑fit line (and usually a confidence band).
# Use it when you want to show both the points and a trend between two numeric variables
# scatter_kws = keyword args forwarded to matplotlib's scatter() call (e.g., alpha, size, colors).
df["highlight"] = ["orangered" if d == 38 else "lightgray" for d in df["day"]]
sns.regplot(
    data=df,
    x="NO2",
    y="SO2",
    fit_reg=False,
    scatter_kws={"facecolors": df["highlight"], "alpha": 0.3},
)
plt.title("NO2 vs SO2 (regplot with custom point colors)")
plt.show()
