import streamlit as st

st.set_page_config(page_title="Insurance Predictor", layout="centered")
st.markdown("### Enter Details Below")
st.sidebar.header("User Input Panel")

st.title("Insurance Cost Prediction App")

st.write("Enter user details to predict insurance cost")

age = st.slider("Age", 18, 65, 25)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.slider("BMI", 10.0, 50.0, 25.0)
children = st.slider("Number of Children", 0, 5, 0)
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

import pickle
import pandas as pd

model = pickle.load(open("models/insurance_model.pkl", "rb"))

input_data = pd.DataFrame({
    'age': [age],
    'sex': [1 if sex == "female" else 0],
    'bmi': [bmi],
    'children': [children],
    'smoker': [1 if smoker == "yes" else 0],
    'region_northwest': [1 if region == "northwest" else 0],
    'region_southeast': [1 if region == "southeast" else 0],
    'region_southwest': [1 if region == "southwest" else 0]
})

if st.button("Predict Insurance Cost"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Insurance Cost: {prediction[0]:.2f}")
