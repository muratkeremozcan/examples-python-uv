import matplotlib.pyplot as plt
import numpy as np

# Key takeaways (statistical plots):
# - Error bars summarize spread (e.g., std dev) on bars or lines.
# - ax.errorbar() adds yerr to a line plot.
# - Boxplots summarize median, IQR, whiskers, and outliers.

rower_heights = np.array([180, 182, 185, 188, 190, 192, 194, 186, 178, 181, 189, 193])
gym_heights = np.array([160, 162, 164, 166, 168, 170, 165, 163, 167, 169, 161, 171])

# Bar chart with error bars (mean ± std).
fig, ax = plt.subplots()
means = [rower_heights.mean(), gym_heights.mean()]
stds = [rower_heights.std(), gym_heights.std()]
ax.bar(["Rowing", "Gymnastics"], means, yerr=stds, capsize=5)
ax.set_ylabel("Height (cm)")
ax.set_title("Mean height with std dev")
plt.show()

# Line plot with error bars.
months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]
seattle_avg = [40, 42, 45, 50, 56, 62, 67, 68, 63, 53, 45, 40]
seattle_std = [2, 2, 3, 3, 4, 4, 3, 3, 3, 3, 2, 2]

fig, ax = plt.subplots()
ax.errorbar(months, seattle_avg, yerr=seattle_std, marker="o", linestyle="--")
ax.set_ylabel("Avg temp (F)")
ax.set_title("Seattle temps with std dev")
plt.show()

# Boxplot comparison.
fig, ax = plt.subplots()
ax.boxplot([rower_heights, gym_heights], labels=["Rowing", "Gymnastics"])
ax.set_ylabel("Height (cm)")
ax.set_title("Height distribution")
plt.show()
