# - Use `df.plot(kind='scatter', x=..., y=...)` to visualize data.
# kinds of plots: line, bar, scatter, histogram, density, box, hexbin
# Key Takeaways:
# - Bar: Compare quantities across categories (e.g., lbs_sold by size).
# - Line: Show trends over time (e.g., lbs_sold by date).
# - Scatter: Visualize relationships between two variables (e.g., lbs_sold vs avg_price).
# - Histogram: Show distribution of a single variable (e.g., lbs_sold distribution).
# - Box: Summarize distribution and outliers.
# - Density: Smooth distribution estimate.
# - Hexbin: Density of points in 2D (for large scatter plots).

import matplotlib.pyplot as plt
from dataframes.avocados import avocados

# Look at the first few rows of data
print(avocados.head())
print()

# Get the total number of avocados sold of each size (index)[values]
nb_sold_by_size = avocados.groupby("size")["lbs_sold"].sum()
print("\nBar graph: Compare quantities across categories (e.g., lbs_sold by size).")
print(nb_sold_by_size)

# Create a figure with 2 subplots (10 by 12 inches)
plt.figure(figsize=(10, 12))

# First subplot - Bar graph
plt.subplot(2, 1, 1)  # 2 rows of graphs, 1 column of graph, 1st subplot
print("\nBar graph: Compare quantities across categories (e.g., lbs_sold by size).")
nb_sold_by_size.plot(kind="bar")
plt.title(
    "Total Avocados Sold by Size - Bar graph: Compare quantities across categories"
)
plt.ylabel("Total lbs Sold")

# Second subplot - Line graph
plt.subplot(2, 1, 2)  # 2 rows of graphs, 1 column of graph, 2nd subplot
nb_sold_by_date = avocados.groupby("date")["lbs_sold"].sum()
print("\nLine graph: Show trends over time (e.g., lbs_sold by date).")
print(nb_sold_by_date)
nb_sold_by_date.plot(kind="line")
plt.title("Avocados Sold Over Time - Line graph: Show trends over time")
plt.ylabel("Total lbs Sold")

# Adjust layout to prevent overlap
plt.tight_layout()
plt.show()

# ===== FIGURE 2: Additional Plots =====
plt.figure(figsize=(14, 10))  # Slightly wider for better layout

# First subplot - Scatter plot
plt.subplot(2, 1, 1)  # 2 rows, 1 column, 1st subplot
print("\nScatter plot: Relationship between price and quantity sold")
avocados.plot(
    x="avg_price",
    y="lbs_sold",
    kind="scatter",
    alpha=0.5,
    ax=plt.gca(),  # Use current subplot
)
plt.title("Price vs Quantity Sold - Scatter: Visualize relationships")
plt.xlabel("Average Price ($)")
plt.ylabel("Pounds Sold")

# Second subplot - Histogram
plt.subplot(2, 1, 2)  # 2 rows, 1 column, 2nd subplot
print("\nHistogram: Distribution of sales by avocado type")

# Plot histograms for each type
avocados[avocados["type"] == "conventional"]["lbs_sold"].hist(
    alpha=0.5, bins=20, label="conventional"
)
avocados[avocados["type"] == "organic"]["lbs_sold"].hist(
    alpha=0.5, bins=20, label="organic"
)

plt.title("Distribution of Pounds Sold by Avocado Type - Histogram: Show distribution")
plt.xlabel("Pounds Sold")
plt.ylabel("Frequency")
plt.legend()

# Adjust layout
plt.tight_layout()
plt.show()
