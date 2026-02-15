import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Key takeaways (comparing groups):
# - KDE is a smoothed histogram; use it to compare continuous distributions.
# - Rug marks show the exact observed values on the axis.
# - Swarm plots show each raw point and reveal spread per category.

# Small pollution-like dataset.
df = pd.DataFrame(
    {
        "city": [
            "Denver",
            "Denver",
            "Denver",
            "LA",
            "LA",
            "LA",
            "Houston",
            "Houston",
            "Houston",
            "Fairbanks",
            "Fairbanks",
            "Fairbanks",
        ],
        "NO2": [12.1, 13.4, 11.8, 18.0, 17.2, 19.1, 15.0, 22.4, 19.8, 9.5, 10.2, 11.0],
    }
)
# print(df)
#         city   NO2
# 0      Denver  12.1
# 1      Denver  13.4
# 2      Denver  11.8
# 3          LA  18.0
# 4          LA  17.2
# 5          LA  19.1
# 6     Houston  15.0
# 7     Houston  22.4
# 8     Houston  19.8
# 9   Fairbanks   9.5
# 10  Fairbanks  10.2
# 11  Fairbanks  11.0


# Compare two groups with KDE (Denver vs everyone else).
df["is_denver"] = df["city"] == "Denver"
sns.kdeplot(data=df, x="NO2", hue="is_denver")
plt.title("NO2 distribution: Denver vs others")
plt.show()

# Add rug marks so you can see where real observations exist.
sns.kdeplot(data=df, x="NO2", hue="is_denver")
sns.rugplot(data=df, x="NO2", hue="is_denver", height=0.05)
plt.title("NO2 distribution with rug")
plt.show()

# Same KDE comparison using explicit filtering plus labels.
sns.kdeplot(df[df["is_denver"]]["NO2"], shade=True, label="Denver", color="crimson")
sns.kdeplot(
    df[~df["is_denver"]]["NO2"], shade=True, label="Other cities", color="lightgray"
)
plt.title("NO2 distribution (shaded KDEs)")
plt.legend()  # show labels for each KDE curve
plt.show()


# Compare many classes with a swarm plot (one dot per row).
sns.swarmplot(data=df, x="city", y="NO2", size=5)
plt.title("NO2 by city (beeswarm)")
plt.show()
