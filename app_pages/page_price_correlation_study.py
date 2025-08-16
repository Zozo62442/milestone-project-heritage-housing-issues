import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

sns.set_style("whitegrid")

# Load the cleaned dataset
@st.cache_data
def load_clean_data():
    return pd.read_csv("outputs/datasets/cleaned/house_prices_cleaned.csv")

def page_price_correlation_study_body():
    df = load_clean_data()
    target_var = "SalePrice"

    # ---- MANUAL top variables (from your EDA notebook) ----
    vars_to_study = ['OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'YearBuilt']

    st.write("## House Price Correlation Study")
    st.info(
        f"Lydia is interested in understanding which house attributes most strongly "
        f"affect the sale price in Ames, Iowa, so she can focus on the most valuable "
        f"features when selling her inherited properties."
    )

    # Inspect data
    if st.checkbox("Inspect House Sales Dataset"):
        st.write(f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns")
        st.write("First 10 rows:")
        st.write(df.head(10))
        st.write("Basic statistics:")
        st.write(df.describe())

    st.write("---")

    # Correlation Study Summary (MANUAL explanation)
    st.write("### Correlation Study Results")
    st.write(
        f"The most correlated variables to SalePrice are: "
        f"**OverallQual, GrLivArea, GarageCars, TotalBsmtSF, YearBuilt**"
    )

    st.info(
        f"**Key Insights from Correlation Analysis:**\n"
        f"* **OverallQual** (overall material and finish quality) is the strongest driver of price.\n"
        f"* **GrLivArea** (above ground living area) is highly correlated with price — bigger homes tend to be more expensive.\n"
        f"* **GarageCars** and **TotalBsmtSF** show strong positive relationships with price.\n"
        f"* **YearBuilt** shows that newer homes are generally valued higher."
    )

    # Individual plots per variable
    if st.checkbox("Sale Price vs Key Variables"):
        price_correlation_per_variable(df, vars_to_study, target_var)

    # Correlation Matrix (optional broader view)
    if st.checkbox("Correlation Matrix Heatmap"):
        plot_correlation_matrix(df)

    # PPS (optional, leave as enhancement)
    if st.checkbox("Predictive Power Score (PPS) Analysis"):
        plot_pps_analysis(df)


# ---------- Helper plotting functions ----------

def price_correlation_per_variable(df, vars_to_study, target_var):
    """Create individual plots for each variable vs SalePrice"""
    for col in vars_to_study:
        if df[col].dtype in ['object', 'category']:
            plot_categorical_vs_price(df, col, target_var)
        else:
            plot_numerical_vs_price(df, col, target_var)


def plot_categorical_vs_price(df, col, target_var):
    """Box plot for categorical variable vs SalePrice"""
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.boxplot(data=df, x=col, y=target_var, ax=ax)
    plt.xticks(rotation=45)
    ax.set_title(f"{col} vs {target_var}")
    st.pyplot(fig)


def plot_numerical_vs_price(df, col, target_var):
    """Scatter plot for numerical variable vs SalePrice"""
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=df[col], y=df[target_var], alpha=0.6, ax=ax)
    ax.set_xlabel(col)
    ax.set_ylabel(target_var)
    ax.set_title(f"{col} vs {target_var}")

    # Add correlation coefficient
    corr = df[col].corr(df[target_var])
    ax.text(0.05, 0.95, f'Correlation: {corr:.3f}', 
            transform=ax.transAxes, fontsize=12,
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    st.pyplot(fig)


def plot_correlation_matrix(df):
    """Correlation matrix heatmap"""
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    corr_matrix = df[numerical_cols].corr()

    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(corr_matrix, annot=False, cmap='coolwarm', center=0,
                square=True, cbar_kws={'shrink': 0.8})
    ax.set_title('Feature Correlation Matrix')
    st.pyplot(fig)


def plot_pps_analysis(df):
    """Predictive Power Score analysis"""
    try:
        import ppscore as pps
        pps_matrix = pps.matrix(df)
        fig = px.imshow(
            pps_matrix.pivot("x", "y", "ppscore"),
            color_continuous_scale="Blues",
            title="Predictive Power Score Matrix"
        )
        st.plotly_chart(fig)
    except ImportError:
        st.error("ppscore library not installed. Run `pip install ppscore` to use PPS analysis.")