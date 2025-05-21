# app/main.py
import streamlit as st

from utils import load_data, plot_boxplot, plot_summary_table

st.set_page_config(page_title="Solar Dashboard", layout="wide")

st.title("☀️ Solar Energy Insights Dashboard")

# Sidebar: Country selection
selected_countries = st.multiselect(
    "Select Countries",
    ["Benin", "Sierra Leone", "Togo"],
    default=["Benin", "Sierra Leone", "Togo"]
)

# Load data for selected countries
dfs = load_data(selected_countries)

# Tabs for Layout
tab1, tab2 = st.tabs(["📊 Metric Comparison", "📋 Summary Statistics"])

with tab1:
    for metric in ["GHI", "DNI", "DHI"]:
        st.subheader(f"{metric} Comparison")
        fig = plot_boxplot(dfs, metric)
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Mean, Median, and Std. Dev")
    summary_df = plot_summary_table(dfs)
    st.dataframe(summary_df)
