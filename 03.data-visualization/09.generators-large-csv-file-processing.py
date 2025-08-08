# Reading Files in Chunks vs. Whole File
# •	Reading an entire file at once can be memory-intensive.
# •	Reading line-by-line (chunking) reduces memory usage.

# Using a Dictionary for Counting Occurrences
# •	{key: count} structure is useful for counting occurrences of unique values in a dataset.

# Generators for Efficient File Handling
# •	Instead of storing all lines in memory, generators (yield) read data lazily (on demand).
# •	Useful when processing large datasets without exhausting memory.

# How read_large_file() Works
# •	Reads one line at a time, then yields it for processing.
# •	Stops reading when the end of the file is reached.

# Open a connection to the file
with open("world_indicators_simple.csv", "r") as file:

    # Skip the column names (first line)
    file.readline()

    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Process only the first 10 rows
    for j in range(10):

        # Read the next line, strip spaces, and split by commas
        line = file.readline().strip().split(",")

        # Get the value for the first column: first_col
        first_col = line[0]

        # If first_col exists in the dictionary, increment count
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1

        # Otherwise, add it to the dictionary with count 1
        else:
            counts_dict[first_col] = 1

# Print the resulting dictionary (unique values and their counts)
print(counts_dict)


############
# What if you want to process the **entire file** efficiently?
# Instead of reading all lines at once, use **generators** to read lazily.


def read_large_file(file_object):
    """A generator function to read a large file lazily."""

    # Loop indefinitely until the end of the file
    while True:
        # Read one line
        data = file_object.readline()

        # Break if EOF is reached
        if not data:
            break

        # Yield (return) the line instead of storing it
        yield data


# Open a connection to the file
with open("world_indicators_simple.csv") as file:
    # Create a generator object for the file: gen_file
    gen_file = read_large_file(file)

    # Print the first three lines of the file
    print(next(gen_file))  # Fetches first line
    print(next(gen_file))  # Fetches second line
    print(next(gen_file))  # Fetches third line


# Processing entire file using generator

# Initialize an empty dictionary for counting occurrences
counts_dict2 = {}

with open("world_indicators_simple.csv") as file:
    # Iterate over the generator function, reading line by line
    for line in read_large_file(file):

        # Remove spaces and split by commas
        row = line.strip().split(",")

        # Extract first column value
        first_col = row[0]

        # If first_col exists, increment count
        if first_col in counts_dict2.keys():
            counts_dict2[first_col] += 1

        # Otherwise, add it to the dictionary with count 1
        else:
            counts_dict2[first_col] = 1

# Print the dictionary with unique values and their counts
print(counts_dict2)
