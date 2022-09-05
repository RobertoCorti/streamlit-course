import streamlit as st

import logging

LOGS_FORMAT = '%(levelname)s - %(asctime)s.%(msecs)s - %(message)s'
# logging.basicConfig(format=LOGS_FORMAT, level=logging.DEBUG)
# logger = logging.getLogger(__name__)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(LOGS_FORMAT)
file_handler = logging.FileHandler('app.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
if __name__ == "__main__":
    st.title("Multi App")
    st.write("Track All Activities of APP")

    menu = ["Home", "EDA", "ML", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        logger.info("Home Page")
    elif choice == "EDA":
        st.subheader("EDA")
        logger.info("EDA Page")
    elif choice == "ML":
        st.subheader("Machine Learning App")
        logger.info("ML Page")
    elif choice == "About":
        st.subheader("About")
        st.write("This is a multi app")
        logger.info("About Page")
