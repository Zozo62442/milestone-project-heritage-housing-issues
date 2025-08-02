import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
# TODO: Replace with actual data loading function
# from src.data_management import load_house_data

sns.set_style("whitegrid")

def page_price_correlation_study_body():

    # TODO: Replace with actual data loading
    # df_main = inputs/datasets/raw
    
    # PLACEHOLDER - Replace with your actual most correlated variables from analysis
    # 02 - EDA.ipynb notebook!!!
    vars_to_study = ['GrLivArea', 'OverallQual', 'YearBuilt', 'GarageCars', 'TotalBsmtSF']
    
    st.write("### House Price Correlation Study")
    st.info(
        f"* Lydia is interested in understanding which house attributes most strongly "
        f"affect the sale price in Ames, Iowa, so she can focus on the most valuable "
        f"features when selling her inherited properties.")

    # Inspect data
    if st.checkbox("Inspect House Sales Dataset"):
        # TODO: Replace with actual data
        st.warning(
            "**PLACEHOLDER**: Dataset inspection will be displayed here.\n"
            "Will show:\n"
            "- Dataset dimensions\n"
            "- First 10 rows of data\n"
            "- Basic statistics"
        )
        # st.write(f"* The dataset has {df_main.shape[0]} rows and {df_main.shape[1]} columns")
        # st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write("### Correlation Study Results")
    st.write(
        f"* A comprehensive correlation study was conducted to understand how "
        f"various house attributes relate to sale price.\n"
        f"* The most correlated variables to SalePrice are: **{top_vars}**"
    )

    # TODO: Replace with actual insights from your correlation analysis
    st.info(
        f"**Key Insights from Correlation Analysis:**\n"
        f"* **PLACEHOLDER - Replace with actual findings from your analysis**\n"
    )

    # Individual plots per variable
    if st.checkbox("Sale Price vs Key Variables"):
        st.warning(
            "**PLACEHOLDER**: Variable correlation plots will be displayed here.\n"
            "Will include:\n"
            "- Scatter plots for numerical variables vs SalePrice\n"
            "- Box plots for categorical variables vs SalePrice\n"
            "- Correlation values displayed on each plot"
        )
        # TODO: Put actual plotting function
        # price_correlation_per_variable(df, vars_to_study)

    # Correlation Matrix
    if st.checkbox("Correlation Matrix Heatmap"):
        st.warning(
            "**PLACEHOLDER**: Correlation matrix heatmap will be displayed here.\n"
            "Will show:\n"
            "- Heatmap of correlations between all numerical variables\n"
            "- Focus on correlations with SalePrice\n"
            "- Color-coded correlation strengths"
        )
        # TODO: Implement correlation matrix visualization
        # plot_correlation_matrix(df)

    # Predictive Power Score
    if st.checkbox("Predictive Power Score (PPS) Analysis"):
        st.warning(
            "**PLACEHOLDER**: PPS analysis will be displayed here.\n"
            "Will show:\n"
            "- PPS matrix showing predictive relationships\n"
            "- Variables ranked by their predictive power for SalePrice\n"
            "- Comparison between PPS and Pearson correlation"
        )
        # TODO: Implement PPS analysis
        # plot_pps_analysis(df)


# TODO: Implement these functions based on analysis still to be finished
def price_correlation_per_variable(df, vars_to_study):
    """
    Create individual plots for each variable vs SalePrice
    """
    target_var = 'SalePrice'
    
    for col in vars_to_study:
        if df[col].dtype in ['object', 'category']:
            plot_categorical_vs_price(df, col, target_var)
        else:
            plot_numerical_vs_price(df, col, target_var)


def plot_categorical_vs_price(df, col, target_var):
    """
    Create box plot for categorical variable vs SalePrice
    """
    fig, axes = plt.subplots(figsize=(12, 5))
    sns.boxplot(data=df, x=col, y=target_var)
    plt.xticks(rotation=45)
    plt.title(f"{col} vs {target_var}", fontsize=16, y=1.05)
    st.pyplot(fig)


def plot_numerical_vs_price(df, col, target_var):
    """
    Create scatter plot for numerical variable vs SalePrice
    """
    fig, axes = plt.subplots(figsize=(10, 6))
    plt.scatter(df[col], df[target_var], alpha=0.6)
    plt.xlabel(col)
    plt.ylabel(target_var)
    plt.title(f"{col} vs {target_var}", fontsize=16)
    
    # Add correlation coefficient to plot
    corr = df[col].corr(df[target_var])
    plt.text(0.05, 0.95, f'Correlation: {corr:.3f}', 
             transform=axes.transAxes, fontsize=12,
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    st.pyplot(fig)


def plot_correlation_matrix(df):
    """
    Create correlation matrix heatmap
    """
    # Select only numerical columns
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    corr_matrix = df[numerical_cols].corr()
    
    fig, axes = plt.subplots(figsize=(12, 10))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
                square=True, fmt='.2f')
    plt.title('Feature Correlation Matrix', fontsize=16)
    st.pyplot(fig)


def plot_pps_analysis(df):
    """
    Create Predictive Power Score analysis
    """
    # TODO: Implement PPS analysis using ppscore library
    # import ppscore as pps
    # pps_matrix = pps.matrix(df)
    # ... visualization code ...
    pass