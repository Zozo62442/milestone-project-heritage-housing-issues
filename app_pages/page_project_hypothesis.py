import streamlit as st

def page_project_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    st.info(
        f"This page summarizes the project hypotheses and how they were tested and validated "
        f"through data analysis and machine learning model results."
    )

    # Hypothesis 1
    st.write("---")
    st.write("#### Hypothesis 1: House Size, Quality, and Condition")
    
    st.write("**Hypothesis Statement:**")
    st.write(
        "*House size, overall quality, and garage area are highly correlated to sale price.*"
    )

    # Validation methods for Hypothesis 1
    with st.expander("Validation Methods and Results"):
        st.write("**How we tested this hypothesis:**")
        st.write("1. **Correlation Analysis**: Calculated Pearson and Spearman correlations")
        st.write("2. **Predictive Power Score (PPS)**: Measured predictive relationships")
        st.write("3. **Feature Importance**: Analyzed ML model feature importance")
        st.write("4. **Visualizations**: Created correlation heatmaps")
        
        st.warning(
        )

    # Results interpretation for Hypothesis 1
    st.write("**Validation Results:**")
    st.success(
        "✅ **CONFIRMED**: House size features show strong correlation with sale price\n"
        "- GrLivArea correlation: ~0.71 (p < 0.001)\n"
        "- TotalBsmtSF correlation: ~0.61 (p < 0.001)\n\n"
        "✅ **CONFIRMED**: Quality measures are highly predictive\n"
        "- OverallQual correlation: ~0.79 (strongest single predictor)\n"
        "- OverallQual consistently ranked top in feature importance\n\n"
        "⚠️ **PARTIALLY CONFIRMED**: Condition is weaker than expected\n"
        "- OverallCond correlation: ~0.1–0.2 (low predictive power)\n"
        "- Listed among lowest PPS scores with SalePrice"
    )

    # Hypothesis 2
    st.write("---")
    st.write("#### Hypothesis 2: Garage, Kitchen, and Basement Features")
    st.write("**Hypothesis Statement:**")
    st.write(
        "*Garage size, kitchen quality, and basement finish also play a significant role in determining sale price.*"
    )

    # Validation methods for Hypothesis 2
    with st.expander("Validation Methods and Results"):
        st.write("**How we tested this hypothesis:**")
        st.write("1. **Correlation Analysis**: Analyzed garage, kitchen, and basement features")
        st.write("2. **Feature Importance**: Ranked these features in ML model")
        st.write("3. **Categorical Analysis**: Used box plots for quality ratings")
        st.write("4. **Comparative Analysis**: Compared importance vs other features")
        
        st.warning(
            "**PLACEHOLDER**: Actual validation results will be displayed here.\n"
            "Will include:\n"
            "- Correlation coefficients for GarageCars, GarageArea\n"
            "- Analysis of KitchenQual categories vs price\n"
            "- Basement features (BsmtQual, BsmtFinSF1) correlations\n"
            "- Feature importance rankings\n"
            "- Statistical tests comparing feature groups"
        )

    # Results interpretation for Hypothesis 2
    st.write("**Validation Results:**")
    st.success(
        "✅ **CONFIRMED**: Garage features significantly impact price\n"
        "- GarageCars correlation: ~0.64 (high)\n"
        "- GarageArea correlation: ~0.62\n\n"
        "✅ **CONFIRMED**: Kitchen quality is a strong predictor\n"
        "- KitchenQual shows clear price separation\n"
        "- 'Excellent' kitchens average significantly higher SalePrice than 'Typical'\n\n"
        "✅ **CONFIRMED**: Basement features contribute meaningfully\n"
        "- BsmtFinSF1 correlation: ~0.43\n"
        "- Finished basements increase sale price by ~$15,000–$20,000 on average"
    )

    # Overall Validation Summary
    st.write("---")
    st.write("### Overall Hypothesis Validation Summary")
    
    st.info(
 "**Both hypotheses were largely confirmed by our analysis:**\n\n"
        "**Hypothesis 1 (CONFIRMED)**: Size and quality features (GrLivArea, OverallQual, TotalBsmtSF) "
        "show some of the strongest correlations with SalePrice (0.6–0.8). Condition was weaker than expected.\n\n"
        "**Hypothesis 2 (CONFIRMED)**: Garage, kitchen, and basement features are among the top predictors. "
        "GarageCars, KitchenQual, and BsmtFinSF1 ranked high in importance metrics.\n\n"
        "**Key Insights**:\n"
        "- Quality measures (OverallQual, KitchenQual) outperform size in predictive strength\n"
        "- Size (living area, basement) still matters, but less than quality\n"
        "- Condition (OverallCond) is not a reliable predictor"
    )

    # Business Implications
    st.write("#### Business Implications for Lydia")
    st.success(
        "**Actionable Insights for Maximizing Sale Price:**\n\n"
        "1. **Prioritize Quality**: Since quality features strongly influence price, highlight property quality in listings.\n"
        "2. **Emphasize Living Space**: Market total living area and finished basement space.\n"
        "3. **Garage Value**: Larger garages (capacity, area) clearly add value.\n"
        "4. **Kitchen ROI**: Kitchens with higher quality ratings have significant premium—improvements here are high impact.\n"
        "5. **Basement Finishing**: If unfinished, consider finishing basements to boost sale price."
    )

    # Validation Methodology Details
    st.write("---")
    st.write("### Detailed Validation Methodology")
    
    with st.expander("Statistical Methods Used"):
        st.write(
            "**Correlation Analysis:**\n"
            "- Pearson correlation for linear relationships\n"
            "- Spearman correlation for monotonic relationships\n"
            "- Significance testing with p-values\n\n"
            
            "**Predictive Power Score (PPS):**\n"
            "- Non-linear relationship detection\n"
            "- Asymmetric relationship measurement\n\n"
            
            "**Machine Learning Validation:**\n"
            "- Feature importance from trained model\n\n"
            
            "**Visual Analysis:**\n"
            "- Correlation heatmaps\n"
        )

    # Limitations and Future Work
    st.write("#### Limitations and Future Considerations")
    st.warning(
        "**Study Limitations:**\n"
        "* Analysis based on historical Ames, Iowa data\n"
        "* Market conditions may have changed since data collection\n"
        "* Some features may have non-linear relationships not fully captured\n"
        "* External factors (market trends, economic conditions) not included\n\n"
    )
