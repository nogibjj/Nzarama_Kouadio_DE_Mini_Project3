"""
We test here
"""

# Import Libraries
import polars as pl
from mylib.lib import (
    load_dataset,
    grab_mean,
    grab_median,
    grab_std_deviation,
    grab_min,
    grab_max,
)

test_dataset = "dataset/police_killings.csv"


def testing_summary_statistics():
    """Testing if statistics are properly being calculated"""
    # Load dataset
    content_df = load_dataset(test_dataset)

    # Test individual statistics
    testing_mean = grab_mean(content_df, "day")
    testing_median = grab_median(content_df, "day")
    testing_std_deviation = grab_std_deviation(content_df, "day")
    testing_min = grab_min(content_df, "day")
    testing_max = grab_max(content_df, "day")

    # Generate the same statistics using Polars select
    describe_test = content_df.select(
        [
            pl.col("day").mean().alias("mean"),
            pl.col("day").median().alias("median"),
            pl.col("day").std().alias("std"),
            pl.col("day").min().alias("min"),
            pl.col("day").max().alias("max"),
        ]
    )

    # Assert that the manually calculated statistics match the calculations for "day"
    assert describe_test["mean"].item() == testing_mean
    assert describe_test["median"].item() == testing_median
    assert describe_test["std"].item() == testing_std_deviation
    assert describe_test["min"].item() == testing_min
    assert describe_test["max"].item() == testing_max


if __name__ == "__main__":
    testing_summary_statistics()
