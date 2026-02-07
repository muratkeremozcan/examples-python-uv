import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Key takeaways (color):
# - Color grabs attention but can bias perception; use it intentionally.
# - Avoid polarizing pairs (e.g., red/blue in US politics) when possible.
# - Color can distort perceived size/length; borders or uniform colors reduce this.

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

# Default palette (each bar gets a different color).
sns.barplot(data=df, x="city", y="NO2")
plt.title("NO2 by city (default palette)")
plt.show()

# Uniform color to reduce visual noise.
sns.barplot(data=df, x="city", y="NO2", color="cadetblue")
plt.title("NO2 by city (single color)")
plt.show()

# Add neutral borders to reduce color-size illusion.
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
