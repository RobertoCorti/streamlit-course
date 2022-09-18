import streamlit as st
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Agg")


def main():
    """Streamlit Theming"""
    st.title("Streamlit Theming")

    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        fname = st.text_input("Fname")
        occupations = st.multiselect("Work", ["Data Scientist", "Developer", "Doctor", "Designer"])
        message = st.text_area('Message')
        if st.button("Submit"):
            st.write("Welcome {} !".format(fname))
            st.write(message)
            st.success("Submitted")

        col1, col2 = st.beta_columns(2)
        with col1:
            with st.beta_expander('First'):
                st.info("Streamlit is Awesome")
                st.write(message)
                my_dict = {"fname": fname, "message": message}
                st.json(my_dict)

        with col2:
            with st.beta_expander('Second'):
                st.warning("Warning: This is Lit")
                st.success("Success: This is So cool")
                st.info("Info: This is Lit")

    elif choice == "About":
        st.subheader("About")


if __name__ == '__main__':
    main()
