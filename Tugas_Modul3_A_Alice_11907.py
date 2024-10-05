import streamlit as st
import pandas as pd
import pickle
import os

st.markdown("""
    <style>
        .main {
            background-color: #1e1e1e;
            color: #ffffff;
        }
        .stButton button {
            background-color: #333333;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 18px;
        }
        .stTextInput, .stNumberInput input {
            background-color: #333333;
            border: 2px solid #ffffff;
            color: #ffffff;
        }
        .stSidebar {
            background-color: #000000;
            color: #ffffff;
        }
        .stSidebar h3, .stSidebar p, .stSidebar label, .stSidebar .header-text {
            color: #ffffff;
        }
        h1 {
            font-family: 'Courier New', monospace;
            color: #ffffff;
            font-size: 18px;
        }
        h3, p {
            font-family: 'Arial', sans-serif;
            color: #ffffff;
        }
        .uploadedFile {
            font-family: 'Arial', sans-serif;
            color: #cccccc;
        }
        .center {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            height: 100px;
        }
        .center img {
            width: 150px;
            height: 100px;
            object-fit: contain;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="center">
    <img src="https://media.tenor.com/oqJo9GcBfyYAAAAd/welcome-images-server.gif" alt="Welcome Image">
</div>
""", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Prediksi IPK - 2025</h1>", unsafe_allow_html=True) 
st.markdown("<p style='text-align: center; color: #0073e6;'>Aplikasi ini berguna untuk memprediksi IPK berdasarkan nilai Matematika, Bahasa Inggris, dan Bahasa Indonesia</p>", unsafe_allow_html=True)

st.sidebar.markdown("<h3 class='header-text'>Upload File dan Input Nilai</h3>", unsafe_allow_html=True)
uploaded_file = st.sidebar.file_uploader("Upload file dataset_regresi_IPK.csv", type=["csv"])


if uploaded_file is not None:
    # Read CSV file
    input_data = pd.read_csv(uploaded_file)
    st.write("<h3 style='text-align: center; color: #0073e6;'>Data yang diupload:</h3>", unsafe_allow_html=True)
    st.dataframe(input_data)

    model_directory = r"C:\Users\lenovo\Documents\Machine Learning\Tugas3_A_11907"
    model_path = os.path.join(model_directory, r"SVR_IPK_model.pkl")

    if os.path.exists(model_path):
        with open(model_path, 'rb') as f:
            loaded_model = pickle.load(f)

        scaler = loaded_model[0]
        feature_selector = loaded_model[1]
        SVR_model = loaded_model[2]

    # Sidebar untuk input nilai
    st.sidebar.subheader("Masukkan Nilai")
    mtk1 = st.sidebar.number_input("Nilai Matematika Semester 1.1", 60.0, 100.0)
    mtk2 = st.sidebar.number_input("Nilai Matematika Semester 1.2", 60.0, 100.0)
    mtk3 = st.sidebar.number_input("Nilai Matematika Semester 2.1", 60.0, 100.0)
    mtk4 = st.sidebar.number_input("Nilai Matematika Semester 2.2", 60.0, 100.0)
    ing1 = st.sidebar.number_input("Nilai Bahasa Inggris Semester 1.1", 64.0, 98.0)
    ing2 = st.sidebar.number_input("Nilai Bahasa Inggris Semester 1.2", 62.0, 99.0)
    ing3 = st.sidebar.number_input("Nilai Bahasa Inggris Semester 2.1", 68.0, 99.0)
    ing4 = st.sidebar.number_input("Nilai Bahasa Inggris Semester 2.2", 67.0, 98.0)
    ind1 = st.sidebar.number_input("Nilai Bahasa Indonesia Semester 1.1", 70.0, 100.0)
    ind2 = st.sidebar.number_input("Nilai Bahasa Indonesia Semester 1.2", 65.0, 99.0)
    ind3 = st.sidebar.number_input("Nilai Bahasa Indonesia Semester 2.1", 66.0, 99.0)
    ind4 = st.sidebar.number_input("Nilai Bahasa Indonesia Semester 2.2", 70.0, 100.0)

    # KKN
    st.sidebar.subheader("Masukkan KKN Nilai")
    kkn_ind1 = st.sidebar.number_input("KKN Nilai Bahasa Indonesia Semester 1.1", 0.0, 100.0)
    kkn_ind2 = st.sidebar.number_input("KKN Nilai Bahasa Indonesia Semester 1.2", 0.0, 100.0)
    kkn_ind3 = st.sidebar.number_input("KKN Nilai Bahasa Indonesia Semester 2.1", 0.0, 100.0)
    kkn_ind4 = st.sidebar.number_input("KKN Nilai Bahasa Indonesia Semester 2.2", 0.0, 100.0)
    kkn_ing1 = st.sidebar.number_input("KKN Nilai Bahasa Inggris Semester 1.1", 0.0, 100.0)
    kkn_ing2 = st.sidebar.number_input("KKN Nilai Bahasa Inggris Semester 1.2", 0.0, 100.0)
    kkn_ing3 = st.sidebar.number_input("KKN Nilai Bahasa Inggris Semester 2.1", 0.0, 100.0)
    kkn_ing4 = st.sidebar.number_input("KKN Nilai Bahasa Inggris Semester 2.2", 0.0, 100.0)
    kkn_mtk1 = st.sidebar.number_input("KKN Nilai Matematika Semester 1.1", 0.0, 100.0)
    kkn_mtk2 = st.sidebar.number_input("KKN Nilai Matematika Semester 1.2", 0.0, 100.0)
    kkn_mtk3 = st.sidebar.number_input("KKN Nilai Matematika Semester 2.1", 0.0, 100.0)
    kkn_mtk4 = st.sidebar.number_input("KKN Nilai Matematika Semester 2.2", 0.0, 100.0)

    input_data = [[mtk1, mtk2, mtk3, mtk4, ing1, ing2, ing3, ing4, ind1, ind2, ind3, ind4,
                   kkn_mtk1, kkn_mtk2, kkn_mtk3, kkn_mtk4, kkn_ing1, kkn_ing2, kkn_ing3, kkn_ing4,
                   kkn_ind1, kkn_ind2, kkn_ind3, kkn_ind4]]

    input_data_scaled = scaler.transform(input_data)
    input_data_selected = feature_selector.transform(input_data_scaled)

    if st.sidebar.button("Prediksi"):
        SVR_model_predict = SVR_model.predict(input_data_selected)
        st.markdown(f"<h3 style='text-align: center; color: #4CAF50;'>Prediksi IPK adalah: {SVR_model_predict[0]:.2f}</h3>", unsafe_allow_html=True)
    else:
        st.error("Model tidak ditemukan, silakan cek file model di direktori.")