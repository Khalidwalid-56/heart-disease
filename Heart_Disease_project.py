# Heart Disease Prediction App
# by Khaled Waled Talat ❤️

import streamlit as st
import numpy as np
import pickle
import plotly.graph_objects as go

st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️", layout="centered")

# ====== HEADER ======
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>❤️ Heart Disease Prediction</h1>", unsafe_allow_html=True)
st.write("### Provide the patient's details to predict the risk of heart disease.")

# ====== LOAD MODEL ======
try:
    with open(r"C:\Users\DELL\Downloads\Heart_Disease_Project - 2\Models\final_model.pkl", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("❌ Model file not found! Please make sure 'final_model.pkl' exists in the specified path.")
    st.stop()

# ====== INPUTS ======
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age (years)", min_value=0, max_value=120, value=30)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=250, value=120)
    chol = st.number_input("Cholesterol (mg/dl)", min_value=0, max_value=600, value=200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl?", ["Yes", "No"])

with col2:
    restecg = st.selectbox("Resting ECG", ["Normal", "ST-T wave abnormality", "Left Ventricular Hypertrophy"])
    thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)
    exang = st.selectbox("Exercise-Induced Angina", ["Yes", "No"])
    oldpeak = st.number_input("Oldpeak (ST depression)", min_value=0.0, max_value=10.0, step=0.1, value=1.0)
    slope = st.selectbox("ST Slope", ["Upsloping", "Flat", "Downsloping"])
    ca = st.slider("Number of Major Vessels (0-3)", min_value=0, max_value=3, value=0)
    thal = st.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect"])

# ====== ENCODING ======
sex_map = {"Male": 1, "Female": 0}
cp_map = {"Typical Angina": 0, "Atypical Angina": 1, "Non-Anginal Pain": 2, "Asymptomatic": 3}
fbs_map = {"Yes": 1, "No": 0}
restecg_map = {"Normal": 0, "ST-T wave abnormality": 1, "Left Ventricular Hypertrophy": 2}
exang_map = {"Yes": 1, "No": 0}
slope_map = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
thal_map = {"Normal": 1, "Fixed Defect": 2, "Reversible Defect": 3}

input_data = np.array([[
    age,
    sex_map[sex],
    cp_map[cp],
    trestbps,
    chol,
    fbs_map[fbs],
    restecg_map[restecg],
    thalach,
    exang_map[exang],
    oldpeak,
    slope_map[slope],
    ca,
    thal_map[thal]
]])

# ====== PREDICT BUTTON ======
st.markdown("---")
if st.button("🔍 Predict"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1] * 100

    if prediction == 1:
        st.error(f"⚠️ High risk of heart disease detected.")
    else:
        st.success(f"✅ No sign of heart disease detected.")

    # Gauge Chart
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=probability,
        title={'text': "Heart Disease Risk (%)", 'font': {'size': 22}},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "red" if probability > 50 else "green"},
            'steps': [
                {'range': [0, 50], 'color': 'lightgreen'},
                {'range': [50, 100], 'color': 'lightcoral'}
            ],
            'threshold': {'line': {'color': "red", 'width': 4}, 'value': 50}
        }
    ))
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption("Made with ❤️ by Khaled Waled Talat")
