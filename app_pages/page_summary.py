import streamlit as st
import pandas as pd
# TODO: Replace with actual data loading function
# from src.data_management import load_house_data

def page_summary_body():

    st.write("### Quick Project Summary")

    # Project Terms & Context
    st.info(
        f"**Project Context**\n"
        f"* **Client**: Lydia, who inherited 4 properties in Ames, Iowa from her great-grandfather\n"
        f"* **Goal**: Help maximize the sales price for inherited properties\n"
        f"* **Challenge**: Lydia's property knowledge is from her home state, not Iowa\n"
        f"* **Solution**: Use Ames housing data to understand what drives property values\n\n"
        f"**Dataset**\n"
        f"* The dataset contains **house sales data from Ames, Iowa**\n"
        f"* Features include house attributes like size, quality, condition, garage, kitchen, basement\n"
        f"* **Target variable**: SalePrice - what we want to predict")

    # Link to project documentation
    st.write(
        f"* For additional information, please visit the "
        f"[Project Documentation](https://github.com/Zozo62442/milestone-project-heritage-housing-issues).")
    
    # Business Requirements
    st.success(
        f"The project has 2 main business requirements:\n"
        f"* **BR1** - Discover how house attributes correlate with sale price. "
        f"Provide data visualizations showing relationships between key features and sale price.\n"
        f"* **BR2** - Predict house sale prices for Lydia's 4 inherited houses "
        f"and create a tool to predict prices for any house in Ames, Iowa."
    )

    # Dataset preview
    st.write("### Dataset Overview")
    
    # TODO: Replace this placeholder with actual data loading
    # df = load_house_data()
    # st.write(f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns")
    # st.write("Sample of the first 5 rows:")
    # st.write(df.head())
    
    # PLACEHOLDER - Remove when you have actual data
    st.warning(
        "**PLACEHOLDER**: Dataset overview will be displayed here once data loading is implemented.\n"
        "Will show:\n"
        "- Dataset dimensions (rows x columns)\n"
        "- First 5 rows of the dataset\n"
        "- Brief description of key features"
    )

    # Project Hypotheses
    st.write("### Project Hypotheses")
    st.info(
        f"**Hypothesis 1**: House size, quality, and condition are highly correlated to sale price.\n\n"
        f"**Hypothesis 2**: Garage size, kitchen quality, and basement finish also play a significant role in determining sale price.\n\n"
        f"**Validation Strategy**: Correlation analysis, Predictive Power Score (PPS), visualizations, and feature importance from ML models."
    )