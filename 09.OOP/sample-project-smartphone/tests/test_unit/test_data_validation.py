"""Unit tests for data validation in the smartphone data preparation."""

import pytest


# Test that there are no NaN values in critical columns
def test_nan_values(clean_smartphone_data):
    """Test that there are no NaN values in 'battery_capacity' or 'os' columns."""
    assert (
        clean_smartphone_data["battery_capacity"].isnull().sum() == 0
    ), "Found NaN values in battery_capacity column"
    assert (
        clean_smartphone_data["os"].isnull().sum() == 0
    ), "Found NaN values in os column"


# Test that all required columns are present
def test_required_columns(clean_smartphone_data):
    """Test that all required columns are present in the cleaned DataFrame."""
    required_columns = [
        "brand_name",
        "os",
        "price",
        "avg_rating",
        "processor_speed",
        "battery_capacity",
        "screen_size",
    ]
    for col in required_columns:
        assert col in clean_smartphone_data.columns, f"Missing required column: {col}"
