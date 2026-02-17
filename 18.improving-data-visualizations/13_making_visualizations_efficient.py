import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Key takeaways (making plots efficient):
# - Efficient means: less effort for the reader to understand the message.
# - Put related charts in one figure with plt.subplots() to reduce context switching.
# - Reuse the same color mapping across plots so color meaning stays consistent.
# - Remove legends only when the mapping is still obvious from context.

# Small monthly pollution-like dataset for 3 years.
rows = []
for year, year_shift in [(2014, -1.2), (2015, 0.0), (2016, 1.0)]:
    for month in range(1, 13):
        rows.append(
            {
                "year": str(year),
                "month": month,
                "NO2": 18 + year_shift + 0.6 * month + (month % 3) * 0.7,
            }
        )
pollution = pd.DataFrame(rows)

# Count observations per year (used for the companion bar chart).
obs_per_year = (
    pollution.groupby("year", as_index=False).size().rename(columns={"size": "n_obs"})
)

# One palette reused in both plots so a year keeps the same color everywhere.
year_palette = {"2014": "#4E79A7", "2015": "#F28E2B", "2016": "#59A14F"}

fig, axes = plt.subplots(1, 2, figsize=(11, 4))

# Plot A: trend view.
sns.lineplot(
    data=pollution,
    x="month",
    y="NO2",
    hue="year",
    palette=year_palette,
    marker="o",
    ax=axes[0],
)
axes[0].set_title("Monthly NO2 trend")
axes[0].set_xlabel("Month")
axes[0].set_ylabel("NO2")

# Plot B: context view (how many observations per year).
# dodge=False keeps bars full-width since each x has one hue value.
sns.barplot(
    data=obs_per_year,
    x="year",
    y="n_obs",
    hue="year",
    palette=year_palette,
    dodge=False,
    ax=axes[1],
)
axes[1].set_title("Rows available per year")
axes[1].set_xlabel("Year")
axes[1].set_ylabel("Count")

# Remove redundant legends from both subplots to reduce clutter.
if axes[0].legend_ is not None:
    axes[0].legend_.remove()
if axes[1].legend_ is not None:
    axes[1].legend_.remove()

fig.suptitle("Efficient multi-plot layout: one story, less visual clutter", y=1.03)
plt.tight_layout()
plt.show()
