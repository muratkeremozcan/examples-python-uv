import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Key takeaways (highlighting data):
# - Plot all points, then highlight a small subset to guide attention.
# - Use a color vector (one color per row) to programmatically highlight points.
# - This scales easily to multiple highlights without multiple plot calls.

# Small, reproducible pollution-like dataset.
df = pd.DataFrame({"day": range(1, 51)})
df["NO2"] = 20 + df["day"] * 0.4 + (df["day"] % 5) * 1.5
df["SO2"] = 10 + df["day"] * 0.3 + (df["day"] % 7)
print(df)
#     day   NO2   SO2
# 0     1  21.9  11.3
# 1     2  23.8  12.6
# 2     3  25.7  13.9
# 3     4  27.6  15.2
# 4     5  22.0  16.5
# 5     6  23.9  17.8
# 6     7  25.8  12.1
# 7     8  27.7  13.4
# 8     9  29.6  14.7
# 9    10  24.0  16.0
# 10   11  25.9  17.3


# Baseline scatter plot.
# scatter plots are best for showing relationships between two quantitative variables.
sns.scatterplot(data=df, x="NO2", y="SO2")
plt.title("NO2 vs SO2 (all days)")
plt.show()

# Highlight a specific day (e.g., day 38).
highlight_day = 38

# highlight using Seaborn (hue + palette mapping).
df["highlight"] = df["day"] == highlight_day
sns.scatterplot(
    data=df,
    x="NO2",
    y="SO2",
    hue="highlight",
    palette={True: "crimson", False: "lightgray"},
    legend=False,
)
plt.title(f"NO2 vs SO2 (highlight day {highlight_day}, seaborn)")
plt.show()

# highlight using matplotlib (color vector).
colors = ["crimson" if d == highlight_day else "lightgray" for d in df["day"]]
plt.scatter(df["NO2"], df["SO2"], c=colors)
plt.title(f"NO2 vs SO2 (highlight day {highlight_day})")
plt.xlabel("NO2")
plt.ylabel("SO2")
plt.show()
