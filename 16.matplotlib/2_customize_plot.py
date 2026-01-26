import matplotlib.pyplot as plt

# Key takeaways (customize plots):
# - marker and linestyle control how data points and lines look.
# - color sets line color.
# - set_xlabel/set_ylabel/set_title label the axes and plot.

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

fig, ax = plt.subplots()
# marker examples: "o" circle, "v" triangle-down, "s" square, "x" x-mark
# linestyle examples: "-" solid, "--" dashed, ":" dotted, "None" no line
# color examples: "r" red, "b" blue, "g" green, "k" black
ax.plot(months, seattle, marker="o", linestyle="--", color="r", label="Seattle")
ax.set_xlabel("Month")
ax.set_ylabel("Avg temp (F)")
ax.set_title("Monthly Average Temperature")
ax.legend()
plt.show()
