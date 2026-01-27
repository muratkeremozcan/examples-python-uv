import matplotlib.pyplot as plt
import pandas as pd

# Key takeaways (time series):
# - Parse date columns and set them as the index for time-aware plotting.
# - Matplotlib formats time axes automatically (years, months).
# - Slice by date strings to zoom into periods.

# Sample time-series data (monthly, 2015-2016).
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
ax.plot(co2.index, co2["co2"])
ax.set_xlabel("Date")
ax.set_ylabel("CO2 (ppm)")
ax.set_title("Atmospheric CO2")
plt.show()

# Zoom to a time window using date slicing.
co2_2015 = co2["2015-01-01":"2015-07-31"]
fig, ax = plt.subplots()
ax.plot(co2_2015.index, co2_2015["co2"])
ax.set_title("CO2 in 2015")
plt.show()
