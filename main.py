"""
Main CLI or app entry point
"""

import polars as pl
from mylib.lib import (
    load_dataset,
    grab_mean,
    grab_median,
    grab_std_deviation,
    grab_min,
    grab_max,
    gender_pie_chart,
)

# Loading the data
dataset = "dataset/police_killings.csv"


def general_describe(dataset, columns=None):
    """General description function using Polars"""
    content_df = pl.read_csv(dataset, encoding="ISO-8859-1", ignore_errors=True)

    # Clean the 'age' column by replacing "Unknown" with None and converting to float
    content_df = content_df.with_columns(
        pl.col("age")
        .replace("Unknown", None)  # Replace "Unknown" with None (null)
        .cast(
            pl.Float64
        )  # Cast the column to a float (or pl.Int64 if i expect integers)
    )

    # If columns are specified, select only those columns
    if columns:
        content_df = content_df.select(columns)

    return content_df


def custom_describe(dataset, col):
    """Returns a dictionary of summary statistics for a column"""
    content_df = load_dataset(dataset)
    descriptive_dict = {
        "category": col,
        "mean": grab_mean(content_df, col),
        "median": grab_median(content_df, col),
        "std": grab_std_deviation(content_df, col),
        "min": grab_min(content_df, col),
        "max": grab_max(content_df, col),
    }
    return descriptive_dict


def chart_created(content_df, show_plot=False):
    """Gather all charts"""
    gender_pie_chart(content_df, show_plot)


def save_to_markdown(dataset):
    """Save summary report to markdown"""
    content_df = load_dataset(dataset)

    # Generate gender distribution statistics using Polars
    gender_distribution = (
        content_df.group_by("gender")
        .agg(pl.count("gender").alias("count"))
        .sort("gender")
    )

    # Create charts (e.g., gender distribution pie chart)
    chart_created(content_df, False)

    # Write the markdown table to a file
    with open(
        "killings_by_police_officers_summary.md", "a", encoding="ISO-8859-1"
    ) as file:
        # Write header
        file.write("# Police Killings Summary Report:\n\n")

        # Write summary statistics for gender distribution
        file.write("# Gender Distribution of People Killed by Police:\n")
        file.write(
            gender_distribution.to_pandas().to_markdown()
        )  # Convert to Pandas to export as Markdown
        file.write("\n\n")

        # Include charts
        file.write("![gender_image_fail_load](killings_by_gender.png)\n")


if __name__ == "__main__":
    save_to_markdown(dataset)
