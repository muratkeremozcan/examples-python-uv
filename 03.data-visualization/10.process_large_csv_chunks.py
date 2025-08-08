# - Use `pd.read_csv(..., chunksize=n)` to read large CSVs in chunks, avoiding memory overload.
# - `next(reader)` retrieves the next chunk (DataFrame) from the iterator.
# - Boolean indexing (`df[df['col'] == value]`) filters DataFrames based on column values.
# - `zip()` pairs values from multiple columns, useful for calculations.
# - Use list comprehensions to efficiently compute new columns.
# - Use `df.plot(kind='scatter', x=..., y=...)` to visualize data.

import os

import matplotlib.pyplot as plt
import pandas as pd

# Get the absolute path of the CSV file to avoid path issues
# how to read file from anywhere
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "ind_pop_data.csv")

# Initialize reader object to process CSV in chunks
df_reader = pd.read_csv(csv_path, chunksize=10)

# Print the first two chunks (first 10 rows, then next 10 rows)
print(next(df_reader))
print(next(df_reader))


######### Process Population Data in Chunks #########

# Initialize reader object again
urb_pop_reader = pd.read_csv(csv_path, chunksize=10)

# Retrieve the first chunk
df_urb_pop = next(urb_pop_reader)

# Print first few rows
print(df_urb_pop.head())


######### Filter Data for a Specific Country #########

# Print 'CountryCode' column
print(df_urb_pop["CountryCode"])

# Boolean filtering: Create a Series where 'CountryCode' is 'CEB' (Central
# Europe and Baltics)
print(df_urb_pop["CountryCode"] == "CEB")

# Use Boolean indexing to filter DataFrame
df_pop_ceb = df_urb_pop[df_urb_pop["CountryCode"] == "CEB"]
# JS equivalent: df_pop_ceb = df_urb_pop.filter(row => row.CountryCode === "CEB");
print(df_pop_ceb)


######### Pair Population and Urban Percentage Data #########

# Print the 'Total Population' column
print(df_pop_ceb["Total Population"])

# The urban percentage is stored in the 'Value' column
print(df_pop_ceb["Value"])

# Pair 'Total Population' and 'Value' using zip()
pops = zip(df_pop_ceb["Total Population"], df_pop_ceb["Value"])
print(pops)  # This prints the zip object reference

# Convert zip object into a list of tuples
pops_list = list(pops)
print(pops_list)


######### Compute Total Urban Population #########

# Compute Total Urban Population = Total Population × Urban percentage ÷ 100
df_pop_ceb["Total Urban Population"] = [int(pop[0] * pop[1] / 100) for pop in pops_list]

# Plot urban population data
df_pop_ceb.plot(kind="scatter", x="Year", y="Total Urban Population")
plt.show()
