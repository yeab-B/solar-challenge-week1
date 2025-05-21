"""Utility functions for loading and plotting solar data."""
import pandas as pd
import plotly.express as px


def load_data(countries):
    """Loads data for specified countries from CSV files.

    Args:
        countries (list): A list of country names.

    Returns:
        dict: A dictionary where keys are country names and values are
            pandas DataFrames.
    """
    dfs = {}
    for country in countries:
        path = f"data/{country.lower().replace(' ', '_')}_clean.csv"
        df = pd.read_csv(path, parse_dates=["Timestamp"])
        df["Country"] = country
        dfs[country] = df
    return dfs


def plot_boxplot(dfs, metric):
    """Generates a boxplot for a given metric across countries.

    Args:
        dfs (dict): A dictionary of DataFrames, keyed by country name.
        metric (str): The name of the column to plot.

    Returns:
        plotly.graph_objs._figure.Figure: A Plotly figure object.
    """
    combined = pd.concat([df for df in dfs.values()])
    fig = px.box(
        combined,
        x="Country",
        y=metric,
        color="Country",
        title=f"{metric} Boxplot"
    )
    return fig


def plot_summary_table(dfs):
    """
    Creates a summary table of GHI, DNI, and DHI statistics for each country.

    Args:
        dfs (dict): A dictionary of DataFrames, keyed by country name.

    Returns:
        pandas.DataFrame: A DataFrame containing summary statistics.
    """
    rows = []
    for country, df in dfs.items():
        row = {
            "Country": country,
            "GHI_mean": df["GHI"].mean(),
            "GHI_median": df["GHI"].median(),
            "GHI_std": df["GHI"].std(),
            "DNI_mean": df["DNI"].mean(),
            "DNI_median": df["DNI"].median(),
            "DNI_std": df["DNI"].std(),
            "DHI_mean": df["DHI"].mean(),
            "DHI_median": df["DHI"].median(),
            "DHI_std": df["DHI"].std(),
        }
        rows.append(row)
    return pd.DataFrame(rows)
