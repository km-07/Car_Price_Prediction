"""This module creates the web page"""

# Import necessary modules.
import streamlit as st

# Import pages.
import home
import predict
import about

# Import other necessary things.
from prepro import load_data

# Configure the web page.
st.set_page_config(
    page_title = 'Car Price Prediction',
    page_icon = 'car',
    layout = 'centered',
    initial_sidebar_state = 'auto'
)


# Load the dataset.
df = load_data()

# Create navbar in sidebar.
st.sidebar.title("Navigation")
user_choice = st.sidebar.radio('Go to', ("Home", "Predict", "About me"))

# Open the page selected by the user.
if (user_choice == "Home"): 
    home.app()
elif (user_choice == "About me"):
    about.app()
else:
    predict.app(df)
