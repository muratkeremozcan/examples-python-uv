"""Unit tests for visualization functions in visualize_versus_price.py"""

from unittest.mock import MagicMock, patch

import numpy as np
import pandas as pd
import pytest

# Import the functions to test
from visualize_versus_price import column_to_label, visualize_versus_price


# Test data for visualization tests
@pytest.fixture
def sample_visualization_data():
    """Create sample data for visualization tests."""
    return pd.DataFrame(
        {
            "price": [100, 200, 300, 400],
            "processor_speed": [2.0, 2.5, 3.0, 3.5],
            "battery_capacity": [3000, 3500, 4000, 4500],
            "os": ["Android", "iOS", "Android", "iOS"],
        }
    )


def test_column_to_label():
    """Test the column_to_label function."""
    assert column_to_label("processor_speed") == "Processor Speed"
    assert column_to_label("battery_capacity") == "Battery Capacity"
    assert column_to_label("os") == "Os"


def test_column_to_label_invalid_input():
    """Test column_to_label with invalid input."""
    with pytest.raises(TypeError):
        column_to_label(123)  # type: ignore
    with pytest.raises(TypeError):
        column_to_label(None)  # type: ignore


def test_visualize_versus_price_input_validation(sample_visualization_data):
    """Test input validation in visualize_versus_price."""
    # Test empty DataFrame
    with pytest.raises(ValueError, match="Input DataFrame is empty"):
        visualize_versus_price(pd.DataFrame(), "processor_speed")

    # Test missing required columns
    with pytest.raises(KeyError):
        visualize_versus_price(sample_visualization_data[["price"]], "processor_speed")
    with pytest.raises(KeyError):
        visualize_versus_price(
            sample_visualization_data[["processor_speed"]], "processor_speed"
        )
    with pytest.raises(KeyError):
        visualize_versus_data = sample_visualization_data.drop(columns=["os"])
        visualize_versus_price(visualize_versus_data, "processor_speed")


@patch("matplotlib.pyplot.show")
def test_visualize_versus_price_plotting(mock_show, sample_visualization_data):
    """Test that the plotting function is called with expected parameters."""
    with patch("seaborn.scatterplot") as mock_scatterplot:
        # Call the function
        visualize_versus_price(sample_visualization_data, "processor_speed")

        # Verify scatterplot was called with expected arguments
        args, kwargs = mock_scatterplot.call_args
        assert kwargs["x"] == "processor_speed"
        assert kwargs["y"] == "price"
        assert kwargs["hue"] == "os"
        assert kwargs["alpha"] == 0.7
        assert kwargs["s"] == 100
        assert kwargs["data"] is not None


@patch("matplotlib.pyplot.show")
def test_visualize_versus_price_titles(mock_show, sample_visualization_data):
    """Test that plot titles and labels are set correctly."""
    with (
        patch("matplotlib.pyplot.xlabel") as mock_xlabel,
        patch("matplotlib.pyplot.ylabel") as mock_ylabel,
        patch("matplotlib.pyplot.title") as mock_title,
        patch("matplotlib.pyplot.tight_layout") as mock_tight_layout,
    ):

        # Call the function
        visualize_versus_price(sample_visualization_data, "battery_capacity")

        # Verify labels and titles
        mock_xlabel.assert_called_once_with("Battery Capacity")
        mock_ylabel.assert_called_once_with("Price ($)")
        mock_title.assert_called_once_with(
            "Battery Capacity vs. Price", pad=20, fontsize=14, fontweight="bold"
        )
        mock_tight_layout.assert_called_once()
