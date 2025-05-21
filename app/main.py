"""Streamlit dashboard for visualizing solar energy data."""
import streamlit as st
import pandas as pd
from utils import load_data, plot_boxplot, plot_summary_table

st.set_page_config(page_title="Solar Dashboard", layout="wide")
st.title("☀️ Solar Energy Insights Dashboard")

selected_countries = st.multiselect(
    "Select Countries",
    ["Benin", "Sierra Leone", "Togo"],
    default=["Benin", "Sierra Leone", "Togo"]
)

dfs = load_data(selected_countries)

# Tabs
tab1, tab2 = st.tabs(["📊 Metric Comparison", "📋 Summary Statistics"])

with tab1:
    for metric in ["GHI", "DNI", "DHI"]:
        st.subheader(f"{metric} Comparison")
        valid_dfs = {
            country: df for country, df in dfs.items()
            if isinstance(df, pd.DataFrame)
        }
        if valid_dfs:
            fig = plot_boxplot(valid_dfs, metric)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No valid data available to plot.")

with tab2:
    st.subheader("Mean, Median, and Std. Dev")
    valid_dfs = {
        country: df for country, df in dfs.items()
        if isinstance(df, pd.DataFrame)
    }
    if valid_dfs:
        summary_df = plot_summary_table(valid_dfs)
        st.dataframe(summary_df)
    else:
        st.warning("No data available for summary statistics.")

# Display any file-specific errors
for country, df in dfs.items():
    if df is None:
        st.error(f"❌ Data file for {country} not found.")
    elif isinstance(df, str) and df.startswith("Error:"):
        st.error(f"⚠️ Failed to load {country} dataset: {df}")
