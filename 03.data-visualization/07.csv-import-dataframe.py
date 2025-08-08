# Extracting Data from a DataFrame Column
# •	df['column_name'] extracts a single column as a pandas Series.
# List Comprehension for Data Extraction
# •	[entry[start:end] for entry in iterable] extracts specific slices from each element.
# Conditional Filtering in List Comprehensions
# •	[output | for item in iterable | if condition] filters elements before adding them to the list.

import pandas as pd

# Load the csv file into a DataFrame
df = pd.read_csv("tweets.csv")

# Extract the 'created_at' column (this is a Series)
tweet_time = df["created_at"]

# **Extract clock time from timestamp**
# - The timestamp format is likely: "YYYY-MM-DD HH:MM:SS"
# - Extract characters from index **11 to 19** → "HH:MM:SS"
tweet_clock_time = [entry[11:19] for entry in tweet_time]
print(tweet_clock_time)

# **Filter times ending in '19' seconds**
# - Extract times, but only keep those where **seconds = '19'**
tweet_clock_time2 = [entry[11:19] for entry in tweet_time if entry[17:19] == "19"]
print(tweet_clock_time2)
