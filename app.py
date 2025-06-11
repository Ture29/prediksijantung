import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load('jantung_model.pkl')

st.title("Prediksi Penyakit Jantung")

st.markdown("### Masukkan Data Pasien")

with st.form("form_jantung"):
    # Input numerik yang akan diskalakan
    age = st.number_input("Age (sudah diskalakan)", format="%.3f")
    resting_bp = st.number_input("Resting Blood Pressure (sudah diskalakan)", format="%.3f")
    cholesterol = st.number_input("Cholesterol (sudah diskalakan)", format="%.3f")
    fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl?", [0, 1])
    max_hr = st.number_input("Max Heart Rate (sudah diskalakan)", format="%.3f")
    oldpeak = st.number_input("Oldpeak (ST depression) (sudah diskalakan)", format="%.3f")

    # One-hot untuk Sex
    sex = st.selectbox("Sex", ["F", "M"])
    sex_f = 1 if sex == "F" else 0
    sex_m = 1 if sex == "M" else 0

    # One-hot untuk ChestPainType
    chest_pain = st.selectbox("Chest Pain Type", ["ASY", "ATA", "NAP", "TA"])
    cpt_asy = 1 if chest_pain == "ASY" else 0
    cpt_ata = 1 if chest_pain == "ATA" else 0
    cpt_nap = 1 if chest_pain == "NAP" else 0
    cpt_ta = 1 if chest_pain == "TA" else 0

    # One-hot untuk RestingECG
    ecg = st.selectbox("Resting ECG", ["LVH", "Normal", "ST"])
    ecg_lvh = 1 if ecg == "LVH" else 0
    ecg_normal = 1 if ecg == "Normal" else 0
    ecg_st = 1 if ecg == "ST" else 0

    # One-hot untuk ExerciseAngina
    angina = st.selectbox("Exercise Angina", ["N", "Y"])
    angina_n = 1 if angina == "N" else 0
    angina_y = 1 if angina == "Y" else 0

    # One-hot untuk ST Slope
    slope = st.selectbox("ST Slope", ["Down", "Flat", "Up"])
    slope_down = 1 if slope == "Down" else 0
    slope_flat = 1 if slope == "Flat" else 0
    slope_up = 1 if slope == "Up" else 0

    submit = st.form_submit_button("Prediksi")

if submit:
    # Susun data sesuai urutan training
    data = [[
        age, resting_bp, cholesterol, fasting_bs, max_hr,
        oldpeak, sex_f, sex_m, cpt_asy, cpt_ata,
        cpt_nap, cpt_ta, ecg_lvh, ecg_normal, ecg_st,
        angina_n, angina_y, slope_down, slope_flat, slope_up
    ]]
    
    prediction = model.predict(data)[0]
    
    st.markdown("### Hasil Prediksi")
    if prediction == 1:
        st.error("🚨 Terdeteksi Penyakit Jantung!")
    else:
        st.success("✅ Tidak Terdeteksi Penyakit Jantung")
