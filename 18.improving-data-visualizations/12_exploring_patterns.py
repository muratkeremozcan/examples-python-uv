from math import log

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Key process for this stage:
# 1) Pick one possible pattern and test it quickly with regplot.
# 2) Aggregate to a useful level (like state) and label outliers.
# 3) If there are too many points, hide points and show text labels only.

# Small farmers-market-like dataset.
markets = pd.DataFrame(
    {
        "name": [
            "Golden Gate Market",
            "Bay Fresh",
            "Austin Harvest",
            "Houston Greens",
            "Brooklyn Farm Stand",
            "Buffalo Fresh",
            "Des Moines Local",
            "Cedar Rapids Market",
            "Anchorage Weekend",
            "Fairbanks Produce",
            "Burlington Market",
            "Montpelier Stalls",
        ],
        "state": [
            "CA",
            "CA",
            "TX",
            "TX",
            "NY",
            "NY",
            "IA",
            "IA",
            "AK",
            "AK",
            "VT",
            "VT",
        ],
        "lat": [37.8, 37.5, 30.3, 29.7, 40.7, 42.9, 41.6, 41.9, 61.2, 64.8, 44.5, 44.3],
        "months_open": [12, 11, 10, 9, 9, 8, 7, 7, 5, 4, 6, 6],
        "state_pop": [
            39000000,
            39000000,
            30500000,
            30500000,
            19700000,
            19700000,
            3200000,
            3200000,
            730000,
            730000,
            650000,
            650000,
        ],
    }
)

# 1) Raw pattern check: latitude vs months open.
sns.regplot(
    x="lat",
    y="months_open",
    data=markets,
    scatter_kws={"alpha": 0.1, "color": "gray"},
    ci=False,
)
plt.title("Pattern check: latitude vs months open")
plt.show()

# 2) State-level summary: log(number of markets) vs log(state population).
markets_and_pop = (
    markets.groupby("state", as_index=False)
    .agg(
        {
            "name": lambda d: log(len(d)),
            "state_pop": lambda d: log(d.iloc[0]),
        }
    )
    .rename(columns={"name": "log_markets", "state_pop": "log_pop"})
)

g = sns.regplot(
    x="log_markets",
    y="log_pop",
    ci=False,
    scatter_kws={"s": 30},
    data=markets_and_pop,
)

for _, row in markets_and_pop.iterrows():
    g.annotate(row["state"], (row["log_markets"], row["log_pop"]), size=10)

plt.title("State profile: market count vs population (log scale)")
plt.show()

# 3) Dense labels example: state-by-good proportions shown as text.
goods_by_state = pd.DataFrame(
    {
        "state": [
            "CA",
            "CA",
            "CA",
            "TX",
            "TX",
            "TX",
            "NY",
            "NY",
            "NY",
            "AK",
            "AK",
            "AK",
        ],
        "good": [
            "Fruits",
            "Seafood",
            "Vegetables",
            "Fruits",
            "Seafood",
            "Vegetables",
            "Fruits",
            "Seafood",
            "Vegetables",
            "Fruits",
            "Seafood",
            "Vegetables",
        ],
        "prop_selling": [
            0.88,
            0.41,
            0.92,
            0.79,
            0.34,
            0.86,
            0.82,
            0.46,
            0.87,
            0.62,
            0.55,
            0.68,
        ],
    }
)
to_plot = ["Fruits", "Seafood", "Vegetables"]
goods_by_state_small = goods_by_state.query("good in @to_plot")

g = sns.scatterplot(x="good", y="prop_selling", data=goods_by_state_small, s=0)

for _, row in goods_by_state_small.iterrows():
    g.annotate(
        row["state"],
        (row["good"], row["prop_selling"]),
        ha="center",
        size=10,
    )

plt.title("Text scatter: which states stand out by good")
plt.show()
