import streamlit as st

from eda_app import run_eda_app
from ml_app import run_ml_app

if __name__ == "__main__":
    st.title("Multi App")

    menu = ["Home", "EDA", "ML", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
    elif choice == "EDA":
        run_eda_app()
    elif choice == "ML":
        run_ml_app()
    elif choice == "About":
        st.subheader("About")
        st.write("This is a multi app")
