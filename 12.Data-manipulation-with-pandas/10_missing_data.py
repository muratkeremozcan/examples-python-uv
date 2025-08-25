# use .isnull().sum() to check columns for missing values
# use .isnull().sum().plot(kind='bar') to plot missing values by variable
# isnull() is identical to isna() for this purpose
# can use .sum() for total number, .any() for boolean

# When there are missing values we can do a few things
# 1) one option is to remove the rows with missing values from the dataset
# to drop rows with missing values use .dropna()
# 2) another option is to fill the missing values with a specific value. For numeric values 0 is used
# to fill missing values use .fillna(<value>)

import matplotlib.pyplot as plt
from dataframes.avocados_2016 import avocados

# use .isnull().sum() to check columns for missing values
print(avocados.isnull().any())
print()
print(avocados.isnull().sum())

# when there are missing values we can do a few things

# 1) one option is to remove the rows with missing values from the dataset
avocados_complete = avocados.dropna()
# when we check again, there should be no missing values
print(avocados_complete.isna().any())

# use .isnull().sum().plot(kind='bar') to plot missing values by variable
# if we look at the original, we can check the missing values
avocados.isna().sum().plot(kind='bar') # Figure 1
# since we dropped the missing values, this would show no missing values
# avocados_complete.isna().sum().plot(kind='bar')

######################

# Histogram summary:
# A histogram visualizes data distribution by grouping values into bins.
# It helps identify patterns, spread, and outliers in numeric data.

# 2) another option is to fill the missing values with a specific value. For numeric values 0 is used

cols_with_missing = ['small_sold', 'large_sold', 'xl_sold']
# 2.a) Create histograms showing the distributions cols_with_missing
# Figure 2 : When you call .hist() on columns with NaNs, those missing rows are ignored. 
# so the histogram only reflects the actual non-missing values.
avocados[cols_with_missing].hist() 

# 2.b) Then fill in missing values with 0
# When you fill missing values with 0, you’re inserting actual zeros into the dataset.
# Now the histogram treats those zeros as valid values.
# This shifts the distribution: you’ll see extra bars piled up at 0 (or very low bins), because all the missing rows now contribute to the counts.
avocados_filled = avocados.fillna(0)
# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist() # Figure 3 : shows us missing values where Y axis is 0

plt.show()

# •	Use NaN if you want to keep track of “data was missing here” (so you don’t distort the distribution).
# •	Use 0 fill if a missing value really means zero (e.g., “no avocados sold”).
# •	Otherwise, filling with 0 can make it look like you had a lot of small values, which may mislead analysis.