# app/utils.py
import pandas as pd
import plotly.express as px


def load_data(countries):
    dfs = {}
    for country in countries:
        path = f"data/{country.lower().replace(' ', '_')}_clean.csv"
        df = pd.read_csv(path, parse_dates=["Timestamp"])
        df["Country"] = country
        dfs[country] = df
    return dfs


def plot_boxplot(dfs, metric):
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
