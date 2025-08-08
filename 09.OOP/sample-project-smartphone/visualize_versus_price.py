# visualize_versus_price.py
# - Creates scatter plots of features vs price
# - Uses seaborn/matplotlib for visualization
# - Colors points by OS

import matplotlib.pyplot as plt
import seaborn as sns


def column_to_label(column_name):
    """
    Convert a column name to a label suitable for plot axes and titles.

    Args:
        column_name (str): Column name in snake_case.

    Returns:
        str: Human-readable label for display on plots.

    Raises:
        TypeError: If column_name is not a string.
    """
    if not isinstance(column_name, str):
        raise TypeError("column_name must be of type 'str'.")

    return " ".join(column_name.split("_")).title()


def visualize_versus_price(clean_data, x):
    """
    Create a scatter plot of a selected feature versus price.

    Args:
        clean_data (pd.DataFrame): Cleaned smartphone data.
        x (str): Column name to plot on the x-axis.

    Returns:
        None
    """
    if clean_data.empty:
        raise ValueError("Input DataFrame is empty.")

    required_columns = {x, "price", "os"}
    missing_columns = required_columns - set(clean_data.columns)
    if missing_columns:
        raise KeyError(f"Missing columns: {', '.join(missing_columns)}")

    # Create the scatterplot
    sns.scatterplot(x=x, y="price", data=clean_data, hue="os", alpha=0.7, s=100)

    # Add axis labels
    plt.xlabel(column_to_label(x))
    plt.ylabel("Price ($)")

    # Add a title
    plt.title(f"{column_to_label(x)} vs. Price", pad=20, fontsize=14, fontweight="bold")

    # Show plot
    plt.tight_layout()
    plt.show()


def main():
    """Example usage of the visualization function."""
    # This would be used when running the script directly
    # For testing, we'll just print a message
    print("This script is meant to be imported, not run directly.")
    print("Use the visualize_versus_price() function in your code.")


if __name__ == "__main__":
    main()
