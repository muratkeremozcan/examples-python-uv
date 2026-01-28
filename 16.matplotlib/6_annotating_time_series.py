import matplotlib.pyplot as plt
import pandas as pd

# Key takeaways (annotations):
# - ax.annotate adds text at a data point (xy).
# - xytext moves the text; arrowprops draws a pointer.

co2 = pd.DataFrame(
    {
        "date": pd.date_range("2015-01-01", periods=12, freq="MS"),
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
# 2015-06-01  405.1           1.02  # Annotate this point
# 2015-07-01  404.0           0.99
# 2015-08-01  402.6           0.97
# 2015-09-01  401.8           0.92
# 2015-10-01  400.3           0.88
# 2015-11-01  399.4           0.85
# 2015-12-01  398.8           0.83

fig, ax = plt.subplots()
ax.plot(co2.index, co2["relative_temp"], color="r")
ax.set_xlabel("Date")
ax.set_ylabel("Relative temp")

# Annotate the first value >= 1.0
point_date = pd.Timestamp("2015-06-01")
point_value = 1.02

start_date = pd.Timestamp("2015-03-01")
start_value = 0.85

ax.annotate(
    ">1.0",
    xy=(point_date, point_value),
    xytext=(start_date, start_value),  # optional arrow's start point
    arrowprops={"arrowstyle": "->", "color": "gray"},  # optional arrow
)

plt.show()
