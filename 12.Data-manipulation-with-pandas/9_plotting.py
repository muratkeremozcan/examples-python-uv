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

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby('size')['lbs_sold'].sum()
print(nb_sold_by_size)

# Bar: Compare quantities across categories (e.g., lbs_sold by size).
nb_sold_by_size.plot(kind='bar')
# plt.show()

# Line: Show trends over time (e.g., lbs_sold by date).
nb_sold_by_date = avocados.groupby('date')['lbs_sold'].sum()
nb_sold_by_date.plot(kind='line')
# plt.show()

# Scatter: Visualize relationships between two variables (e.g., lbs_sold vs avg_price).
avocados.plot(x='lbs_sold', y='avg_price', kind='scatter', title='Number of avocados sold vs. average price')
# plt.show()

# Histogram: Show distribution of a single variable (e.g., lbs_sold distribution)
avocados[avocados["type"] == "conventional"]["lbs_sold"].hist(alpha=0.5, bins=20)
avocados[avocados["type"] == "organic"]["lbs_sold"].hist(alpha=0.5, bins=20)

plt.legend(['conventional', 'organic'])
plt.show()
