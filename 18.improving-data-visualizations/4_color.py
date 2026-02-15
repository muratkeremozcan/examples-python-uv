import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Key takeaways (color):
# - Color grabs attention fast, so use it on purpose.
# - Strong cultural color pairs can add unintended meaning.
# - Too many colors add noise; single-color bars are often easier to read.

# Small categorical dataset.
df = pd.DataFrame(
    {
        "city": ["Denver", "LA", "Houston", "Fairbanks"],
        "NO2": [12.4, 18.2, 20.1, 9.8],
    }
)
# print(df)
#         city   NO2
# 0     Denver  12.4
# 1         LA  18.2
# 2    Houston  20.1
# 3  Fairbanks   9.8

# Default behavior: each bar gets a different color.
sns.barplot(data=df, x="city", y="NO2")
plt.title("NO2 by city (default palette)")
plt.show()

# One color across bars reduces visual noise.
sns.barplot(data=df, x="city", y="NO2", color="cadetblue")
plt.title("NO2 by city (single color)")
plt.show()

# Add neutral borders so shape/height are easier to compare.
sns.barplot(
    data=df,
    x="city",
    y="NO2",
    color="cadetblue",
    edgecolor="black",
    linewidth=1,
)
plt.title("NO2 by city (single color + borders)")
plt.show()
