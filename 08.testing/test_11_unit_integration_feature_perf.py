import pandas as pd
import pytest

DF_PATH = "08.testing/salaries.csv"


@pytest.fixture
def read_df():
    return pd.read_csv(DF_PATH)


# what is this doing?
# •	Here, .agg (short for “aggregate”) takes a dict that maps column names to aggregation functions.
# 	•	In our case, we’re telling pandas: “For each work_year group, run describe() on the salary column.”
# 	•	Calling describe() on a numeric column returns a Series of summary stats:
# 	•	count, mean, std, min, 25%, 50% (median), 75%, max
# 	•	The result of .agg({"salary": "describe"}) is a DataFrame whose rows are indexed by work_year and whose columns are those descriptive‐stat labels.
# Roughly, you get a table like this:
# work_year	count	mean			std				min			25%			50%			75%			max
# 2020			2			55 000.0	7 071.07	50 000	52 500	55 000	57 500	60 000
# 2021			2			75 000.0	7 071.07	70 000	72 500	75 000	77 500	80 000
# 2022			2			92 500.0	3 535.53	90 000	91 250	92 500	93 750	95 000
def get_grouped(df):
    return df.groupby("work_year").agg({"salary": "describe"})["salary"]


##############
# Unit test
# it checks that your fixture returns a non‐empty DataFrame
def test_read_df(read_df):
    # check the type of the dataframe
    assert isinstance(read_df, pd.DataFrame)
    # Check that read_df contains rows
    assert len(read_df) > 0
    # check the shape of the dataframe
    assert read_df.shape[0] > 0
    # more check
    assert read_df.shape == (6, 2)


# Integration test
# checks that multiple layers (CSV → DataFrame → grouping) interoperate correctly.
def test_get_grouped(read_df):
    salary_by_year = get_grouped(read_df)
    # check the nulls
    # 1. salary_by_year.isnull() → DataFrame of booleans
    # 2. .sum() → Series where each entry = null‐count for one column
    # 3. another .sum() → single integer = total nulls across all columns and rows.
    assert salary_by_year.isnull().sum().sum() == 0


# Feature test
# checks a specific deliverable or “feature” (the median salary for 2022) behaves as your users or requirements dictate.
def test_feature_2022(read_df):
    salary_by_year = get_grouped(read_df)
    salary_2022 = salary_by_year.loc[2022, "50%"]
    # check the median type
    assert isinstance(salary_2022, float)
    # check the median is greater than zero
    assert salary_2022 > 0


# Performance test using pytest-benchmark
def test_reading_speed(benchmark, read_df):
    # Benchmark the get_grouped function
    result = benchmark(get_grouped, read_df)

    # Basic assertion to ensure the function still works
    assert not result.empty

    # Performance assertion with realistic threshold (in seconds)
    # Based on benchmark results, operation takes ~4.3ms on average
    # Using 10ms as a safe upper limit to account for CI variability
    assert (
        benchmark.stats["mean"] < 0.01
    ), f"Grouping operation took {benchmark.stats['mean']*1000:.2f}ms, which is too slow"

    # You can also check the number of iterations and other stats
    assert benchmark.stats["iterations"] > 0

    # Print benchmark results for reference
    # print(f"\nPerformance stats for get_grouped:")
    # print(f"Mean time: {benchmark.stats['mean']:.6f} seconds")
    # print(f"Std dev: {benchmark.stats['stddev']:.6f} seconds")
    # print(f"Rounds: {benchmark.stats['rounds']}")
    # print(f"Iterations per round: {benchmark.stats['iterations']}")
