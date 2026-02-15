import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Key takeaways:
# - One number (an average) is only a best guess from sample data.
# - CI bars show the "reasonable range" around that guess.
# - Short CI bar = more precise guess; long CI bar = more uncertainty.
# - hlines() is a simple way to draw those interval bars.

# Simple sample-based estimates with 95% confidence intervals.
df = pd.DataFrame(
    {
        "measure": ["CO mean", "NO2 mean", "O3 mean"],
        "estimate": [0.80, 1.30, 0.55],
        "ci_low": [0.62, 1.05, 0.38],
        "ci_high": [0.98, 1.55, 0.72],
    }
)
# print(df)
#    measure  estimate  ci_low  ci_high
# 0  CO mean      0.80    0.62     0.98
# 1 NO2 mean      1.30    1.05     1.55
# 2  O3 mean      0.55    0.38     0.72

y_pos = list(range(len(df)))

fig, ax = plt.subplots()

# Horizontal blue bar: confidence interval range from ci_low to ci_high.
ax.hlines(
    y=y_pos, xmin=df["ci_low"], xmax=df["ci_high"], color="steelblue", linewidth=3
)

# Vertical black marker: single best-guess value (point estimate).
ax.vlines(
    x=df["estimate"],
    ymin=[y - 0.12 for y in y_pos],
    ymax=[y + 0.12 for y in y_pos],
    color="black",
    linewidth=2,
)

ax.set_yticks(y_pos)
ax.set_yticklabels(df["measure"])
ax.set_xlabel("Estimated value")
ax.set_title("Point estimates with 95% confidence intervals")
plt.show()

# Exercise-style pattern: small subplot per pollutant.
average_ests = pd.DataFrame(
    {
        "pollutant": ["CO", "NO2", "O3", "SO2"],
        "mean": [0.95, 1.45, 0.62, 0.21],
        "std_err": [0.08, 0.10, 0.07, 0.04],
        "seen": [1.02, 1.39, 0.69, 0.25],  # observed value to compare against interval
        "y": [0, 0, 0, 0],  # anchor line and point on each small subplot
    }
)

# 95% CI formula used in class/exercises.
average_ests["lower"] = average_ests["mean"] - 1.96 * average_ests["std_err"]
average_ests["upper"] = average_ests["mean"] + 1.96 * average_ests["std_err"]

g = sns.FacetGrid(average_ests, row="pollutant", sharex=False, height=1.6, aspect=3)
# Blue line = normal range from history (CI around mean).
g.map(plt.hlines, "y", "lower", "upper", color="steelblue", linewidth=3)
# Orange dot = newly observed value we compare against that normal range.
g.map(plt.scatter, "seen", "y", color="orangered")
g.set_ylabels("").set_xlabels("Value")
plt.show()
