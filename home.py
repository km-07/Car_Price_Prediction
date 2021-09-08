"""This module creates the home page."""

# Import necessary modules.
import streamlit as st

def app():
    st.title("Car Prediction Website")
    st.image("./welcome.jpg")
    st.text(
        """
        This web app allows a user to predict the prices of a car based on their 
        engine size, year of manufacturing, seating, mileage and other parameters type parameters.
        """
    )