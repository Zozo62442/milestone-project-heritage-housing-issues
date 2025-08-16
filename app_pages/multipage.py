import streamlit as st

# Configure the main app settings (only once, at the start)
st.set_page_config(
    page_title="Ames Housing Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# Class to handle multiple Streamlit pages
class MultiPage:

    def __init__(self, app_name: str) -> None:
        self.pages = []
        self.app_name = app_name

    def add_page(self, title: str, func) -> None:
        """Add a new page to the app"""
        self.pages.append({"title": title, "function": func})

    def run(self):
        """Run the selected page"""
        st.title(self.app_name)
        page = st.sidebar.radio(
            '📑 Navigation',
            self.pages,
            format_func=lambda page: page['title']
        )
        page['function']()