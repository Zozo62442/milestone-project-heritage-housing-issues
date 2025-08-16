"""
Main Streamlit application for House Price Prediction Dashboard
Helps Lydia maximize the sales price for her inherited properties in Ames, Iowa
"""

import streamlit as st
from multipage import MultiPage

# Import page functions
from page_summary import page_summary_body
from page_price_correlation_study import page_price_correlation_study_body
from page_predict_lydia_houses import page_predict_lydia_houses_body
from page_live_price_prediction import page_live_price_prediction_body
from page_model_performance import page_model_performance_body
from page_project_hypothesis import page_project_hypothesis_body

# Create multipage app
app = MultiPage(app_name="House Price Predictor - Ames, Iowa")

# List of pages to add
pages = [
    ("Project Summary", page_summary_body),
    ("Price Correlation Study", page_price_correlation_study_body),
    ("Predict Lydia's Houses", page_predict_lydia_houses_body),
    ("Live Price Prediction Tool", page_live_price_prediction_body),
    ("Model Performance", page_model_performance_body),
    ("Project Hypothesis & Validation", page_project_hypothesis_body),
]

# Register all pages
for title, func in pages:
    app.add_page(title, func)

# Run the app
app.run()