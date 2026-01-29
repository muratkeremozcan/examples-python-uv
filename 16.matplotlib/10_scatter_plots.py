import matplotlib.pyplot as plt
import pandas as pd

# Key takeaways (scatter plots):
# - Scatter plots compare two variables (x vs y).
# - Use color/labels to compare groups.
# - Use c= to encode a third variable (e.g., time).

co2 = pd.DataFrame(
    {
        "date": pd.date_range("1985-01-01", periods=24, freq="MS"),
        "co2": [340 + i * 0.5 for i in range(24)],
        "relative_temp": [0.1 + i * 0.01 for i in range(24)],
    }
).set_index("date")
# print(co2)
#               co2  relative_temp
# date
# 1985-01-01  340.0           0.10
# 1985-02-01  340.5           0.11
# 1985-03-01  341.0           0.12
# 1985-04-01  341.5           0.13
# 1985-05-01  342.0           0.14
# 1985-06-01  342.5           0.15
# 1985-07-01  343.0           0.16
# 1985-08-01  343.5           0.17
# 1985-09-01  344.0           0.18
# 1985-10-01  344.5           0.19
# 1985-11-01  345.0           0.20
# 1985-12-01  345.5           0.21
# 1986-01-01  346.0           0.22
# 1986-02-01  346.5           0.23
# 1986-03-01  347.0           0.24
# 1986-04-01  347.5           0.25
# 1986-05-01  348.0           0.26
# 1986-06-01  348.5           0.27
# 1986-07-01  349.0           0.28
# 1986-08-01  349.5           0.29
# 1986-09-01  350.0           0.30
# 1986-10-01  350.5           0.31
# 1986-11-01  351.0           0.32

# Basic scatter plot: co2 vs temp.
fig, ax = plt.subplots()
ax.scatter(co2["co2"], co2["relative_temp"])
ax.set_xlabel("CO2 (ppm)")
ax.set_ylabel("Relative temp")
plt.show()

# Compare two time windows with color + legend.
eighties = co2["1985":"1989"]
nineties = co2["1990":"1994"]

fig, ax = plt.subplots()
ax.scatter(eighties["co2"], eighties["relative_temp"], color="r", label="1980s")
ax.scatter(nineties["co2"], nineties["relative_temp"], color="b", label="1990s")
ax.set_xlabel("CO2 (ppm)")
ax.set_ylabel("Relative temp")
ax.legend()
plt.show()

# Encode time as color (c=).
fig, ax = plt.subplots()
ax.scatter(co2["co2"], co2["relative_temp"], c=co2.index.year)
ax.set_xlabel("CO2 (ppm)")
ax.set_ylabel("Relative temp")
plt.show()
