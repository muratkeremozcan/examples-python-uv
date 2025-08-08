# 1. Reading and Parsing Dates:
#    - Read CSV with datetime parsing: pd.read_csv(parse_dates=['column_name'])
#    - Access datetime properties/methods with .dt accessor (ex: ride_durations.dt.total_seconds())
#
# 2. Time Delta Operations:
#    - Calculate time differences between datetime columns
#    - Convert timedelta to seconds: .dt.total_seconds()
#
# 3. Boolean Masking and Filtering:
#    - Create boolean masks for filtering: df['col1'] == df['col2'] (ex: joyrides = rides['Start station'] == rides['End station'])
#    - Filter data using boolean masks: df[mask] (ex: joyrides = rides[joyrides])
#    - Use .sum() on boolean masks to count True values
#
# 4. Statistical Analysis:
#    - Use median() for duration analysis (less affected by outliers than mean)
#
# 5. Time Series Resampling:
#    - Resample time series data: df.resample('D', on='date_column')
#    - Common frequency strings: 'D' (daily), 'M' (monthly), 'H' (hourly), 'W' (weekly)
#    - Get counts per period: .size()
#    - Plot time series data directly: .plot()
#
# 6. Grouping by Time and Categories:
#    - Group by member type and resample: df.groupby('Member type').resample('M', on='date_column')
#    - Calculate value counts ratios: .value_counts() / .size()
#
# 7. Visualization:
#    - Set y-axis limits: .plot(ylim=[min, max])
#    - Display plots: plt.show()
#
# 8. Timezone Handling:
#    - Localize: df['ts'] = df['ts'].dt.tz_localize('America/New_York', ambiguous='NaT')
#    - Convert:  df['ts'] = df['ts'].dt.tz_convert('Europe/London')
#
# 9. Feature Extraction – Weekday:
#    - df['weekday'] = df['ts'].dt.day_name()
#    - df.groupby('weekday')['Duration'].median()
#
# 10. Lagged & Inter-Event Metrics:
#    - prev = df['End date'].shift(1)
#    - df['Time since'] = (df['Start date'] - prev).dt.total_seconds()
#    - Resample that metric: df.resample('M', on='Start date')['Time since'].mean()/3600
#


import os

import pandas as pd

# read file from anywhere
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "capital-onebike.csv")

# Read CSV and parse date columns into datetime objects
rides = pd.read_csv(csv_path, parse_dates=["Start date", "End date"])
print(rides.iloc[0])

# Calculate time differences between end and start dates
# This creates a timedelta64[ns] Series
ride_durations = rides["End date"] - rides["Start date"]

# Convert timedelta to total seconds for easier analysis
# dt accessor provides datetime properties/methods
rides["Duration"] = ride_durations.dt.total_seconds()
print(rides["Duration"].head())


###########
# Boolean mask to identify joyrides (start and end at same station)
# This creates a Series of True/False values where True indicates a joyride
joyrides = rides["Start station"] == rides["End station"]
print("{} rides were joyrides".format(joyrides.sum()))

# Median is used instead of mean because it's less affected by outliers
print("Median ride duration: {} seconds".format(rides["Duration"].median()))

# Filter the DataFrame using the boolean mask and calculate median duration
# This is an example of boolean indexing in pandas
print(
    "Median joyride duration: {} seconds".format(rides[joyrides]["Duration"].median())
)

import matplotlib.pyplot as plt

# resample('D') is a frequency string that tells pandas to group the data into daily bucket

# Your CSV has timestamps in the 'Start date' column like:
# 2017-10-01 15:23:25
# 2017-10-01 15:42:57 (same day)
# 2017-10-02 06:37:10 (next day)
# When you do resample('D'), pandas:
# Groups all timestamps by their date (ignoring the time part)
# Creates one group for each unique date
# For example, both 2017-10-01 15:23:25 and 2017-10-01 15:42:57 go into the same daily bucket
# The .size() then counts how many rides occurred in each daily bucket.

# Common frequency strings in pandas:
# 'D' = daily
# 'H' = hourly
# 'W' = weekly
# 'M' = monthly
# '15T' = 15 minutes
# '30S' = 30 seconds

rides.resample("D", on="Start date").size().plot(ylim=[0, 15])  # line plot with y limit

# plt.show() # optional


# resample and just select 'Member type' column from the resampled DataFrame
monthly_rides = rides.resample("M", on="Start date")["Member type"]

# Take the ratio of the .value_counts() over the total number of rides
print(monthly_rides.value_counts() / monthly_rides.size())

# Group rides by member type, and resample to the month
grouped = rides.groupby("Member type").resample("M", on="Start date")

# Print the median duration for each group
print(grouped["Duration"].median())

####
# Localize the Start date column to America/New_York
rides["Start date"] = rides["Start date"].dt.tz_localize(
    "America/New_York", ambiguous="NaT"
)

print(rides["Start date"].iloc[0])

# Convert the Start date column to Europe/London
rides["Start date"] = rides["Start date"].dt.tz_convert("Europe/London")
print(rides["Start date"].iloc[0])

# Add a column for the weekday of the start of the ride
rides["Ride start weekday"] = rides["Start date"].dt.day_name()
# Print the median trip time per weekday
print(rides.groupby("Ride start weekday")["Duration"].median())

# Shift the index of the end date up one; now subtract it from the start date
rides["Time since"] = rides["Start date"] - rides["End date"].shift(1)
# Move from a timedelta to a number of seconds, which is easier to work with
rides["Time since"] = rides["Time since"].dt.total_seconds()
# Resample to the month
monthly_rides = rides.resample("M", on="Start date")
# Print the average hours between rides each month
print(monthly_rides["Time since"].mean() / 3600)
