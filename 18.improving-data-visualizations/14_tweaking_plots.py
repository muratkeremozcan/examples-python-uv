import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Key takeaways (final polish):
# - Last stage is small visual tweaks for readability and destination context.
# - set_style() controls background/grid look.
# - despine() removes border lines to reduce visual clutter.
# - set(font_scale=...) scales text globally so titles/labels stay legible.

# Small reusable dataset.
tips_like = pd.DataFrame(
    {
        "day": [
            "Thur",
            "Thur",
            "Fri",
            "Fri",
            "Sat",
            "Sat",
            "Sun",
            "Sun",
        ],
        "total_bill": [15.4, 18.2, 21.1, 19.8, 26.4, 28.7, 24.1, 27.6],
    }
)

# 1) Default-ish look for comparison.
sns.set_style("whitegrid")
sns.set(font_scale=1.0)
sns.barplot(data=tips_like, x="day", y="total_bill", estimator="mean", errorbar=None)
plt.title("Average bill by day (whitegrid, font_scale=1.0)")
plt.show()

# 2) Final-tweak style: plain background, larger text, cleaner frame.
sns.set_style("ticks")  # good when you want a plain background with axis ticks
sns.set(font_scale=1.25)  # increase all text sizes
ax = sns.barplot(
    data=tips_like,
    x="day",
    y="total_bill",
    estimator="mean",
    errorbar=None,
    color="cadetblue",
)
ax.set_title("Average bill by day (ticks, font_scale=1.25)")
ax.set_xlabel("Day of week")
ax.set_ylabel("Average total bill ($)")

# Remove top/right spines by default; keeps axes clear but less boxy.
sns.despine()
plt.show()

# 3) Optional: remove all spines for a very minimal style.
sns.set_style("white")
sns.set(font_scale=1.1)
sns.lineplot(
    data=pd.DataFrame(
        {
            "month": list(range(1, 7)),
            "NO2": [18, 19, 21, 20, 22, 23],
        }
    ),
    x="month",
    y="NO2",
    marker="o",
    color="steelblue",
)
plt.title("Minimal look (all spines removed)")
plt.xlabel("Month")
plt.ylabel("NO2")
sns.despine(left=True, bottom=True)
plt.show()

# Reset to defaults so this file does not affect later scripts.
sns.reset_defaults()
