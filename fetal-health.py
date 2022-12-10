import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('fetal-health.sav', 'rb'))

st.title('Prediksi Kesehatan Janin')

col1, col2, col3 = st.columns(3)

with col1:
     baseline_value = st.number_input('Nilai dasar')

with col2:
    accelerations = st.number_input('Akselerasi')

with col3:
    fetal_movement = st.number_input('Gerakan janin')

with col1:
    uterine_contractions = st.number_input('Kontraksi Rahim')

with col2:
    light_decelerations = st.number_input('Deselerasi Ringan')

with col3:
    severe_decelerations = st.number_input('Deselerasi Parah')

with col1:
    prolongued_decelerations = st.number_input('Deselerasi Berkepanjangan')

with col2:
    abnormal_short_term_variability = st.number_input('Variabilitas jangka Pendek Yang Abnormal')

with col3:
    mean_value_of_short_term_variability =  st.number_input('Nilai Rata-Rata Variabilitas Jangka Pendek')

with col1:
    percentage_of_time_with_abnormal_long_term_variability =  st.number_input('Persentase Waktu Dengan Variabilitas Jangka Panjang Abnormal')

with col2:
    mean_value_of_long_term_variability = st.number_input('Nilai Rata-Rata Variabilitas Jangka Panjang')

with col3:
    histogram_width = st.number_input('Lebar Histogram')

with col1:
    histogram_min = st.number_input('Minimum Histogram')

with col2:
    histogram_max = st.number_input('Maksimum Histogram')

with col3:
    histogram_number_of_peaks = st.number_input('Jumlah Histogram Puncak')

with col1:
    histogram_number_of_zeroes = st.number_input('Jumlah Histogram Nol')

with col2:
    histogram_mode = st.number_input('Mode Histogram')

with col3:
    histogram_mean = st.number_input('Rata-Rata Histogram')

with col1:
    histogram_median = st.number_input('Median Histogram')

with col2:
    histogram_variance = st.number_input('Varian Histogram')

with col3:
    histogram_tendency = st.number_input('Kecenderungan Histogram')

fetal_diagnosis = ''

if st.button('Prediksi Kesehatan Janin'):
    fetal_prediction = model.predict([[baseline_value, accelerations, fetal_movement, uterine_contractions, light_decelerations, severe_decelerations, prolongued_decelerations, abnormal_short_term_variability, mean_value_of_short_term_variability, percentage_of_time_with_abnormal_long_term_variability, mean_value_of_long_term_variability,histogram_width, histogram_min, histogram_max, histogram_number_of_peaks, histogram_number_of_zeroes, histogram_mode, histogram_mean, histogram_median, histogram_variance, histogram_tendency]])

    if(fetal_prediction[0]==0):
        fetal_diagnosis = 'Tingkat Resiko Rendah'
    elif(fetal_prediction[0]==1):
        fetal_diagnosis = 'Tingkat Resiko Sedang'
    else:
        fetal_diagnosis = 'Tingkat Resiko Tinggi'

st.success(fetal_diagnosis)
