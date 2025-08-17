import streamlit as st
import pandas as pd
import joblib

# ----------------------------
# PAGE FUNCTION
# ----------------------------
def page_live_price_prediction_body():

    st.write("### Live House Price Prediction Tool")
    st.info(
        f"* This tool allows you to predict the sale price for any house in Ames, Iowa.\n"
        f"* Enter the house attributes below and click 'Predict Price' to get an estimate.\n"
        f"* The prediction is based on the trained ML model using historical sales data."
    )

    # Load trained pipeline
    try:
        price_prediction_pipeline = joblib.load(
            "outputs/ml_pipeline/predict_SalePrice/v1/best_regressor_pipeline.pkl"
        )
    except Exception as e:
        st.error(f"Could not load prediction pipeline: {e}")
        return
    
    st.write("---")
    
    # Generate Live Data Input Form
    X_live = draw_input_widgets()

    # Predict on live data
    if st.button("🏠 Predict House Price", type="primary"):
        st.write("### Prediction Results")

        try:
            prediction = make_live_prediction(X_live, price_prediction_pipeline)
            display_prediction_results(X_live, prediction)
        except Exception as e:
            st.error(f"Error making prediction: {e}")


# ----------------------------
# INPUT WIDGETS
# ----------------------------
def draw_input_widgets():
    """
    Create input widgets for house features
    """
    st.write("#### Enter House Details")
    
    X_live = pd.DataFrame([], index=[0])

    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    col7, col8, col9 = st.columns(3)

    with col1:
        X_live["GrLivArea"] = st.number_input(
            "GrLivArea (Ground Living Area sq ft)",
            min_value=500, max_value=5000, value=1500
        )

    with col2:
        X_live["OverallQual"] = st.selectbox(
            "OverallQual (Overall Quality)",
            options=list(range(1, 11)), index=6
        )

    with col3:
        X_live["YearBuilt"] = st.number_input(
            "YearBuilt", min_value=1800, max_value=2024, value=2000
        )

    with col4:
        X_live["GarageCars"] = st.selectbox(
            "GarageCars (Garage Capacity)", options=[0, 1, 2, 3, 4], index=2
        )

    with col5:
        X_live["TotalBsmtSF"] = st.number_input(
            "TotalBsmtSF (Basement Area sq ft)",
            min_value=0, max_value=3000, value=1000
        )

    with col6:
        X_live["FullBath"] = st.selectbox(
            "FullBath (Full Bathrooms)", options=[0, 1, 2, 3, 4], index=2
        )

    with col7:
        X_live["Neighborhood"] = st.selectbox(
            "Neighborhood",
            options=["CollgCr", "OldTown", "Edwards", "Somerst", "Gilbert", "NridgHt", "Sawyer", "NWAmes"]
        )

    with col8:
        X_live["KitchenQual"] = st.selectbox(
            "KitchenQual (Kitchen Quality)",
            options=["Po", "Fa", "TA", "Gd", "Ex"], index=2
        )

    with col9:
        X_live["FireplaceQu"] = st.selectbox(
            "FireplaceQu (Fireplace Quality)",
            options=["None", "Po", "Fa", "TA", "Gd", "Ex"], index=0
        )

    if st.checkbox("Show Input Data"):
        st.write("**Current Input Values:**")
        st.dataframe(X_live.T, use_container_width=True)

    return X_live


# ----------------------------
# PREDICTION FUNCTIONS
# ----------------------------
def make_live_prediction(X_live, pipeline):
    """
    Make prediction using the trained pipeline
    """
    prediction = pipeline.predict(X_live)
    return prediction[0]


def display_prediction_results(X_live, prediction):
    """
    Display detailed prediction results
    """
    st.success(f"**Predicted Sale Price: ${prediction:,.0f}**")

    with st.expander("Prediction Details"):
        st.write("**Input Features Used for Prediction:**")
        st.dataframe(X_live.T, use_container_width=True)
        st.write("---")
        st.write("**Note:** Confidence intervals and feature importance are not included here, "
                 "but can be added if needed.")