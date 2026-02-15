import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Key takeaways (categorical palettes):
# - Use distinct colors for categories, but keep category count manageable.
# - If there are too many classes, highlight a few and group the rest as "Other".
# - Use qualitative palettes for unordered categories.
# - Use ordered palettes for ordinal categories (low -> high).

# Small dataset with many categories.
df = pd.DataFrame(
    {
        "city": ["Denver", "LA", "Houston", "Fairbanks", "Miami", "Seattle", "Boston"],
        "NO2": [12.4, 18.2, 20.1, 9.8, 17.0, 14.6, 15.2],
    }
)
# print(df)
#         city   NO2
# 0     Denver  12.4
# 1         LA  18.2
# 2    Houston  20.1
# 3  Fairbanks   9.8
# 4      Miami  17.0
# 5    Seattle  14.6
# 6     Boston  15.2

# "Set2" is a built-in qualitative palette from ColorBrewer.
sns.set_palette("Set2")
sns.barplot(data=df, x="city", y="NO2")
plt.title("NO2 by city (qualitative palette)")
plt.show()

# Keep only key cities distinct, collapse the rest into "Other".
focus = {"Denver", "LA", "Houston"}
df_grouped = df.copy()
df_grouped["city_group"] = df_grouped["city"].apply(
    lambda c: c if c in focus else "Other"
)
sns.barplot(data=df_grouped, x="city_group", y="NO2")
plt.title("Focus on key cities, group the rest as Other")
plt.show()

#####################################################

# Ordinal data example (1-5 happiness scale).
df_ord = pd.DataFrame(
    {
        "happiness": ["1", "2", "3", "4", "5"],
        "count": [5, 9, 12, 8, 4],
    }
)
order = ["1", "2", "3", "4", "5"]
sns.barplot(
    data=df_ord,
    x="happiness",
    y="count",
    order=order,
    palette=sns.color_palette("OrRd", n_colors=5),
)
plt.title("Ordinal palette (OrRd) for ordered categories")
plt.show()

# Palette shortcut: pass the palette name directly.
sns.scatterplot(
    data=df,
    x="NO2",
    y="NO2",
    hue="city",
    palette="Set2",
)
plt.title("Palette name shortcut (Set2)")
plt.show()

#####################################################

# qcut turns a continuous column into ordered bins (quartiles here).
df_bins = df.copy()
df_bins["NO2_quartile"] = pd.qcut(df_bins["NO2"], q=4, labels=False)
sns.scatterplot(
    data=df_bins,
    x="NO2",
    y="NO2",
    hue="NO2_quartile",
    palette="GnBu",
)
plt.title("NO2 quartiles (qcut) with ordinal palette")
plt.show()

#####################################################

# Too many categories: highlight a few lines, group the rest as "other".
months = [1, 2, 3, 4, 5, 6]
city_pol_month = pd.DataFrame(
    {
        "month": months * 4,
        "city_pol": [
            "Vandenberg Air Force Base NO2",
            "Vandenberg Air Force Base NO2",
            "Vandenberg Air Force Base NO2",
            "Vandenberg Air Force Base NO2",
            "Vandenberg Air Force Base NO2",
            "Vandenberg Air Force Base NO2",
            "Long Beach CO",
            "Long Beach CO",
            "Long Beach CO",
            "Long Beach CO",
            "Long Beach CO",
            "Long Beach CO",
            "Cincinnati SO2",
            "Cincinnati SO2",
            "Cincinnati SO2",
            "Cincinnati SO2",
            "Cincinnati SO2",
            "Cincinnati SO2",
            "Other City O3",
            "Other City O3",
            "Other City O3",
            "Other City O3",
            "Other City O3",
            "Other City O3",
        ],
        "value": [
            0.1,
            0.2,
            0.1,
            0.0,
            -0.1,
            -0.2,
            0.0,
            0.1,
            0.2,
            0.1,
            0.0,
            -0.1,
            -0.3,
            -0.2,
            -0.1,
            0.0,
            0.1,
            0.2,
            0.05,
            0.0,
            -0.05,
            -0.1,
            -0.05,
            0.0,
        ],
    }
)
wanted_combos = [
    "Vandenberg Air Force Base NO2",
    "Long Beach CO",
    "Cincinnati SO2",
]
city_pol_month["color_cats"] = [
    x if x in wanted_combos else "other" for x in city_pol_month["city_pol"]
]

# hue controls line color groups; units tells seaborn which rows belong to one line.
# estimator=None disables averaging so each category keeps its own raw trajectory.
sns.lineplot(
    data=city_pol_month,
    x="month",
    y="value",
    hue="color_cats",
    units="city_pol",
    estimator=None,
    palette="Set2",
)
plt.title("Highlight a few category lines, fade the rest")
plt.show()
