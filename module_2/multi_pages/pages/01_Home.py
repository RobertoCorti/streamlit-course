import streamlit as st
from app import my_var
from pages.eda import my_calc
st.subheader("Home Page")
st.write(my_var)
st.write(my_calc)