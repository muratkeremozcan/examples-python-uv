import re

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Key takeaways (intro to geospatial plotting):
# - Location can reveal patterns you cannot see in raw tables.
# - Treat longitude/latitude like x/y in a scatter plot.
# - Longitude goes on x-axis, latitude on y-axis.
# - If lat/lon are buried in strings or tuples, extract them first.

# Example 1: lat/lon already present as a tuple (lat, lon).
chickens = pd.DataFrame(
    {
        "permit_id": [101, 102, 103, 104],
        "location": [
            (36.1627, -86.7816),
            (36.1749, -86.7675),
            (36.1550, -86.8027),
            (36.1480, -86.7900),
        ],
    }
)

# Pull lat/lon out of each tuple into clean numeric columns.
chickens["lat"] = [loc[0] for loc in chickens["location"]]
chickens["lon"] = [loc[1] for loc in chickens["location"]]

# Plot like a regular scatter plot: x=longitude, y=latitude.
sns.scatterplot(data=chickens, x="lon", y="lat", color="orangered", s=70)
plt.title("Chicken permits (sample points)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(alpha=0.25)
plt.show()

# Example 2: lat/lon buried in a text field.
stops = pd.DataFrame(
    {
        "stop_name": ["A", "B", "C"],
        "raw_location": [
            "POINT (36.1642, -86.7745) zone=DT",
            "POINT (36.1725, -86.7602) zone=Midtown",
            "POINT (36.1499, -86.7920) zone=SoBro",
        ],
    }
)

# Regex captures:
# group 1 = latitude (after '(' and before comma)
# group 2 = longitude (after comma and before ')')
pattern = r"\(([-\d.]+),\s*([-\d.]+)\)"
matches = [re.search(pattern, text) for text in stops["raw_location"]]
stops["lat"] = [float(m.group(1)) for m in matches]
stops["lon"] = [float(m.group(2)) for m in matches]

print(stops[["stop_name", "lat", "lon"]])
#   stop_name      lat      lon
# 0         A  36.1642 -86.7745
# 1         B  36.1725 -86.7602
# 2         C  36.1499 -86.7920
