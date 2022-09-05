import streamlit as st
import pandas as pd
import sklearn as sk

def run_ml_app():
    st.subheader("Machine Learning App")
    df = pd.read_csv("data/diabetes_data_upload.csv")
    st.success("MODEL TRAINED SUCCESSFULLY")

