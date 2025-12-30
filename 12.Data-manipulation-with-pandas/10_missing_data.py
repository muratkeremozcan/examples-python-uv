# Missing-data + reshape cheat sheet:
# - stack/dropna: stack drops all-NaN rows by default; set dropna=False to keep them.
# - unstack/fill_value: unstack can create NaNs when groups lack labels; use fill_value to plug a default.
# - fillna(): replace NaNs after stacking/unstacking (0/mean/median or custom per column).
# - isna()/isnull(): check for NaNs; .sum() counts, .any() flags presence.
# - Plots: hist ignores NaNs; filling zeros changes the distribution (piles at 0).

import matplotlib.pyplot as plt
from dataframes.avocados_2016 import avocados

print(avocados)

print("\nuse .isnull().any() to check columns for missing values\n")
print(avocados.isnull().any())
print("\nuse .isnull().sum() to check columns for missing values\n")
print(avocados.isnull().sum())

print("\nwhen there are missing values we can do a few things")

print(
    "\n1) one option is to remove the rows with missing values from the dataset, use .dropna() :"
)
avocados_complete = avocados.dropna()
print(avocados_complete.isna().any())
print()

print(
    '\nuse .isnull().sum().plot(kind="bar") to plot missing values by variable (# Figure 1)'
)
# if we look at the original, we can check the missing values
avocados.isna().sum().plot(kind="bar")
plt.title("Figure 1: Missing Values by Column")
plt.show()

######################

# Histogram summary:
# A histogram visualizes data distribution by grouping values into bins.
# It helps identify patterns, spread, and outliers in numeric data.

cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
# 2.a) Create histograms showing the distributions cols_with_missing
print(
    "\nFigure 2 : When you call .hist() on columns with NaNs, those missing rows are ignored."
)
print("\nso the histogram only reflects the actual non-missing values.")
avocados[cols_with_missing].hist()
plt.suptitle("Figure 2: Original Data Distribution (NaNs ignored)")
plt.show()

print(
    "\n2) another option is to fill the missing values with a specific value. For numeric values 0 is used, use .fillna(<value>)"
)
print(
    "\nWhen you fill missing values with 0, you're inserting actual zeros into the dataset."
)
print("Now the histogram treats those zeros as valid values.")
print(
    "This shifts the distribution: you'll see extra bars piled up at 0 (or very low bins), because all the missing rows now contribute to the counts."
)
print("\nFigure 3:")
avocados_filled = avocados.fillna(0)
avocados_filled[
    cols_with_missing
].hist()  # Figure 3 : shows us missing values where Y axis is 0
plt.suptitle("Figure 3: Distribution After Filling with 0")
plt.show()

print("\n3) Fill with statistical measures - more realistic than 0")
print("\n3a) Fill with mean: .fillna(df.mean()) - good for normally distributed data")
avocados_mean_filled = avocados.fillna(avocados.mean(numeric_only=True))
print("Small sold mean:", avocados["small_sold"].mean())
print("Large sold mean:", avocados["large_sold"].mean())

print("\n3b) Fill with median: .fillna(df.median()) - less effected by outliers")
avocados_median_filled = avocados.fillna(avocados.median(numeric_only=True))
print("Small sold median:", avocados["small_sold"].median())
print("Large sold median:", avocados["large_sold"].median())

print("\nFigure 4: Distribution After Filling with Median")
avocados_median_filled[cols_with_missing].hist()
plt.suptitle("Figure 4: Distribution After Filling with Median")
plt.show()

print("\n4) Forward fill (ffill) and backward fill (bfill) - good for time series")
print("\n4a) Forward fill: .ffill() - use previous value")
avocados_ffill = avocados.ffill()
print("Forward fill carries the last known value forward")

print("\n4b) Backward fill: .bfill() - use next value")
avocados_bfill = avocados.bfill()
print("Backward fill uses the next known value to fill backwards")

print("\nFigure 5: Distribution After Forward Fill")
avocados_ffill[cols_with_missing].hist()
plt.suptitle("Figure 5: Distribution After Forward Fill")
plt.show()

print("\n5) Fill specific columns differently")
fill_values = {
    "small_sold": avocados["small_sold"].median(),
    "large_sold": avocados["large_sold"].median(),
    "xl_sold": 0,  # Maybe xl_sold missing really means 0
}
avocados_custom_fill = avocados.fillna(value=fill_values)
print("Custom fill: median for small/large, 0 for xl_sold")

plt.show()
