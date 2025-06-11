import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load('jantung_model.pkl')

st.title("Prediksi Penyakit Jantung")

with st.form("form_jantung"):
    Age = st.number_input('Usia (Age)', min_value=1, max_value=120, step=1)
    Sex = st.selectbox('Jenis Kelamin (Sex)', ['M', 'F'])
    ChestPainType = st.selectbox('Tipe Nyeri Dada (ChestPainType)', ['ATA', 'NAP', 'ASY', 'TA'])
    RestingBP = st.number_input('Tekanan Darah Saat Istirahat (RestingBP)', min_value=0, max_value=200)
    Cholesterol = st.number_input('Kolesterol (Cholesterol)', min_value=0, max_value=1000)
    FastingBS = st.selectbox('Gula Darah Puasa > 120? (FastingBS)', [0, 1])
    RestingECG = st.selectbox('Hasil EKG Saat Istirahat (RestingECG)', ['Normal', 'ST', 'LVH'])
    MaxHR = st.number_input('Detak Jantung Maksimum (MaxHR)', min_value=60, max_value=220)
    ExerciseAngina = st.selectbox('Angina saat olahraga? (ExerciseAngina)', ['N', 'Y'])
    Oldpeak = st.number_input('Oldpeak (depresi ST)', min_value=0.0, max_value=10.0, step=0.1)
    ST_Slope = st.selectbox('Kemiringan ST (ST_Slope)', ['Up', 'Flat', 'Down'])
    submit = st.form_submit_button("Prediksi")

if submit:
    # Encoding fitur kategorikal
    sex_encoded = 1 if Sex == 'M' else 0
    cp_encoded = {'ATA': 0, 'NAP': 1, 'ASY': 2, 'TA': 3}[ChestPainType]
    ecg_encoded = {'Normal': 0, 'ST': 1, 'LVH': 2}[RestingECG]
    angina_encoded = 1 if ExerciseAngina == 'Y' else 0
    slope_encoded = {'Up': 0, 'Flat': 1, 'Down': 2}[ST_Slope]

    # Susun fitur sesuai urutan yang dipakai model
    features = np.array([[Age, sex_encoded, cp_encoded, RestingBP, Cholesterol,
                          FastingBS, ecg_encoded, MaxHR, angina_encoded, Oldpeak, slope_encoded]])

    prediction = model.predict(features)[0]

    if prediction == 1:
        st.error("Hasil: Positif - Terindikasi Penyakit Jantung")
    else:
        st.success("Hasil: Negatif - Tidak Terindikasi Penyakit Jantung")
