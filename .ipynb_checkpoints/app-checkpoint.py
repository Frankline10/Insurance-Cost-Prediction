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

import pandas as pd

if st.button("Predict"):

    import pandas as pd

    # ✅ Step 1: Create RAW input (same as training)
    input_data = pd.DataFrame({
        'age': [age],
        'sex': [1 if sex == "female" else 0],
        'bmi': [bmi],
        'children': [children],
        'smoker': [1 if smoker == "yes" else 0],
        'region': [region]
    })

    # ✅ Step 2: Convert categorical to dummy
    input_data = pd.get_dummies(input_data)

    # ✅ Step 3: Match columns EXACTLY
    for col in model.feature_names_in_:
        if col not in input_data.columns:
            input_data[col] = 0

    input_data = input_data[model.feature_names_in_]

    # 🔍 DEBUG (KEEP THIS)
    st.write("Final Input:", input_data)

    # ✅ Step 4: Predict
    prediction = model.predict(input_data)

    st.success(f"Predicted Cost: {prediction[0]}")