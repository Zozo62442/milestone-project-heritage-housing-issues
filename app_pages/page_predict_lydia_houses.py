import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

def page_predict_lydia_houses_body():

    st.write("### Predict Lydia's Inherited Houses")
    
    st.info(
        f"* This page shows the predicted sale prices for Lydia's 4 inherited houses.\n"
        f"* The predictions are based on the trained ML model using house attributes.\n"
        f"* The total predicted value helps Lydia understand the potential worth of her inheritance."
    )

    # Load data + model
    try:
        lydia_houses = pd.read_csv("outputs/datasets/collection/inherited_houses.csv")
        price_prediction_pipeline = joblib.load(
            "outputs/ml_pipeline/predict_SalePrice/v1/best_regressor_pipeline.pkl"
        )
    except Exception as e:
        st.error(f"Error loading data or model: {e}")
        return

    # Predict prices
    try:
        predictions = price_prediction_pipeline.predict(lydia_houses)
        lydia_houses["Predicted_Price"] = predictions
    except Exception as e:
        st.error(f"Error making predictions: {e}")
        return

    # Show houses table
    st.write("### Lydia's Inherited Houses")
    st.dataframe(lydia_houses, use_container_width=True)

    # Expanders for individual house details
    if st.checkbox("Show Detailed House Information"):
        for i, row in lydia_houses.iterrows():
            with st.expander(f"House {i+1} Details"):
                col1, col2 = st.columns(2)

                with col1:
                    st.write("**House Attributes:**")
                    st.write(row.drop("Predicted_Price").to_frame().T)

                with col2:
                    st.write("**Prediction Result:**")
                    st.success(f"Predicted Price: ${row['Predicted_Price']:,.0f}")

    # Summary
    st.write("---")
    st.write("### Summary of All House Predictions")

    # Show summary table (with selected key features + predicted price)
    key_cols = ["GrLivArea", "OverallQual", "YearBuilt", "Predicted_Price"]
    summary_df = lydia_houses[key_cols]
    st.dataframe(summary_df, use_container_width=True)

    # Total portfolio value
    total_value = lydia_houses["Predicted_Price"].sum()
    st.write("#### Total Portfolio Value")
    st.success(f"**Total Predicted Value of All 4 Houses: ${total_value:,.0f}**")

    # --- NEW BAR CHART ---
    st.write("#### Visual Comparison of Predicted Prices")
    fig = px.bar(
        lydia_houses.reset_index(),
        x=lydia_houses.index + 1,
        y="Predicted_Price",
        text="Predicted_Price",
        labels={"x": "House", "Predicted_Price": "Predicted Sale Price"},
        title="Predicted Prices for Lydia's Inherited Houses"
    )
    fig.update_traces(texttemplate="$%{text:,.0f}", textposition="outside")
    fig.update_layout(xaxis_title="House Number", yaxis_title="Predicted Price ($)")
    st.plotly_chart(fig, use_container_width=True)

    # Recommendations (can later replace with data-driven rules)
    st.info(
        f"**Recommendations for Lydia:**\n"
        f"* Consider prioritizing houses with higher predicted values when selling.\n"
        f"* Explore cost-effective renovations (e.g., kitchen, bathrooms) in lower-valued houses.\n"
        f"* Compare predicted values with recent Ames market trends before making final decisions."
    )

    # Notes
    st.write("---")
    st.write("### Prediction Confidence and Limitations")
    st.warning(
        "**Important Notes:**\n"
        "* Predictions are based on historical Ames housing data.\n"
        "* Model performance metrics are available on the Model Performance page.\n"
        "* Market conditions and unique house features may affect actual sale prices.\n"
        "* Professional appraisals are recommended before final selling decisions."
    )
