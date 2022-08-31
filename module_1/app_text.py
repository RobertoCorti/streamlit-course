import streamlit as st

# text
st.text('Hello World, this is a text')

name = "Roberto"
st.text(f'My name is {name}')

# headers
st.header('This is a header')
st.subheader('This is a subheader')

# title
st.title('This is a title')

# markdown
st.markdown('This is a markdown')

st.markdown('### This is a markdown at header 3')

# display colored text/boostraps alert
st.success('This is a success message')
st.warning('This is a warning message')
st.info('This is a info message')
st.error('This is a error message')
st.exception('This is a exception message')

# superfunction
st.write("Normal text")
st.write('## This is a markdown text')
st.write(1 + 1)

# help
# st.help(st.write)


