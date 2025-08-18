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

# GrLivArea
    with col1:
        X_live["GrLivArea"] = st.number_input(
            "GrLivArea (Ground Living Area sq ft)",
            min_value=300, max_value=6000, value=1500, step=10
        )

    # TotalBsmtSF
    with col2:
        X_live["TotalBsmtSF"] = st.number_input(
            "TotalBsmtSF (Total Basement Area sq ft)",
            min_value=0, max_value=3000, value=1000, step=10
        )

    # OverallQual
    with col3:
        X_live["OverallQual"] = st.selectbox(
            "OverallQual (Overall Quality, 1=Very Poor, 10=Excellent)",
            options=list(range(1, 11)), index=6
        )

    # GarageArea
    with col4:
        X_live["GarageArea"] = st.number_input(
            "GarageArea (Garage Size sq ft)",
            min_value=0, max_value=1500, value=500, step=10
        )

    # YearBuilt
    with col5:
        X_live["YearBuilt"] = st.number_input(
            "YearBuilt (Year the House was Built)",
            min_value=1800, max_value=2024, value=2000, step=1
        )

    # 1stFlrSF
    with col6:
        X_live["1stFlrSF"] = st.number_input(
            "1stFlrSF (First Floor sq ft)",
            min_value=300, max_value=4000, value=1000, step=10
        )


    if st.checkbox("Show Input Data"):
        st.write("**Current Input Values:**")
        st.dataframe(X_live.T, use_container_width=True)

    return X_live


# ----------------------------
# DEFAULTS + PREDICTION
# ----------------------------
def make_live_prediction(X_live, pipeline):
    """
    Make prediction using trained pipeline,
    filling in missing features with defaults
    """

    # Define defaults here (median/mode from training dataset)
    feature_defaults = {
        "1stFlrSF": 1162.63,
        "2ndFlrSF": 327.99,
        "BedroomAbvGr": 2.88,
        "BsmtExposure": "No",   # categorical - most common
        "BsmtFinSF1": 443.64,
        "BsmtFinType1": "Unf",  # categorical
        "BsmtUnfSF": 567.24,
        "EnclosedPorch": 46.66,
        "GarageArea": 472.98,
        "GarageFinish": "Unf",  # categorical
        "GarageYrBlt": 1978.59,
        "GrLivArea": 1515.46,
        "KitchenQual": "TA",    # categorical
        "LotArea": 10516.83,
        "LotFrontage": 69.86,
        "MasVnrArea": 103.12,
        "OpenPorchSF": 46.66,
        "OverallCond": 5.58,
        "OverallQual": 6.10,
        "TotalBsmtSF": 1057.43,
        "WoodDeckSF": 11.01,
        "YearBuilt": 1971.27,
        "YearRemodAdd": 1984.87,
        "SalePrice": 180921.20  # target, not actually used as input
}

    # Start with defaults
    X_full = pd.DataFrame([feature_defaults])

    # Overwrite with user inputs
    for col in X_live.columns:
        X_full[col] = X_live[col].values[0]

    # Reorder to pipeline expectation
    X_full = X_full[pipeline.feature_names_in_]

    prediction = pipeline.predict(X_full)
    return prediction[0]


def display_prediction_results(X_live, prediction):
    """
    Display detailed prediction results
    """
    st.success(f"**Predicted Sale Price: ${prediction:,.0f}**")

    with st.expander("Prediction Details"):
        st.write("**Key Features Entered:**")
        st.dataframe(X_live.T, use_container_width=True)
        st.write("---")
        st.write("**Note:** Other features were filled with typical values "
                 "from the training dataset to make the prediction.")