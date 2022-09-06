import streamlit as st

import pandas as pd
import numpy as np

import altair as alt

if __name__ == "__main__":
    st.title("Plotting with Streamlit")
    df = pd.read_csv("data/iris.csv")
    df2 = pd.read_csv("data/lang_data.csv")

    st.dataframe(df2.head())

    # bar chart
    # st.bar_chart(df[['sepal_length', 'petal_length']])

    lang_choices = st.multiselect(label="Choose Language",
                                  options=df2.columns[1:])

    st.line_chart(df2[lang_choices], use_container_width=True)

    # area
    st.area_chart(df2[lang_choices], use_container_width=True)

    # altair
    df3 = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])

    c = alt.Chart(df3).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
    )
    st.dataframe(df3)

    # st.write(c)

    st.altair_chart(c, use_container_width=True)