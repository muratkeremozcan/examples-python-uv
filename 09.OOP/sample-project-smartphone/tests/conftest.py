import os
import sys

import pandas as pd
import pytest

# Add project root to Python path (cleaner than multiple os.path.dirname calls)
project_root = os.path.dirname(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from prepare_smartphone_data import prepare_smartphone_data


@pytest.fixture
def clean_smartphone_data():
    """Fixture to load and clean smartphone data."""
    data_path = os.path.join(project_root, "data", "smartphones.csv")
    return prepare_smartphone_data(data_path)
