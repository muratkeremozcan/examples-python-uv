import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Key takeaways (style & color):
# - `sns.set_style()` controls the plot background and grid ("white", "dark", "whitegrid", "darkgrid", "ticks").
# - `sns.set_palette()` changes default colors (diverging, sequential, or custom lists).
# - Add `_r` to reverse a palette (e.g., "RdBu_r").
# - `sns.set_context()` scales elements for different settings ("paper", "notebook", "talk", "poster").

# Small categorical dataset.
df_masc = pd.DataFrame(
    {
        "how_masculine": [
            "not at all",
            "somewhat",
            "very",
            "somewhat",
            "very",
            "not very",
        ],
        "group": ["A", "A", "B", "B", "B", "A"],
    }
)
# print(df_masc)
#   how_masculine group
# 0    not at all     A
# 1      somewhat     A
# 2          very     B
# 3      somewhat     B
# 4          very     B
# 5      not very     A


# Small quantitative dataset.
df_cars = pd.DataFrame(
    {
        "horsepower": [90, 110, 130, 150, 170, 200],
        "mpg": [32, 29, 26, 24, 21, 18],
        "cylinders": [4, 4, 4, 6, 6, 8],
    }
)
# print(df_cars)
#    horsepower  mpg  cylinders
# 0          90   32          4
# 1         110   29          4
# 2         130   26          4
# 3         150   24          6
# 4         170   21          6
# 5         200   18          8


# Style example: white (default-like) vs whitegrid.
sns.set_style("white")
sns.catplot(data=df_masc, x="how_masculine", kind="count")
plt.show()

sns.set_style("whitegrid")
sns.catplot(data=df_masc, x="how_masculine", kind="count")
plt.show()

# Palette example: diverging palette.
sns.set_palette("RdBu")
sns.catplot(data=df_masc, x="how_masculine", hue="group", kind="count")
plt.show()

# Sequential palette for a numeric variable.
sns.set_palette("Blues")
sns.scatterplot(
    data=df_cars, x="horsepower", y="mpg", hue="cylinders", size="cylinders"
)
plt.show()

# Custom palette + larger context for presentations.
sns.set_palette(["#1b9e77", "#d95f02", "#7570b3"])
sns.set_context("talk")
sns.scatterplot(data=df_cars, x="horsepower", y="mpg", hue="cylinders")
plt.show()
