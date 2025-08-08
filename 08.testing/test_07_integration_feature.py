import pandas as pd
import pytest


# Fixture to read the dataframe
@pytest.fixture
def get_df():
    return pd.read_csv(
        "https://assets.datacamp.com/production/repositories/6253/datasets/757c6cb769f7effc5f5496050ea4d73e4586c2dd/laptops_train.csv"
    )


# Aggregation feature
def agg_with_sum(data, group_by_column, aggregate_column):
    return data.groupby(group_by_column)[aggregate_column].sum()


########################


# Integration test
# verify the type of the object returned from get_df equals pd.DataFrame.
def test_get_df(get_df):
    assert isinstance(get_df, pd.DataFrame)

    # check the number of rows
    assert len(get_df) > 0


# Feature test
# checks a specific deliverable or “feature”  behaves as your users or requirements dictate.
def test_agg_feature(get_df):
    # prepare the feature
    aggregated = agg_with_sum(get_df, "Manufacturer", "Price")

    # check the type
    assert isinstance(aggregated, pd.Series)

    # Test the number of rows of the aggregated is more than 0
    assert len(aggregated) > 0

    # Test the data type of the aggregated
    assert aggregated.dtype in (int, float)
