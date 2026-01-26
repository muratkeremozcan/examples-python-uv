import matplotlib.pyplot as plt

# Key takeaways (small multiples):
# - Too much data in one plot can get messy.
# - Use subplots (small multiples) to compare similar data.
# - plt.subplots(r, c) returns a grid of Axes.
# - sharey=True keeps the same y-axis range for fair comparison.

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

seattle_avg = [5.2, 3.9, 3.4, 2.7, 1.8, 1.5, 0.7, 0.9, 1.5, 3.4, 5.6, 5.5]
seattle_p25 = [4.1, 3.1, 2.6, 2.0, 1.1, 1.0, 0.5, 0.7, 1.1, 2.7, 4.4, 4.3]
seattle_p75 = [6.3, 4.7, 4.1, 3.4, 2.6, 2.0, 1.0, 1.2, 2.0, 4.2, 6.8, 6.7]

austin_avg = [2.0, 2.0, 2.5, 2.0, 4.0, 3.5, 2.0, 2.2, 3.2, 3.5, 2.4, 2.3]
austin_p25 = [1.2, 1.2, 1.5, 1.2, 2.5, 2.0, 1.2, 1.3, 2.0, 2.2, 1.4, 1.4]
austin_p75 = [2.8, 2.8, 3.5, 2.7, 5.5, 5.0, 2.8, 3.0, 4.5, 4.8, 3.3, 3.2]

fig, axes = plt.subplots(2, 1, sharey=True)  # 2 rows, 1 column of plots

axes[0].plot(months, seattle_avg, label="Seattle")
axes[0].plot(months, seattle_p25, linestyle="--")
axes[0].plot(months, seattle_p75, linestyle="--")
axes[0].set_ylabel("Precip (in)")
axes[0].set_title("Seattle")

axes[1].plot(months, austin_avg, label="Austin")
axes[1].plot(months, austin_p25, linestyle="--")
axes[1].plot(months, austin_p75, linestyle="--")
axes[1].set_ylabel("Precip (in)")
axes[1].set_xlabel("Month")
axes[1].set_title("Austin")

plt.show()
