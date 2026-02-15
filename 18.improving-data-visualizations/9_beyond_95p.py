import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Key takeaways (beyond 95%):
# - A single interval answers one confidence level (for example 95%).
# - Multiple nested intervals show several confidence levels in one chart.
# - For color encoding, use lighter color for wider intervals and darker for narrower.
# - For confidence bands, lower alpha helps keep grid lines and trend lines readable.
# - If color is not available, use line width to encode interval level.

# Common confidence levels and z-like multipliers used in the course.
interval_specs = [("99%", 2.58), ("95%", 1.96), ("90%", 1.67)]
interval_colors = sns.color_palette("OrRd", n_colors=3)  # light -> dark

# ---------------------------------------------------------------------
# 1) Overlay multiple confidence intervals with hlines (point estimates).
# ---------------------------------------------------------------------
diffs_by_year = pd.DataFrame(
    {
        "year": [2017, 2018, 2019, 2020, 2021],
        "mean": [-0.10, -0.24, -0.15, -0.35, -0.22],
        "std_err": [0.08, 0.07, 0.09, 0.08, 0.06],
    }
)

fig, ax = plt.subplots()
for i, ((label, z), color) in enumerate(zip(interval_specs, interval_colors)):
    lower = diffs_by_year["mean"] - z * diffs_by_year["std_err"]
    upper = diffs_by_year["mean"] + z * diffs_by_year["std_err"]
    ax.hlines(
        y=diffs_by_year["year"],
        xmin=lower,
        xmax=upper,
        color=color,
        linewidth=9 - i * 2,
        label=label,
    )

# Point estimate marker at each year (best single estimate).
ax.plot(diffs_by_year["mean"], diffs_by_year["year"], "k|", markersize=12)

# x=0 is the "no difference" line.
ax.axvline(x=0, color="gray", linestyle="--")
ax.set_title("Nested confidence intervals by year")
ax.set_xlabel("Difference estimate")
ax.set_ylabel("Year")
ax.legend(title="Interval")
plt.show()

# ---------------------------------------------------------------------
# 2) Overlay multiple confidence bands with fill_between (continuous line).
# ---------------------------------------------------------------------
trend = pd.DataFrame(
    {
        "day": list(range(1, 21)),
        "mean": [
            14.0,
            14.3,
            14.5,
            14.4,
            14.8,
            15.1,
            15.0,
            15.3,
            15.6,
            15.5,
            15.8,
            16.0,
            16.1,
            16.3,
            16.2,
            16.5,
            16.6,
            16.8,
            16.9,
            17.0,
        ],
        "std_err": [
            0.16,
            0.14,
            0.15,
            0.14,
            0.16,
            0.15,
            0.14,
            0.16,
            0.15,
            0.14,
            0.16,
            0.15,
            0.14,
            0.16,
            0.15,
            0.14,
            0.16,
            0.15,
            0.14,
            0.16,
        ],
    }
)

for (label, z), color in zip(interval_specs, interval_colors):
    lower = trend["mean"] - z * trend["std_err"]
    upper = trend["mean"] + z * trend["std_err"]
    plt.fill_between(
        x=trend["day"],
        y1=lower,
        y2=upper,
        color=color,
        alpha=0.25,
        label=label,
    )

plt.plot(trend["day"], trend["mean"], color="black", linewidth=2)
plt.title("Nested confidence bands over time")
plt.xlabel("Day")
plt.ylabel("Estimate")
plt.legend(title="Band")
plt.show()

# ---------------------------------------------------------------------
# 3) No-color version: encode interval level with linewidth only.
# ---------------------------------------------------------------------
fig, ax = plt.subplots()
for i, (label, z) in enumerate(interval_specs):
    lower = diffs_by_year["mean"] - z * diffs_by_year["std_err"]
    upper = diffs_by_year["mean"] + z * diffs_by_year["std_err"]
    ax.hlines(
        y=diffs_by_year["year"],
        xmin=lower,
        xmax=upper,
        color="dimgray",
        linewidth=9 - i * 2,
        label=label,
    )

ax.plot(diffs_by_year["mean"], diffs_by_year["year"], "k|", markersize=12)
ax.axvline(x=0, color="gray", linestyle="--")
ax.set_title("Nested confidence intervals (linewidth encoding)")
ax.set_xlabel("Difference estimate")
ax.set_ylabel("Year")
ax.legend(title="Interval")
plt.show()
