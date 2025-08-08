# Extracting column names (df.columns.tolist()) and row values (df.iloc[i].tolist()).
# Using zip() to combine column names and row values into a dictionary.
# Using list comprehension to create multiple row dictionaries (list_of_dicts).
# Converting list of dictionaries back into a DataFrame (pd.DataFrame(list_of_dicts)).
# Function version (lists2dict) to generalize column-value pairing.

# 🚀 This file essentially demonstrates CSV-to-DataFrame round tripping via dictionaries while using zip() effectively.

import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("world_indicators_simple.csv")
print(df)  # Print the entire DataFrame

# Extract column names (header row)
feature_names = df.columns.tolist()

# Extract the first row values
row_vals = df.iloc[0].tolist()

# Use zip() to pair column names with row values
zipped_lists = zip(feature_names, row_vals)

# Convert zipped lists into a dictionary (column name -> value mapping)
rs_dict = dict(zipped_lists)

# Print the dictionary representation of the first row
print(rs_dict)


########### Function version for reusability ###########


def lists2dict(list1, list2):
    """
    Convert two lists into a dictionary, where list1 provides keys and list2 provides values.

    Parameters:
    - list1 (list): Keys (e.g., column names)
    - list2 (list): Values (e.g., row values)

    Returns:
    - dict: Dictionary mapping keys to values
    """

    # Zip lists together
    zipped_lists = zip(list1, list2)

    # Convert zipped lists into a dictionary
    rs_dict = dict(zipped_lists)

    return rs_dict


# Convert first row to a dictionary using the function
print(lists2dict(feature_names, row_vals))


########### Processing multiple rows ###########

# Extract all row values from the DataFrame
row_lists = [df.iloc[i].tolist() for i in range(len(df))]

# Print the first two row lists
print(row_lists[0])
print(row_lists[1])

# Create a list of dictionaries - one dictionary per row
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Print the first two row dictionaries
print(list_of_dicts[0])
print(list_of_dicts[1])

# Convert the list of dictionaries back into a DataFrame
df_from_dicts = pd.DataFrame(list_of_dicts)

# Print the first few rows of the newly created DataFrame
print(df_from_dicts.head())
