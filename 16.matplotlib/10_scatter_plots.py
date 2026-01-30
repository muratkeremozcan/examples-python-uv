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
