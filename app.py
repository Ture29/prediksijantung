import streamlit as st
import numpy as np
import joblib
model = joblib.load('jantung_model.pkl')
st.title("Prediksi Jantung")
# Form input
with st.form("form_jantung"):
  Age = st.number_input('Age', min_value=0, max_value=20, step=1)
  Sex = st.number_input('Sex', min_value=0, max_value=200)
  ChestPainType = st.number_input('ChestPainType', min_value=0, max_value=150)
  RestingBP = st.number_input('RestingBP', min_value=0, max_value=100)
  Cholesterol = st.number_input('Cholesterol', min_value=0, max_value=1000)
  FastingBS = st.number_input('FastingBS', min_value=0.0, max_value=70.0)
  RestingECG_ST = st.number_input('RestingECG_ST', min_value=0.0, max_value=2.5)
  MaxHR = st.number_input('MaxHR', min_value=1, max_value=120)
  ExerciseAngina = st.number_input('ExerciseAngina_Y', min_value=1, max_value=120)
  Oldpeak  = st.number_input('Oldpeak', min_value=1, max_value=120)
  ST_Slope = st.number_input('ST_Slope_Up', min_value=1, max_value=120)
  submit = st.form_submit_button("Proses")
# Ketika tombol ditekan
if submit:
# Format input ke bentuk array
   features = np.array([[Age, Sex,
ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG_ST, MaxHR, ExerciseAngina, Oldpeak, ST_Slope]])
# Prediksi
   prediction = model.predict(features)[0]
# Tampilkan hasil
   if prediction == 1:
      st.error("Hasil: Positif Jantung")
   else:
      st.success("Hasil: Negatif Penyakit Jantung")
