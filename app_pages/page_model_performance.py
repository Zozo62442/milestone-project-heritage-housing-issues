import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np

def page_model_performance_body():

    st.write("### Model Performance Evaluation")
    st.info(
        f"This page explains how well the ML model predicts house prices in Ames, Iowa.\n"
        f"Lydia can use this information to trust the predictions on her inherited houses."
    )

    # Load model and test data
    try:
        model = joblib.load("outputs/ml_pipeline/predict_SalePrice/v1/best_regressor_pipeline.pkl")
        test_data = pd.read_csv("outputs/datasets/cleaned/house_prices_cleaned.csv")
    except Exception as e:
        st.error(f"Error loading model or data: {e}")
        return

    # Separate features and target
    X = test_data.drop("SalePrice", axis=1)
    y = test_data["SalePrice"]

    # Predict
    y_pred = model.predict(X)

    # --- Metrics ---
    r2 = r2_score(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    mae = mean_absolute_error(y, y_pred)

    st.write("### Performance Metrics")
    st.success(
        f"**R² Score:** {r2:.3f}\n\n"
        f"**RMSE:** ${rmse:,.0f}\n\n"
        f"**MAE:** ${mae:,.0f}"
    )

    st.write("---")

    # --- Predicted vs Actual Scatterplot ---
    st.write("#### Predicted vs Actual Sale Prices")
    fig, ax = plt.subplots(figsize=(8,6))
    sns.scatterplot(x=y, y=y_pred, alpha=0.6)
    plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
    plt.xlabel("Actual Sale Price")
    plt.ylabel("Predicted Sale Price")
    plt.title("Predicted vs Actual Prices")
    st.pyplot(fig)

    # --- Residuals ---
    st.write("#### Residuals Distribution")
    residuals = y - y_pred
    fig, ax = plt.subplots(figsize=(8,6))
    sns.histplot(residuals, bins=40, kde=True, color="blue")
    plt.xlabel("Residual (Actual - Predicted)")
    plt.title("Residuals Distribution")
    st.pyplot(fig)

    # Notes
    st.info(
        "**Interpretation:**\n"
        "* An R² close to 1 means the model explains most of the price variation.\n"
        "* Low RMSE and MAE mean predictions are usually close to actual prices.\n"
        "* The scatterplot should align along the red diagonal line.\n"
        "* Residuals should be centered around zero without big skew."
    )
