"""
Test goes here
"""

import polars as pl
from main import general_describe, custom_describe, save_to_markdown

test_dataset = "dataset/police_killings.csv"


def testing_describe():
    """Test .describe with custom describe function"""
    # Run general and custom describe
    describe_test = general_describe(test_dataset)
    custom_test = custom_describe(test_dataset, "age")

    # Assert the calculated statistics match for the 'age' column
    assert describe_test.select(pl.col("age").mean()).item() == custom_test["mean"]
    assert describe_test.select(pl.col("age").std()).item() == custom_test["std"]
    assert describe_test.select(pl.col("age").min()).item() == custom_test["min"]


def testing_charts():
    """Test markdown conversion"""
    save_to_markdown(test_dataset)


if __name__ == "__main__":
    testing_describe()
    testing_charts()
