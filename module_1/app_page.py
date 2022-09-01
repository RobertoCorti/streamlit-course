import streamlit as st
from PIL import Image

img = Image.open('./module_1/data/image_01.jpg')

# configuration of the page
st.set_page_config(page_title="Hello", page_icon=img,
                   layout='wide', initial_sidebar_state='collapsed')


# title of the page
st.title("Hello Streamlit lovers 🫂")

st.sidebar.success("Menu")

