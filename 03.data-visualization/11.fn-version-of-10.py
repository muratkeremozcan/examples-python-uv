# Encapsulates logic in a function (plot_pop) to allow flexible usage with different country codes.
# 	•	Processes large CSVs in chunks, avoiding memory overload.
# 	•	Uses filtering (df_urb_pop['CountryCode'] == country_code) to select data for a specific country.
# 	•	Uses zip() to combine 'Total Population' and 'Value' (urban percentage) columns.
# 	•	Computes the Total Urban Population dynamically using list comprehension.
# 	•	Uses pd.concat() to progressively merge chunks into a single DataFrame.
# 	•	Plots the final processed data using Matplotlib.

import os  # Used for constructing the correct file path

import matplotlib.pyplot as plt
import pandas as pd

# Get path to current directory (ensures compatibility with different environments)
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "ind_pop_data.csv")


def plot_pop(filename, country_code):
    """
    Processes a large CSV file in chunks and plots total urban population for a given country.

    Parameters:
    - filename (str): Path to the CSV file.
    - country_code (str): Country code to filter the dataset.

    Returns:
    - A scatter plot of 'Total Urban Population' vs. 'Year'.
    """

    # Initialize an empty DataFrame to store results
    data = pd.DataFrame()

    # Read CSV in chunks to handle large files efficiently
    urb_pop_reader = pd.read_csv(
        filename, chunksize=10, quotechar='"', escapechar="\\", on_bad_lines="warn"
    )

    # Process each chunk of data
    for df_urb_pop in urb_pop_reader:

        # Filter the chunk to include only the specified country
        df_pop_ceb = df_urb_pop[df_urb_pop["CountryCode"] == country_code]

        # Zip 'Total Population' with 'Value' (which represents Urban %)
        pops = zip(df_pop_ceb["Total Population"], df_pop_ceb["Value"])

        # Convert zip object into a list
        pops_list = list(pops)

        # Compute 'Total Urban Population' using list comprehension
        df_pop_ceb["Total Urban Population"] = [
            int(tup[0] * tup[1] * 0.01) for tup in pops_list
        ]

        # Merge processed chunk into the final DataFrame
        data = pd.concat([data, df_pop_ceb])

    # Generate scatter plot of Total Urban Population over time
    data.plot(kind="scatter", x="Year", y="Total Urban Population")
    plt.show()


# Run the function for 'CEB' country code
plot_pop(csv_path, "CEB")
