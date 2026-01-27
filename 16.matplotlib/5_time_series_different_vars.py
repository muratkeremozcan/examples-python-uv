import matplotlib.pyplot as plt
import pandas as pd

# Key takeaways (two time-series, different scales):
# - Two variables can share the same time axis but need different y-axes.
# - ax.twinx() creates a second y-axis that shares the x-axis.
# - Use colors + tick_params to tie each line to its axis.

co2 = pd.DataFrame(
    {
        "date": pd.date_range("2015-01-01", periods=12, freq="MS"),
        "co2": [
            399.9,
            400.1,
            401.3,
            403.2,
            404.6,
            405.1,
            404.0,
            402.6,
            401.8,
            400.3,
            399.4,
            398.8,
        ],
        "relative_temp": [
            0.82,
            0.84,
            0.90,
            0.95,
            0.98,
            1.02,
            0.99,
            0.97,
            0.92,
            0.88,
            0.85,
            0.83,
        ],
    }
).set_index("date")
# print(co2)
#               co2  relative_temp
# date
# 2015-01-01  399.9           0.82
# 2015-02-01  400.1           0.84
# 2015-03-01  401.3           0.90
# 2015-04-01  403.2           0.95
# 2015-05-01  404.6           0.98
# 2015-06-01  405.1           1.02
# 2015-07-01  404.0           0.99
# 2015-08-01  402.6           0.97
# 2015-09-01  401.8           0.92
# 2015-10-01  400.3           0.88
# 2015-11-01  399.4           0.85
# 2015-12-01  398.8           0.83

fig, ax = plt.subplots()

ax.plot(co2.index, co2["co2"], color="b")
ax.set_xlabel("Date")
ax.set_ylabel("CO2 (ppm)", color="b")
ax.tick_params("y", colors="b")

ax2 = ax.twinx()
ax2.plot(co2.index, co2["relative_temp"], color="r")
ax2.set_ylabel("Relative temp", color="r")
ax2.tick_params("y", colors="r")

plt.title("CO2 vs Temperature")
plt.show()

# Reusable helper for labeling a timeseries on an axis.


def plot_timeseries(ax, x, y, color, xlabel, ylabel):
    ax.plot(x, y, color=color)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel, color=color)
    ax.tick_params("y", colors=color)


fig, ax = plt.subplots()
plot_timeseries(ax, co2.index, co2["co2"], "b", "Date", "CO2 (ppm)")
ax2 = ax.twinx()
plot_timeseries(ax2, co2.index, co2["relative_temp"], "r", "Date", "Relative temp")
plt.title("CO2 vs Temperature (helper)")
plt.show()
