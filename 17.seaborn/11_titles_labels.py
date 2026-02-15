import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Key takeaways (titles & labels):
# - `relplot()` and `catplot()` return a FacetGrid (can contain multiple subplots).
# - Use `g.figure.suptitle(...)` for a figure-wide title on a FacetGrid.
# - `scatterplot()` and `boxplot()` return one axes; use `ax.set_title(...)`.
# - `g.set_titles(...)` updates each subplot title; `g.set(...)` sets axis labels.
# - Use `plt.xticks(rotation=...)` when tick labels overlap.
# - `hue` keeps groups in one plot with different colors.
# - `row`/`col` splits groups into separate subplots.

# Small dataset.
df = pd.DataFrame(
    {
        "region": ["East", "East", "West", "West", "North", "North"],
        "birth_rate": [12.5, 14.1, 9.8, 10.2, 11.0, 12.2],
    }
)

# FacetGrid from catplot (figure-level title).
g = sns.catplot(data=df, x="region", y="birth_rate", kind="box")
g.figure.suptitle("Birth rates by region (per 1,000 people)", y=1.03)
g.figure.subplots_adjust(top=0.85)  # make room for suptitle
# or: g.figure.tight_layout(rect=[0, 0, 1, 0.95])
g.set_axis_labels("Region", "Birth rate per 1,000 people")
plt.show()

# AxesSubplot title (axes-level plot).
ax = sns.boxplot(data=df, x="region", y="birth_rate")
ax.set_title("Birth rates by region", y=1.02)
ax.set(xlabel="Region", ylabel="Birth rate per 1,000 people")
plt.xticks(rotation=30)
plt.show()

# FacetGrid subplot titles with set_titles.
df_groups = pd.DataFrame(
    {
        "region": ["East", "West", "North", "East", "West", "North"],
        "birth_rate": [12.5, 9.8, 11.0, 14.1, 10.2, 12.2],
        "group": ["Group 1", "Group 1", "Group 1", "Group 2", "Group 2", "Group 2"],
    }
)

g = sns.catplot(data=df_groups, x="region", y="birth_rate", col="group", kind="box")
g.figure.suptitle("Birth rates by region and group", y=1.03)
g.figure.subplots_adjust(top=0.8)
g.set_titles("This is {col_name}")
g.set(xlabel="Region", ylabel="Birth rate per 1,000 people")
plt.xticks(rotation=30)
plt.show()

# Putting it all together: style, palette, context, hue, col, titles, labels.
df_rel = pd.DataFrame(
    {
        "total_bill": [10.2, 18.5, 24.0, 35.2, 12.3, 28.0, 16.8, 40.0],
        "tip": [1.5, 3.0, 3.6, 5.0, 2.0, 4.2, 2.1, 6.1],
        "smoker": ["No", "Yes", "No", "Yes", "No", "No", "Yes", "Yes"],
        "day": ["Thur", "Fri", "Sat", "Sat", "Sun", "Sun", "Fri", "Sat"],
    }
)

sns.set_style("whitegrid")
sns.set_palette("Set2")
sns.set_context("notebook")
g = sns.relplot(
    data=df_rel,
    x="total_bill",
    y="tip",
    hue="smoker",
    col="day",
    kind="scatter",
)
g.figure.suptitle("Tips vs total bill by day (smoker highlighted)", y=1.03)
g.set_axis_labels("Total bill ($)", "Tip ($)")
plt.show()
