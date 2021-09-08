"""This create prediction page"""

# Import necessary module
import streamlit as st
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
import pandas as pd

def app(df):
    # Use markdown to give title
    st.markdown("<p style='color:red; font-size: 30px'>This app uses <b>XG boost regression</b> to predict the price of a car based on your inputs.</p>", unsafe_allow_html=True)

    #creating dictionaries
    brand_d = {"Maruti":20, "Hyundai":26, "Mahindra":10, "Tata":11, "Honda":28, "Toyota":9, "Ford":25, "Chevrolet":19, "Renault":27, "Volkswagen":4, "BMW":6, "Skoda":14, "Nissan":21, "Jaguar":22, "Volvo":2, "Datsun":29, "Mercedes-Benz":3, "Fiat":23, "Audi":17, "Lexus":13, "Jeep":16, "Mitsubishi":18, "Land":30, "Force":5, "Isuzu":15, "Kia":7, "Ambassador":8, "Daewoo":0, "MG":1, "Opel":12, "Ashok":24}

    fuel_d = {"Diesel":1, "Petrol":3, "CNG":2, "LPG":0}

    seller_type_d = {"Individual":1, "Dealer":0, "Trustmark Dealer":2}

    trans_d = {"Manual":1, "Automatic":0}

    owner_d = {"First Owner":0, "Second Owner":2, "Third Owner":4, "Fourth & Above Owner":1, "Test Drive Car":3}



    # Create a section for user to input data.
    st.header("Select Values:")

    #To select parameters.
    brand = st.selectbox("Brand", ["Maruti", "Hyundai", "Mahindra", "Tata", "Honda", "Toyota", "Ford", "Chevrolet", "Renault", "Volkswagen", "BMW", "Skoda", "Nissan", "Jaguar", "Volvo", "Datsun", "Mercedes-Benz", "Fiat", "Audi", "Lexus", "Jeep", "Mitsubishi", "Land", "Force", "Isuzu", "Kia", "Ambassador", "Daewoo", "MG", "Opel", "Ashok"])

    year = st.slider("Year", 1994, 2020)

    km = st.slider("KM Driven", 0, 250000, 1000)

    fuel = st.selectbox("Fuel Type", ["Diesel", "Petrol", "CNG", "LPG"])

    seller_type = st.selectbox("Seller Type", ["Individual", "Dealer", "Trustmark Dealer"])

    trans = st.radio("Transmission", ["Manual", "Automatic"])

    owner = st.selectbox("Owner", ["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner", "Test Drive Car"])

    mileage = st.slider("Mileage", 0.0, 50.0)

    engine = st.slider("Engine in CC", 600, 3700)

    maxp = st.slider("Max Power in bhp", 30.0, 400.0)

    seats = st.slider("No. of Seats", 2, 14)


    features = [[brand_d[brand], year, km, fuel_d[fuel], seller_type_d[seller_type], trans_d[trans], owner_d[owner], mileage, engine, maxp, seats]]

    f = pd.DataFrame(features)

    

    if st.button("Predict"):
       y = df["selling_price"]

       X = df.drop("selling_price", axis=1)

       model = XGBRegressor(max_depth=4 ,n_estimators=800, booster="gbtree", learning_rate=0.03)
       model.fit(X, y)

       pred_price = model.predict(f)
       pred_price = pred_price[0]
        
       st.warn("This will take 10 to 15 seconds to get you the predictions. KINDLY HOLD ON")

       st.success(f"The predicted price of the car: Rs.{int(pred_price):,}")



