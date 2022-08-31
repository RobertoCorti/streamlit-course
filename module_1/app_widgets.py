import streamlit as st

name = "Roberto"
if st.button('Click me'):
    st.write(f'Hello {name}')

# radio button
status = st.radio('What is your status', ('Active', 'Inactive'))

if status == 'Active':
    st.success('You are active')
else:
    st.warning('You are inactive')

# checkbox
if st.checkbox('Show'):
    st.text('Showing something')

# expander
with st.expander('Python'):
    st.success('hello Python')

# selectbox
language = st.selectbox('What is your favorite language',
                        ('Python', 'R', 'Java', 'C++'))
st.write(f'You selected {language}')

# multiselectbox
languages = st.multiselect('What are your favorite languages',
                           ('Python', 'R', 'Java', 'C++'))
text = "You selected: "
for language in languages:
    text += f'{language}, '
st.write(f'{text[:-2]}')

# slider
age = st.slider('What is your age', 0, 100)
st.write(f'You are {age} years old')

# select slider
color = st.select_slider('What is your favorite color',
                         ('Yellow', 'Red', 'Green', 'Blue'),
                         value=['Yellow', 'Red'])
st.write(f'You selected {color}')
