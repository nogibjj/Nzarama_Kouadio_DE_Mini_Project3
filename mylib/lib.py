import polars as pl
import matplotlib.pyplot as plt

# Load the dataset
dataset = "dataset/police_killings.csv"


def load_dataset(dataset):
    """Loads the dataset"""
    content_df = pl.read_csv(dataset, encoding="ISO-8859-1", null_values=["-", "NA"])

    # Clean the age column by removing unknown references and converting to numeric
    content_df = content_df.with_columns(
        [
            pl.when(pl.col("age") == "Unknown")
            .then(None)  # Replace "Unknown" with None (null)
            .otherwise(pl.col("age"))
            .cast(pl.Float64)  # Cast the column to Float64
        ]
    )

    return content_df


# Data Calculation Functions
def grab_mean(content_df, col):
    """Returns the mean of a column"""
    return content_df[col].mean()


def grab_median(content_df, col):
    """Returns the median of a column"""
    return content_df[col].median()


def grab_std_deviation(content_df, col):
    """Returns the standard deviation of a column"""
    return content_df[col].std()


def grab_min(content_df, col):
    """Returns the minimum value inside a column"""
    return content_df[col].min()


def grab_max(content_df, col):
    """Returns the maximum value inside a column"""
    return content_df[col].max()


# Data Visualization: Distribution of police killings across gender
def gender_pie_chart(content_df, show_plot=True):
    """Create and display a pie chart of police killings by gender"""
    # Count occurrences of each gender using Polars
    gender_counts = (
        content_df.group_by("gender")
        .agg(pl.count("gender").alias("count"))
        .sort("gender")
    )

    # Extract the labels (genders) and values (counts)
    genders = gender_counts["gender"].to_list()
    counts = gender_counts["count"].to_list()

    # Plot the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(
        counts,
        labels=genders,
        autopct="%1.1f%%",
        startangle=90,
        colors=["blue", "pink"],
        wedgeprops={"edgecolor": "black"},
    )
    plt.title("Police Killings by Gender (in percent %)")
    plt.xlabel("Gender")
    plt.grid(True)

    # Save the plot and display if show_plot is True
    plt.savefig("killings_by_gender.png")
    if show_plot:
        plt.show()
