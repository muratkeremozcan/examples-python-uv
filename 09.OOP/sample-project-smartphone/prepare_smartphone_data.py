# prepare_smartphone_data.py
# - Loads and cleans smartphone data
# - Removes rows with missing values
# - Converts price from cents to dollars

import os

import pandas as pd


def prepare_smartphone_data(file_path):
    """
    Load and clean smartphone data for visualization.

    The function applies the following transformations:
    - Selects only columns needed for analysis.
    - Removes records missing battery_capacity or os.
    - Converts price from cents to dollars.

    Args:
        file_path (str): Path to the CSV file containing smartphone data.

    Returns:
        pd.DataFrame: Cleaned DataFrame ready for visualization.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Read the raw data
    raw_data = pd.read_csv(file_path)
    print(
        raw_data.head()
    )  # TODO: For checking dataset; remove before final submission.

    # Columns to keep for analysis
    columns_to_keep = [
        "brand_name",
        "os",
        "price",
        "avg_rating",
        "processor_speed",
        "battery_capacity",
        "screen_size",
    ]

    # Check that all required columns exist
    missing_columns = [col for col in columns_to_keep if col not in raw_data.columns]
    if missing_columns:
        raise ValueError(f"Missing columns: {', '.join(missing_columns)}")

    # Select columns
    trimmed_data = raw_data[columns_to_keep].copy()

    # Remove rows missing battery_capacity or os
    cleaned_data = trimmed_data.dropna(subset=["battery_capacity", "os"])

    # Convert price from cents to dollars
    cleaned_data["price"] = cleaned_data["price"] / 100

    return cleaned_data


if __name__ == "__main__":
    # This block only runs when the script is executed directly
    import os

    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the data file
    data_path = os.path.join(script_dir, "data", "smartphones.csv")
    cleaned_data = prepare_smartphone_data(data_path)
    print("Data loaded successfully!")
    print("\nFirst 5 rows:")
    print(cleaned_data.head())
