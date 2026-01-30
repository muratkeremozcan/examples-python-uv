import matplotlib.pyplot as plt
import pandas as pd

# Key takeaways (automate figures):
# - Use data-driven loops to adapt plots to unknown categories.
# - Series.unique() gives the categories to iterate over.
# - Automation makes plots faster, flexible, and reproducible.

athletes = pd.DataFrame(
    {
        "Sport": [
            "Rowing",
            "Rowing",
            "Rowing",
            "Gymnastics",
            "Gymnastics",
            "Swimming",
            "Swimming",
        ],
        "Height": [185, 188, 192, 165, 168, 180, 182],
    }
)

sports = athletes["Sport"].unique()

fig, ax = plt.subplots()

for sport in sports:
    sport_df = athletes[athletes["Sport"] == sport]
    ax.bar(
        sport,
        sport_df["Height"].mean(),
        yerr=sport_df["Height"].std(),
        capsize=4,
    )

ax.set_ylabel("Height (cm)")
ax.set_xticklabels(sports, rotation=90)
ax.set_title("Average height by sport")
plt.show()
