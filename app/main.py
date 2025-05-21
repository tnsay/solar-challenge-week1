import streamlit as st
import pandas as pd
import os
import glob
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Solar Potential Dashboard")

# Dropdown for countries
country_files = {
    "Benin": "notebooks/data/benin_clean.csv",
    "Sierra Leone": "notebooks/data/sierra_leone_clean.csv",
    "Togo": "notebooks/data/togo_clean.csv"
}

selected_countries = st.multiselect(
    "Select countries to include:",
    options=list(country_files.keys()),
    default=list(country_files.keys())
)

# Load and concatenate selected data
dfs = []
for country in selected_countries:
    file_path = country_files[country]
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df["Country"] = country  
        dfs.append(df)

if dfs:
    df = pd.concat(dfs, ignore_index=True)

    st.write("### Raw Data Preview")
    st.dataframe(df.head())

    
    st.write("### GHI Distribution by Country")
    sns.boxplot(x="Country", y="GHI", data=df)
    st.pyplot(plt.gcf())
    plt.clf()

    # Summary Table
    st.write("### Summary Statistics")
    summary = df.groupby("Country")[["GHI", "DNI", "DHI"]].agg(["mean", "median", "std"]).round(2)
    st.dataframe(summary)

    # Top 10 Regions
    st.write("### Top 10 Records by Average GHI (Simulated - No Region Info)")
    top_records = df.sort_values(by="GHI", ascending=False).head(10)
    st.dataframe(top_records[["Country", "GHI"]])
else:
    st.warning("Please select at least one country with available data.")