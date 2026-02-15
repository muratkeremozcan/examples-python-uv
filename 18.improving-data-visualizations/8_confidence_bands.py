import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Key takeaways (confidence bands):
# - A confidence band is the uncertainty ribbon around a line estimate.
# - Use fill_between(lower, upper) to draw the ribbon.
# - Plot the estimate line on top so the trend is easy to read.
# - If you have many groups, separate bands into facets/subplots.
# - If you must compare two bands directly, use lower alpha to reduce overlap clutter.

# One estimate over time with a confidence band.
hours = list(range(12))
mean = [20.0, 20.8, 22.0, 22.7, 23.1, 22.5, 21.8, 21.2, 20.6, 20.1, 19.8, 19.5]
lower = [m - 1.2 for m in mean]
upper = [m + 1.2 for m in mean]

plt.fill_between(hours, lower, upper, color="steelblue", alpha=0.25)
plt.plot(hours, mean, color="steelblue", linewidth=2)
plt.title("Single confidence band over time")
plt.xlabel("Hour")
plt.ylabel("Estimate")
plt.show()

# Two groups across time.
df = pd.DataFrame(
    {
        "hour": hours * 2,
        "group": ["A"] * len(hours) + ["B"] * len(hours),
        "mean": mean + [m + 1.0 for m in mean],
    }
)
df["lower"] = df["mean"] - 1.0
df["upper"] = df["mean"] + 1.0

# Preferred when possible: separate bands so each is easier to read.
fig, axes = plt.subplots(2, 1, sharex=True, figsize=(8, 6))
for ax, group in zip(axes, ["A", "B"]):
    part = df[df["group"] == group]
    ax.fill_between(
        part["hour"], part["lower"], part["upper"], color="steelblue", alpha=0.25
    )
    ax.plot(part["hour"], part["mean"], color="steelblue", linewidth=2)
    ax.set_title(f"Group {group}")
plt.xlabel("Hour")
plt.tight_layout()
plt.show()

# Direct two-band comparison: keep to two groups, reduce fill opacity, use paired colors.
colors = sns.color_palette("Set2", n_colors=2)
for color, group in zip(colors, ["A", "B"]):
    part = df[df["group"] == group]
    plt.fill_between(part["hour"], part["lower"], part["upper"], color=color, alpha=0.4)
    plt.plot(
        part["hour"], part["mean"], color=color, linewidth=2, label=f"Group {group}"
    )

plt.title("Two confidence bands on one plot")
plt.xlabel("Hour")
plt.ylabel("Estimate")
plt.legend()
plt.show()

# Exercise-style example 1: 99% confidence band around a rolling mean.
vandenberg_NO2 = pd.DataFrame(
    {
        "day": list(range(1, 21)),
        "mean": [
            14.0,
            14.3,
            14.1,
            14.5,
            14.8,
            15.0,
            15.3,
            15.1,
            15.4,
            15.7,
            15.9,
            16.1,
            16.0,
            16.3,
            16.5,
            16.7,
            16.6,
            16.9,
            17.1,
            17.0,
        ],
        "std_err": [
            0.20,
            0.18,
            0.22,
            0.21,
            0.19,
            0.20,
            0.18,
            0.22,
            0.21,
            0.20,
            0.19,
            0.18,
            0.20,
            0.22,
            0.21,
            0.20,
            0.19,
            0.18,
            0.20,
            0.22,
        ],
    }
)
vandenberg_NO2["lower"] = vandenberg_NO2["mean"] - 2.58 * vandenberg_NO2["std_err"]
vandenberg_NO2["upper"] = vandenberg_NO2["mean"] + 2.58 * vandenberg_NO2["std_err"]

# White line is easiest to read on a dark theme.
plt.style.use("dark_background")
plt.plot("day", "mean", data=vandenberg_NO2, color="white", alpha=0.4)
plt.fill_between(
    x="day",
    y1="lower",
    y2="upper",
    data=vandenberg_NO2,
    color="coral",
    alpha=0.35,
)
plt.title("Vandenberg NO2 mean with 99% confidence band")
plt.xlabel("Day")
plt.ylabel("NO2")
plt.show()
plt.style.use("default")

# Exercise-style example 2: separate many confidence bands with FacetGrid.
city_offsets = {
    "Cincinnati": 0.0,
    "Indianapolis": 0.6,
    "Pittsburgh": 1.0,
    "Philadelphia": 1.4,
}
rows = []
for city, offset in city_offsets.items():
    for day in range(1, 11):
        mean_val = 5.0 + offset + 0.25 * day
        std_err = 0.18 + 0.02 * (day % 3)
        rows.append({"city": city, "day": day, "mean": mean_val, "std_err": std_err})

eastern_SO2 = pd.DataFrame(rows)
eastern_SO2["lower"] = eastern_SO2["mean"] - 1.96 * eastern_SO2["std_err"]
eastern_SO2["upper"] = eastern_SO2["mean"] + 1.96 * eastern_SO2["std_err"]

plt.style.use("dark_background")
g = sns.FacetGrid(eastern_SO2, col="city", col_wrap=2)
g.map(plt.fill_between, "day", "lower", "upper", color="coral", alpha=0.5)
g.map(plt.plot, "day", "mean", color="white")
g.set_axis_labels("Day", "SO2")
g.fig.suptitle("Separated confidence bands by city", y=1.02)
plt.show()
plt.style.use("default")
