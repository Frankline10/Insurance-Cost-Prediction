# 🏥 Insurance-Cost-Prediction
Machine Learning Project for predicting insurance costs

---

## 📌 Project Title

**Insurance Cost Prediction using Machine Learning**

---

## 🎯 Problem Statement

The objective of this project is to develop a machine learning model that predicts individual medical insurance costs based on demographic and lifestyle attributes such as age, BMI, smoking status, number of dependents, and region. Accurate prediction of insurance charges helps insurance companies assess risk and design effective pricing strategies.

---

## 📊 Dataset Description

The dataset consists of **1338 records** with **7 features**, including both numerical and categorical variables.

### 🔑 Features:

* **age** → Age of the individual
* **sex** → Gender (male/female)
* **bmi** → Body Mass Index
* **children** → Number of dependents
* **smoker** → Smoking status (yes/no)
* **region** → Residential region
* **charges** → Medical insurance cost (**Target Variable**)

---

## 🔄 Project Workflow (Phases 1–10)

1. **Business Understanding**
   Defined the problem and business objectives.

2. **Data Understanding**
   Explored dataset structure, data types, and statistical properties.

3. **Exploratory Data Analysis (EDA)**
   Analyzed distributions and relationships to identify key patterns and trends.

4. **Data Preprocessing**
   Handled encoding, duplicates, and prepared data for modeling.

5. **Feature Engineering**
   Created new features such as BMI category, age group, and risk level.

6. **Model Building**
   Trained multiple machine learning models.

7. **Model Evaluation**
   Evaluated models using MAE, RMSE, and R² score.

8. **Model Selection**
   Selected the best-performing model based on evaluation metrics.

9. **Business Insights**
   Derived meaningful insights to support business decisions.

10. **Model Saving & Finalization**
    Saved the final model for future predictions.

---

## 🤖 Models Used

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* XGBoost Regressor (optional)

---

## 🏆 Best Model

**Random Forest Regressor**

* Selected due to its ability to capture non-linear relationships
* Provided highest accuracy and lowest error among all models

---

## 📈 Results / Accuracy

* **R² Score:** ~0.85 – 0.88 (depending on preprocessing & tuning)
* **RMSE:** Lower compared to other models
* **MAE:** Minimum among all models

👉 The model demonstrated strong predictive performance and generalization capability.

---

## 📊 Key Insights

* Smoking is the most significant factor affecting insurance charges
* BMI and age have strong positive correlation with costs
* High-risk individuals (smokers with high BMI) incur the highest expenses
* Region has minimal impact on insurance pricing

---

## 🧾 Conclusion

A robust machine learning model was successfully developed to predict insurance costs. Random Forest emerged as the best-performing model due to its ability to handle complex relationships. The project also provided valuable business insights that can help insurance companies optimize pricing strategies and improve risk assessment.

---

## 🚀 Future Improvements

* Hyperparameter tuning for improved accuracy
* Deployment using Streamlit or Flask
* Integration with real-time user input
* Use of advanced models like Gradient Boosting
* Incorporation of additional features (medical history, lifestyle habits)

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* Jupyter Notebook

---

## 📌 Author

**Soujanya Prokash Singha**

---

⭐ If you found this project useful, feel free to give it a star!
