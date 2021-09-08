"""This module helps to preprocess the data."""

# Import necessary modules.
import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder

# Load the dataset.
@st.cache()
def load_data():
    """This function perform preprocessing on dataset and return that"""
    # read the dataset.
    df = pd.read_csv("D:\Template\Car details v3.csv")

#dropping null values
    df.dropna(axis=0, inplace=True)

#modifying name by splitting
    new_list = []
    for i in list(df['name']):
        name = i.split()[0]
        new_list.append(name)

    car_series = pd.Series(new_list)
    df['name'] = car_series

    #modifying max_power by splitting
    new_list = []
    for i in list(df['max_power']):
        name = i.split()[0]
        new_list.append(name)

    car_series = pd.Series(new_list)
    df['max_power'] = car_series

    #modifying engine by splitting
    new_list = []
    for i in list(df['engine']):
        name = i.split()[0]
        new_list.append(name)

    car_series = pd.Series(new_list)
    df['engine'] = car_series

    #modifying mileage by splitting
    new_list = []
    for i in list(df['mileage']):
        name = i.split()[0]
        new_list.append(name)

    car_series = pd.Series(new_list)
    df['mileage'] = car_series

    #dropping torque
    df.drop(['torque'], axis=1, inplace=True)

    #dropping newly created null values
    df.dropna(axis=0, inplace=True)

    #creating label encoder
    label_encoder = LabelEncoder()

    #label_encding columns
    df['fuel']= label_encoder.fit_transform(df['fuel'])
    df['fuel'].unique()

    df['seller_type']= label_encoder.fit_transform(df['seller_type'])
    df['seller_type'].unique()

    df['transmission']= label_encoder.fit_transform(df['transmission'])
    df['transmission'].unique()

    df['owner']= label_encoder.fit_transform(df['owner'])
    df['owner'].unique()

    df['name']= label_encoder.fit_transform(df['name'])
    df['name'].unique()

    df[["mileage", "engine", "max_power"]] = df[["mileage", "engine", "max_power"]].apply(pd.to_numeric)

    return df
