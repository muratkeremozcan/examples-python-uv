import matplotlib.pyplot as plt
import pandas as pd

# Key takeaways (first exploration pass):
# - Start broad. Do not hunt for one story too early.
# - Use head() to see columns and rough shape.
# - Use describe(include="all") to scan both numeric and categorical columns.
# - Use a scatter matrix to quickly check relationships across numeric fields.
# - Lower alpha in scatter plots so overlap is visible.

# Small farmers-market-like dataset for reproducible practice.
markets = pd.DataFrame(
    {
        "market_name": [
            "Downtown Fresh",
            "Riverfront Market",
            "Green Corner",
            "Sunrise Stalls",
            "Valley Produce",
            "City Harvest",
            "Northside Market",
            "Lakeside Local",
        ],
        "state": ["CA", "CA", "TX", "TX", "NY", "NY", "OH", "OH"],
        "months_open": [12, 10, 8, 7, 11, 9, 6, 5],
        "vendors": [120, 85, 62, 55, 98, 77, 41, 36],
        "avg_item_price": [6.5, 5.8, 4.9, 4.6, 6.1, 5.3, 4.7, 4.4],
        "state_pop_millions": [39.0, 39.0, 30.5, 30.5, 19.7, 19.7, 11.8, 11.8],
    }
)

print("=== head() ===")
print(markets.head())
#           market_name state  months_open  vendors  avg_item_price  state_pop_millions
# 0      Downtown Fresh    CA           12      120             6.5                39.0
# 1   Riverfront Market    CA           10       85             5.8                39.0
# 2        Green Corner    TX            8       62             4.9                30.5
# 3      Sunrise Stalls    TX            7       55             4.6                30.5
# 4      Valley Produce    NY           11       98             6.1                19.7

print("\n=== describe(include='all') ===")
print(markets.describe(include="all"))
# include='all' shows summary for both:
# - numeric columns (mean, min, max, etc.)
# - categorical columns (count, top, freq)

# Scatter matrix = a grid of small scatter plots for every numeric-column pair.
numeric_cols = ["months_open", "vendors", "avg_item_price", "state_pop_millions"]
pd.plotting.scatter_matrix(
    markets[numeric_cols],
    figsize=(8, 8),
    diagonal="hist",
    alpha=0.55,  # lower alpha makes overlap visible in small panels
)

plt.suptitle("First exploration: scatter matrix of numeric columns", y=1.02)
plt.tight_layout()
plt.show()
