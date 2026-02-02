import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Key takeaways (line plots):
# - Use line plots to track the same measure over an ordered x (often time).
# - With multiple observations per x, Seaborn aggregates (mean by default) and can show uncertainty bands.
# - `hue`/`style` create subgroup lines; `markers` adds points; `dashes=False` keeps solid lines.

# Base dataset: multiple stations per location, per hour.
hours = [0, 1, 2, 3, 4, 5]
base_means = [12, 14, 18, 17, 15, 13]
location_offsets = {"North": 0, "South": 2, "East": -1, "West": 1}
station_offsets = {"A": -2, "B": 0, "C": 1, "D": 3}

rows = []
for hour, base in zip(hours, base_means):
    for location, loc_offset in location_offsets.items():
        for station, st_offset in station_offsets.items():
            rows.append(
                {
                    "hour": hour,
                    "NO_2": base + loc_offset + st_offset,
                    "location": location,
                    "station": station,
                }
            )

df = pd.DataFrame(rows)
# print(df.head(12))
#     hour  NO_2 location station
# 0      0    10    North       A
# 1      0    12    North       B
# 2      0    13    North       C
# 3      0    15    North       D
# 4      0    12    South       A
# 5      0    14    South       B
# 6      0    15    South       C
# 7      0    17    South       D
# 8      0     9     East       A
# 9      0    11     East       B
# 10     0    12     East       C
# 11     0    14     East       D

# Mean per hour (derived from the same df).
df_mean = (
    df.groupby("hour", as_index=False)["NO_2"]
    .mean()
    .rename(columns={"NO_2": "NO_2_mean"})
)
# print(df_mean)
#    hour  NO_2_mean
# 0     0       12.0
# 1     1       14.0
# 2     2       18.0
# 3     3       17.0
# 4     4       15.0
# 5     5       13.0

# Scatter vs line for the same time series.
sns.relplot(data=df_mean, x="hour", y="NO_2_mean", kind="scatter")
plt.show()

sns.relplot(data=df_mean, x="hour", y="NO_2_mean", kind="line")
plt.show()

# Subgroups by location (color + style + markers) from the same df.
sns.relplot(
    data=df,
    x="hour",
    y="NO_2",
    kind="line",
    hue="location",
    style="location",
    markers=True,
    dashes=False,
)
plt.show()

# Multiple observations per x-value -> mean + uncertainty band.
sns.relplot(data=df, x="hour", y="NO_2", kind="line")
plt.show()

# Show standard deviation instead of confidence interval.
sns.relplot(data=df, x="hour", y="NO_2", kind="line", errorbar="sd")
plt.show()

# Turn off the band entirely.
sns.relplot(data=df, x="hour", y="NO_2", kind="line", errorbar=None)
plt.show()
