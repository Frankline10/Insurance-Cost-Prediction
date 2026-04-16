import streamlit as st
import pandas as pd
import joblib


# Loading the Model

model = joblib.load("models/insurance_model.pkl")


# App Title

st.set_page_config(page_title="Insurance Cost Predictor", layout="centered")

st.title("Insurance Cost Prediction")
st.write("Enter the details below to predict insurance charges")


# User Inputs

age = st.slider("Age", 18, 100, 25)

sex = st.selectbox("Sex", ["male", "female"])

bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)

children = st.slider("Number of Children", 0, 5, 0)

smoker = st.selectbox("Smoker", ["yes", "no"])

region = st.selectbox("Region", ["southwest", "southeast", "northwest", "northeast"])



# Prediction Button

if st.button("Predict Insurance Cost"):
    
    # Creating DataFrame
    
    input_data = pd.DataFrame({
        "age": [age],
        "sex": [sex],
        "bmi": [bmi],
        "children": [children],
        "smoker": [smoker],
        "region": [region]
    })

    
    # Prediction
    prediction = model.predict(input_data)

    
    # Output
    st.success(f"Estimated Insurance Cost: ₹ {round(prediction[0], 2)}")