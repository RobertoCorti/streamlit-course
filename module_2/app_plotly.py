import streamlit as st

import pandas as pd
import numpy as np

import plotly.express as px

if __name__ == "__main__":
    st.title("Plotting in Streamlit with Plotly")

    df = pd.read_csv("data/prog_languages_data.csv")

    st.dataframe(df)

    fig = px.pie(data_frame=df,
                 values='Sum',
                 labels='lang',
                 title="Pie chart of Languages")
    st.plotly_chart(fig)

    fig2 = px.bar(data_frame=df, x='lang', y='Sum')
    st.plotly_chart(fig2)

