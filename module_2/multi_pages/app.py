import streamlit as st

my_var = "From Main App.py Page"


def main():
    st.title("Streamlit Multi-Page")
    st.subheader("Main Page")
    st.write(my_var)

    submenu = st.sidebar.selectbox("SubMenu", ["Pandas", "Tensorflow"])
    if submenu == "Pandas":
        st.subheader("Pandas")
    else:
        st.subheader("Tensorflow")

if __name__ == "__main__":
    main()
