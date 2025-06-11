import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load('jantung_model.pkl')

# Judul aplikasi
st.title("Prediksi Penyakit Jantung")

# Formulir input data
with st.form("form_jantung"):
    Age = st.number_input('Usia', min_value=1, max_value=120, step=1)
    
    Sex = st.selectbox('Jenis Kelamin', ['M', 'F'])  # M = Male, F = Female

    ChestPainType = st.selectbox('Tipe Nyeri Dada', ['ATA', 'NAP', 'ASY', 'TA'])

    RestingBP = st.number_input('Tekanan Darah Istirahat (RestingBP)', min_value=0, max_value=200)
    
    Cholesterol = st.number_input('Kolesterol', min_value=0, max_value=1000)
    
    FastingBS = st.selectbox('Gula Darah Puasa > 120 mg/dl?', [0, 1])  # 0 = tidak, 1 = ya

    RestingECG = st.selectbox('Hasil EKG Istirahat', ['Normal', 'ST', 'LVH'])

    MaxHR = st.number_input('Detak Jantung Maksimum (MaxHR)', min_value=60, max_value=220)
    
    ExerciseAngina = st.selectbox('Angina saat olahraga?', ['N', 'Y'])  # N = Tidak, Y = Ya
    
    Oldpeak = st.number_input('Oldpeak (depresi ST)', min_value=0.0, max_value=10.0, step=0.1)
    
    ST_Slope = st.selectbox('Kemiringan ST', ['Up', 'Flat', 'Down'])

    submit = st.form_submit_button("Prediksi")

# Saat tombol ditekan
if submit:
    # Encoding manual (sesuai model pelatihan)
    sex_encoded = 1 if Sex == 'M' else 0
    cp_encoded = {'ATA': 0, 'NAP': 1, 'ASY': 2, 'TA': 3}[ChestPainType]
    ecg_encoded = {'Normal': 0, 'ST': 1, 'LVH': 2}[RestingECG]
    angina_encoded = 1 if ExerciseAngina == 'Y' else 0
    slope_encoded = {'Up': 0, 'Flat': 1, 'Down': 2}[ST_Slope]

    # Buat array fitur
    features = np.array([[Age, sex_encoded, cp_encoded, RestingBP, Cholesterol, FastingBS,
                          ecg_encoded, MaxHR, angina_encoded, Oldpeak, slope_encoded]])

    # Prediksi
    prediction = model.predict(features)[0]

    # Tampilkan hasil
    if prediction == 1:
        st.error("Hasil: Positif - Terindikasi Penyakit Jantung")
    else:
        st.success("Hasil: Negatif - Tidak Terindikasi Penyakit Jantung")
