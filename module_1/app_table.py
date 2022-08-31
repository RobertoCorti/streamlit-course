import streamlit as st
import pandas as pd

# display data
df = pd.read_csv("./data/iris.csv")

st.title("Iris Dataset")

# method one
# st.dataframe(df)

# st.dataframe(df.style.highlight_max(axis=0))

# method two
# st.table(df)

# method three
st.write(df.head())

# display json
st.json(df.to_json(orient="records"))

# display code
mycode = """
import pandas as pd
df = pd.read_csv("./data/iris.csv")
st.write(df.head())
"""
st.code(mycode, language="python")
