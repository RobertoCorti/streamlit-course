import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Plotting in Streamlit with Plotly")

df = pd.read_csv('./module_1/data/prog_languages_data.csv')

st.dataframe(df)

fig = px.pie(df, values='Sum', names='lang', title='Programming Languages')
st.plotly_chart(fig)

fig2 = px.bar(df, x='lang', y='Sum', title='Programming Languages')
st.plotly_chart(fig2)