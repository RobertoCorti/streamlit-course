import streamlit as st

from PIL import Image


@st.cache
def load_image(img):
    im = Image.open(img)
    return im


def save_uploaded_file(uploaded_file):
    with open(f"temp_dir/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.getbuffer())
    return uploaded_file.name


if __name__ == "__main__":
    st.title("Multiple file upload")

    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Upload Multiple Files")

        image_files = st.file_uploader("Upload Multiple Images",
                                       type=['png', 'jpeg', 'jpg'],
                                       accept_multiple_files=True)
        if image_files is not None:
            for image_file in image_files:
                file_details = {"FileName": image_file.name,
                                "FileType": image_file.type,
                                "FileSize": image_file.size}
                st.write(file_details)
                st.image(load_image(image_file), width=250, caption="Uploaded Image")
                save_uploaded_file(image_file)
                st.success("Image saved successfully")
    elif choice == "About":
        st.subheader("About")
        st.write("Streamlit Multiple File Upload Tutorial")