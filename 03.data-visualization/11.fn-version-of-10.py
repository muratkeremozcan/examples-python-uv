# Encapsulates logic in a function (plot_pop) to allow flexible usage with different country codes.
# 	•	Processes large CSVs in chunks (configurable chunksize) to bound memory.
# 	•	Vectorized computation and .loc copy avoid SettingWithCopy warnings.
# 	•	Collects chunk results in a list and concatenates once to reduce overhead.
# 	•	Reads only needed columns via usecols to cut I/O and memory.
# 	•	Plots the final processed data using Matplotlib (optional).

import os  # Used for constructing the correct file path

import matplotlib.pyplot as plt
import pandas as pd

# Get path to current directory (ensures compatibility with different environments)
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "ind_pop_data.csv")


def plot_pop(filename, country_code, chunksize=1000, plot=True):
    """
    Processes a large CSV file in chunks and plots total urban population for a given country.

    Parameters:
    - filename (str): Path to the CSV file.
    - country_code (str): Country code to filter the dataset.
    - chunksize (int): Number of rows per chunk to stream from CSV.
    - plot (bool): Whether to render the scatter plot.

    Returns:
    - DataFrame with filtered rows and computed 'Total Urban Population'.
    """

    data_frames = []

    # Read CSV in chunks to handle large files efficiently
    urb_pop_reader = pd.read_csv(
        filename,
        chunksize=chunksize,
        quotechar='"',
        escapechar="\\",
        on_bad_lines="warn",
        usecols=["CountryCode", "Total Population", "Value", "Year"],
    )

    # Process each chunk of data
    for df_urb_pop in urb_pop_reader:

        # Filter the chunk to include only the specified country
        mask = df_urb_pop["CountryCode"] == country_code
        if not mask.any():
            continue
        df_pop_ceb = df_urb_pop.loc[mask].copy()  # copy to avoid chained assignment

        # Compute 'Total Urban Population' using vectorized math
        df_pop_ceb["Total Urban Population"] = (
            df_pop_ceb["Total Population"] * df_pop_ceb["Value"] * 0.01
        ).astype(int)

        # Collect processed chunk
        data_frames.append(df_pop_ceb)

    if not data_frames:
        print(f"No data found for country code '{country_code}'.")
        return pd.DataFrame()

    data = pd.concat(
        data_frames, ignore_index=True
    )  # single concat is faster than per-chunk

    if plot:
        # Generate scatter plot of Total Urban Population over time
        data.plot(kind="scatter", x="Year", y="Total Urban Population")
        plt.show()

    return data


# Run the function for 'CEB' country code
plot_pop(csv_path, "CEB")
