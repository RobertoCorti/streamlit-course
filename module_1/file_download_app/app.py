import streamlit as st
import streamlit.components as stc

import base64
import time
import pandas as pd

timestr = time.strftime("%Y%m%d-%H%M%S")


# function approach

# def text_downloader(raw_text):
#    b64 = base64.b64encode(raw_text.encode()).decode()
#    new_filename = f"new_text_file_{timestr}_.txt"
#    st.markdown("#### Download File ###")
#    href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Click Here!!</a>'  # html code for download link
#    st.markdown(href, unsafe_allow_html=True)


# def csv_downloader(raw_data):
#    csv_file = raw_data.to_csv(index=False)
#    b64 = base64.b64encode(csv_file.encode()).decode()
#    new_filename = f"new_text_file_{timestr}_.csv"
#    st.markdown("#### Download File ###")
#    href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Click Here!!</a>'  # html code for download link
#    st.markdown(href, unsafe_allow_html=True)


# class approach
class FileDownloader(object):

    def __init__(self, data, file_ext='txt'):
        self.data = data
        self.file_ext = file_ext

    def download(self, file_name=None):
        if file_name is None:
            file_name = f'downloaded_file_{timestr}.{self.file_ext}'
        b64 = base64.b64encode(self.data.encode()).decode()
        new_filename = f"new_text_file_{timestr}_.{self.file_ext}"
        st.markdown("#### Download File ###")
        href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Click Here!!</a>'  # html code for download link
        st.markdown(href, unsafe_allow_html=True)


class CSVDownloader(object):

    def __init__(self, data):
        self.df = data

    def download(self, file_name=None):
        if file_name is None:
            file_name = f'downloaded_file_{timestr}.csv'
        csv_file = self.df.to_csv(index=False)
        b64 = base64.b64encode(csv_file.encode()).decode()
        new_filename = f"new_text_file_{timestr}_.csv"
        st.markdown("#### Download File ###")
        href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Click Here!!</a>'  # html code for download link
        st.markdown(href, unsafe_allow_html=True)


if __name__ == "__main__":

    menu = ["Home", "CSV", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        my_text = st.text_area("Your Message")

        if st.button("Save"):
            st.write(my_text)
            # text_downloader(my_text)
            FileDownloader(my_text).download()
    elif choice == "CSV":
        st.subheader("CSV")
        df = pd.read_csv("data/iris.csv")
        st.dataframe(df)
        # csv_downloader(df)
        CSVDownloader(df).download()
    else:
        st.subheader("About")
