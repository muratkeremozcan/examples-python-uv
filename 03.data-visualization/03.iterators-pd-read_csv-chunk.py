import pandas as pd

# Processing large CSV files in chunks prevents memory overload.
# A dictionary is used to count occurrences of unique values in a CSV column.
# Iterating over a DataFrame column gives direct access to its values.
# Using `chunksize` in `pd.read_csv()` creates an iterable that loads part
# of the file at a time.

# Initialize an empty dictionary to store counts
counts_dict = {}

# Define the chunk size for processing
chunk_size = 10

# Process the CSV file in chunks
for chunk in pd.read_csv("tweets.csv", chunksize=chunk_size):
    # Iterate over the 'lang' column in each chunk
    for entry in chunk["lang"]:
        # Increment count if key exists, otherwise initialize it
        counts_dict[entry] = counts_dict.get(entry, 0) + 1

# Print the populated dictionary (language occurrences)
print(counts_dict)

#############
# Defining a function to encapsulate the logic for reusability


def count_entries(csv_file, c_size, col_name):
    """
    Return a dictionary with counts of occurrences as values for each unique key.

    Parameters:
    -----------
    csv_file : str
        Path to the CSV file
    c_size : int
        Chunk size for reading the CSV
    col_name : str
        Name of the column to count occurrences in

    Returns:
    --------
    dict
        Dictionary with column values as keys and their frequency as values.
    """
    counts_dict = {}

    # Process CSV file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize=c_size):
        for entry in chunk[col_name]:
            counts_dict[entry] = counts_dict.get(entry, 0) + 1

    return counts_dict


# Call function to count occurrences in 'lang' column
result_counts = count_entries("tweets.csv", 10, "lang")

# Print the result
print(result_counts)
