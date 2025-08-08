"""Integration tests for price conversion in the smartphone data preparation."""

import os

import pandas as pd


# Test that price conversion from cents to dollars works correctly
def test_price_conversion(clean_smartphone_data):
    """Test that the 'price' column was correctly converted from cents to dollars."""
    # Get the path to the original data file
    data_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        "data",
    )
    data_path = os.path.join(data_dir, "smartphones.csv")

    # Load original prices from raw data
    original_prices = pd.read_csv(data_path)["price"]

    # Get converted prices back to cents for comparison
    converted_prices = clean_smartphone_data["price"] * 100

    # Convert both to float for comparison to avoid type mismatch
    pd.testing.assert_series_equal(
        original_prices.astype(float).sort_values(ignore_index=True),
        converted_prices.astype(float).sort_values(ignore_index=True),
        check_names=False,
        rtol=1e-5,  # Relative tolerance for floating point comparisons
    )
