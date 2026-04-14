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

    # Step 1: Feature Engineering (SAME as training)

    # Age group
    if age < 30:
        age_group = "Young"
    elif age < 50:
        age_group = "Adult"
    else:
        age_group = "Senior"

    # BMI category
    if bmi < 18.5:
        bmi_category = "Underweight"
    elif bmi < 25:
        bmi_category = "Normal"
    elif bmi < 30:
        bmi_category = "Overweight"
    else:
        bmi_category = "Obese"

    # Step 2: Create DataFrame
    input_data = pd.DataFrame({
        'sex': [1 if sex == "female" else 0],
        'children': [children],
        'smoker': [1 if smoker == "yes" else 0],
        'region_northwest': [1 if region == "northwest" else 0],
        'region_southeast': [1 if region == "southeast" else 0],
        'region_southwest': [1 if region == "southwest" else 0],
        'age_group': [age_group],
        'bmi_category': [bmi_category]
    })

    # Step 3: Convert engineered categories to dummy
    input_data = pd.get_dummies(input_data)

    # Step 4: Match training columns
    for col in model.feature_names_in_:
        if col not in input_data.columns:
            input_data[col] = 0

    input_data = input_data[model.feature_names_in_]

    # Step 5: Predict
    prediction = model.predict(input_data)

    st.success(f"Predicted Cost: {prediction[0]}")