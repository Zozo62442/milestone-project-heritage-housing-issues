import streamlit as st
import pandas as pd

# Data loading function
@st.cache_data
def load_house_data():
    """Load cleaned Ames Housing dataset."""
    df = pd.read_csv("outputs/datasets/cleaned/house_prices_cleaned.csv")  
    return df

def page_summary_body():
    st.write("## 🏡 Project Summary")

    # Project Terms & Context
    st.info(
        "**Project Context**\n"
        "- **Client**: Lydia, who inherited 4 properties in Ames, Iowa from her great-grandfather.\n"
        "- **Goal**: Help maximize the sales price for inherited properties.\n"
        "- **Challenge**: Lydia's property knowledge is from her home state, not Iowa.\n"
        "- **Solution**: Use Ames housing data to understand what drives property values.\n\n"
        "**Dataset**\n"
        "- Contains **house sales data from Ames, Iowa**.\n"
        "- Features: house attributes like size, quality, condition, garage, kitchen, basement.\n"
        "- **Target variable**: `SalePrice` (the selling price of each property)."
    )

    # Link to project documentation
    st.markdown(
        "* For additional information, please visit the "
        "[Project Documentation](https://github.com/Zozo62442/milestone-project-heritage-housing-issues)."
    )
    
    # Business Requirements
    st.success(
        "**Business Requirements**\n"
        "- **BR1**: Discover how house attributes correlate with sale price. Provide data visualizations showing relationships between key features and sale price.\n"
        "- **BR2**: Predict house sale prices for Lydia's 4 inherited houses and create a tool to predict prices for any house in Ames, Iowa."
    )

    # Dataset preview
    st.write("### 📊 Dataset Overview")
    df = load_house_data()
    st.write(f"* The dataset has **{df.shape[0]} rows** and **{df.shape[1]} columns**.")
    st.write("##### First 5 rows of the dataset:")
    st.dataframe(df.head())

    # Key variables overview
    st.write("##### Key Variables")
    st.markdown(
        "- **OverallQual**: Overall material and finish quality\n"
        "- **GrLivArea**: Above ground living area (sq ft)\n"
        "- **GarageCars**: Garage size in car capacity\n"
        "- **KitchenQual**: Kitchen quality rating\n"
        "- **TotalBsmtSF**: Total basement area (sq ft)\n"
        "- **SalePrice**: Target variable we want to predict"
    )

    # Project Hypotheses
    st.write("### 🔎 Project Hypotheses")
    st.info(
        "**Hypothesis 1**: House size, quality, and condition are highly correlated to sale price.\n\n"
        "**Hypothesis 2**: Garage size, kitchen quality, and basement finish also play a significant role in determining sale price.\n\n"
        "**Validation Strategy**: Correlation analysis, Predictive Power Score (PPS), visualizations, and feature importance from ML models."
    )