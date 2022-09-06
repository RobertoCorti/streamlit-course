import matplotlib
import streamlit as st

import pandas as pd
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

matplotlib.use('Agg')

if __name__ == "__main__":
    st.title("Plotting with st.Pyplot")
    df = pd.read_csv("data/iris.csv")

    st.dataframe(df.head())

    # df['species'].value_counts().plot(kind='bar')
    # st.pyplot()

    # fig, ax = plt.subplots()
    #
    # ax.scatter(x=np.random.random(size=100),
    #           y=np.random.random(size=100))
    # st.pyplot(fig=fig)

    # fig = plt.figure()
    # df['species'].value_counts().plot(kind='bar')
    # st.pyplot(fig=fig)

    # fig, ax = plt.subplots()
    # df['species'].value_counts().plot(kind='bar')
    # st.pyplot(fig=fig)

    fig = plt.figure()
    sns.countplot(df['species'])
    st.pyplot(fig=fig)