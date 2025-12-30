import os

import pandas as pd
import pytest


@pytest.fixture
def data():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    df = pd.read_csv(os.path.join(test_dir, "games.csv"))
    yield df
    # Teardown: Clear the DataFrame
    df.drop(df.index, inplace=True)
    # No need for 'delete df' - Python handles this automatically


def test_type(data):
    assert isinstance(data, pd.DataFrame)


def test_shape(data):
    assert data.shape[0] == 82
