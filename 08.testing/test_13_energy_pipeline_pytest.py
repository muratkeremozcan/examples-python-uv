import pandas as pd
import pytest

DF_PATH = "https://assets.datacamp.com/production/repositories/6253/datasets/f015ac99df614ada3ef5e011c168054ca369d23b/energy_truncated.csv"


def get_data():
    return pd.read_csv(DF_PATH)


# finds the minimum value in that column
# returns the index label of the first row where that minimum value appears
def min_country(df):
    return df["VALUE"].idxmin()


@pytest.fixture
def set_up():
    df = get_data()
    df.drop("previousYearToDate", axis=1, inplace=True)
    df = df.groupby("COUNTRY").agg({"VALUE": "sum"})
    yield df  # this is where the test runs, or you can return df / the last line
    # Use yield if you need teardown code that runs after the test
    # Use return for simpler cases without teardown
    # in Pytest you never need teardown, it handles it (but these examples show it for some reason)

    # Teardown: pytest handles this
    # df.drop(df.index, inplace=True)


def test_nas(set_up):
    # Check the number of nulls in the entire DataFrame
    assert set_up.isna().sum().sum() == 0


def test_argmax(set_up):
    # Check that min_country returns a string
    assert isinstance(min_country(set_up), str)


# Pytest is designed to handle cleanup automatically, just like Jest. The only times you'd need to think about teardown are the rare edge cases like:

# Working with files on disk
# Managing database connections
# Interacting with external services
# Using module/session-scoped fixtures that modify external state
