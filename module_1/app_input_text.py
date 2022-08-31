import streamlit as st

# text
fname = st.text_input('Enter First name')
st.write(fname)

# text area
message = st.text_area('Enter message', height=100)
st.write(message)

# number input
number = st.number_input('Enter number', min_value=0.0, max_value=100.0, step=0.2)
st.write(number)

# date input
date = st.date_input('Enter date')
st.write(date)

# time input
time = st.time_input('Enter time')
st.write(time)

# text input hide password
password = st.text_input('Enter password', type='password')
if password == "aaa":
    st.success('You entered the correct password')
else:
    st.error('You entered the wrong password')

# color input
color = st.color_picker('Pick a color')
st.write(color)