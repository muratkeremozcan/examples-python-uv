# KEY TAKEAWAYS:
# - Use os.path to build file paths that work regardless of current directory
# - groupby().sum() aggregates data by category (index)[value]
# - Create calculated columns with simple arithmetic operations
# - sort_values() orders data by column values
# - to_csv() exports DataFrames back to CSV files

import os

import pandas as pd

# import csv
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "airline_bumping.csv")

airline_bumping = pd.read_csv(csv_path)

print(airline_bumping)

# For each airline, select nb_bumped and total_passengers and sum
airline_totals = airline_bumping.groupby("airline")[
    ["nb_bumped", "total_passengers"]
].sum()
# Create new col, bumps_per_10k: no. of bumps per 10k passengers for each airline
airline_totals["bumps_per_10k"] = (
    airline_totals["nb_bumped"] / airline_totals["total_passengers"] * 10000
)

print(airline_totals)

# Create airline_totals_sorted
airline_totals_sorted = airline_totals.sort_values("bumps_per_10k", ascending=False)

# Print airline_totals_sorted
print(airline_totals_sorted)

# Save as airline_totals_sorted.csv in the same directory as this script
output_path = os.path.join(script_dir, "airline_totals_sorted.csv")
airline_totals_sorted.to_csv(output_path)
