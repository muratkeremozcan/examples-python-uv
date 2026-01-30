import matplotlib.pyplot as plt

# Key takeaways (sharing + styles):
# - plt.style.use(...) changes the global look of all plots.
# - Styles persist until changed (e.g., back to "default").
# - Use colorblind-friendly styles when sharing.

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

# Apply a style for all plots in this session.
# https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html

plt.style.use("ggplot")

fig, ax = plt.subplots()
ax.plot(months, seattle, label="Seattle")
ax.plot(months, austin, label="Austin")
ax.set_ylabel("Avg temp (F)")
ax.set_title("Monthly Average Temperature")
ax.legend()
plt.show()

# Key takeaways (saving figures):
# - Use fig.savefig(...) instead of plt.show() to write to disk.
# - File format comes from the extension (png, jpg, svg).
# - dpi controls resolution; set_size_inches controls figure size.

# Set size and save at higher resolution.
fig.set_size_inches(6, 4)
fig.savefig("16.matplotlib/temperatures.png", dpi=300)
# dpi + quality together works for JPEG (quality is ignored for PNG/PDF/SVG).
# Other common formats:
# fig.savefig("temperatures.pdf")
# fig.savefig("temperatures.tiff")
# fig.savefig("temperatures.svg")
# fig.savefig("temperatures.jpg", quality=85)
