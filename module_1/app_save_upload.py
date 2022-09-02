import streamlit as st

from PIL import Image
import pandas as pd
import docx2txt
from PyPDF2 import PdfFileReader
import pdfplumber


def save_uploadedfile(uploadedfile):
    with open(f"temp_dir/{uploadedfile.name}", "wb") as f:
        f.write(uploadedfile.getbuffer())
    return uploadedfile.name


@st.cache
def load_image(img):
    im = Image.open(img)
    return im


@st.cache
def load_csv(data_file_input):
    data = pd.read_csv(data_file_input)
    return data


def read_pdf(file):
    pdfReader = PdfFileReader(file)
    count = pdfReader.numPages
    all_pages_text = ""
    for i in range(count):
        page = pdfReader.getPage(i)
        all_pages_text += page.extractText()
    return all_pages_text


if __name__ == "__main__":
    st.title("File Upload Tutorial")

    menu = ["Home", "Dataset", "DocumentFiles", "About"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        image_file = st.file_uploader("Upload Image",
                                      type=['png', 'jpeg', 'jpg'])
        if image_file is not None:
            file_details = {"FileName": image_file.name,
                            "FileType": image_file.type,
                            "FileSize": image_file.size}
            st.write(file_details)
            st.image(load_image(image_file), width=250, caption="Uploaded Image")
            save_uploadedfile(image_file)
            st.success("Image saved successfully")
    elif choice == "Dataset":
        st.subheader("Dataset")
        data_file = st.file_uploader("Upload Dataset",
                                     type=['csv'])
        if data_file is not None:
            file_details = {"FileName": data_file.name,
                            "FileType": data_file.type,
                            "FileSize": data_file.size}
            st.write(file_details)
            st.dataframe(load_csv(data_file))
            save_uploadedfile(data_file)
            st.success("Data saved successfully")
    elif choice == "DocumentFiles":
        st.subheader("Document Files")
        doc_file = st.file_uploader("Upload Document",
                                    type=['pdf', 'docx', 'txt'])
        if st.button("Process"):
            if doc_file is not None:
                file_details = {"FileName": doc_file.name,
                                "FileType": doc_file.type,
                                "FileSize": doc_file.size}
                st.write(file_details)
                if doc_file.type == 'application/pdf':
                    st.write("PDF File")
                    raw_text = read_pdf(doc_file)
                    st.write(raw_text)
                    # try:
                    #    with pdfplumber.open(doc_file) as pdf:
                    #        pages = pdf.pages[-1]
                    #        text = pages.extract_text()
                    #        st.write(text)
                    # except:
                    #    st.write("Error in reading file")
                elif doc_file.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
                    st.write("Word File")
                    raw_text = docx2txt.process(doc_file)
                    st.write(raw_text)

                elif doc_file.type == 'text/plain':
                    st.write("Text File")
                    raw_text = str(doc_file.read(), "utf-8")
                    st.text(raw_text)

                save_uploadedfile(doc_file)
                st.success("File saved successfully")
    else:
        st.subheader("About")
