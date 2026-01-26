import matplotlib.pyplot as plt

# Key takeaways (pyplot + axes):
# - We’ve already used Matplotlib via plt and pandas .plot().
# - Figure = whole canvas; Axes = the plot area inside it.
# - This model makes multi-plot layouts and styling easier.
# - plt.subplots() returns (fig, ax); plot with ax.plot(), then plt.show().

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
seattle = [40, 42, 45, 50, 56, 62, 67, 68, 63, 53, 45, 40]
austin = [50, 54, 62, 70, 77, 84, 88, 89, 83, 73, 62, 52]

fig, ax = (
    plt.subplots()
)  # fig is optional here, but needed for saving/size/layout later
ax.plot(months, seattle, label="Seattle")
ax.plot(months, austin, label="Austin")
ax.set_ylabel("Avg temp (F)")
ax.set_title("Monthly Average Temperature")
ax.legend()
plt.show()
