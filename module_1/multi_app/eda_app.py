import streamlit as st

import pandas as pd
import plotly.express as px


def run_eda_app():
    st.subheader("Exploratory Data Analysis App")
    df = pd.read_csv("data/diabetes_data_upload.csv")
    st.dataframe(df)

    fig = px.histogram(df, y='Gender', title='Gender')
    st.plotly_chart(fig)

    fig2 = px.histogram(df, x='Age', title='Age')
    st.plotly_chart(fig2)

