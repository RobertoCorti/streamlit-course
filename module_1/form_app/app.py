import streamlit as st
import pandas as pd

if __name__ == "__main__":

    st.title("Streamlit Forms & Salary Calculator")
    menu = ["Home", "About"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Forms Tutorial")
        with st.form(key="salary_form", clear_on_submit=True):
            col1, col2, col3 = st.columns([3, 2, 1])

            with col1:
                amount = st.number_input(label="Hourly Rate in EUR")

            with col2:
                hour_per_week = st.number_input(label="Hours per Week", min_value=1, max_value=120)

            with col3:
                st.text("Salary")
                submit_salary = st.form_submit_button(label="Calculate")

        if submit_salary:
            with st.expander("Result"):
                daily = [amount * 8]
                weekly = [amount * hour_per_week]
                df = pd.DataFrame({'hourly': amount, 'daily': daily, 'weekly': weekly}, index=["EUR"])
                st.dataframe(df.T)

        # Method 1: Context manager approach (with)
        with st.form(key="form1", clear_on_submit=True):
            first_name = st.text_input("Firstname")
            last_name = st.text_input("Lastname")
            dob = st.date_input("Date of Birth")
            submit_button = st.form_submit_button(label="SignUp")

        # results can be either form or outside
        if submit_button:
            st.success(f"Account created successfully for {first_name} {last_name}")

        # Method 2: variable approach
        form2 = st.form(key="form2", clear_on_submit=True)
        user_name = form2.text_input(label="Username")
        job_type = form2.selectbox(label="Job", options=["Dev", "Data Scientist", "Data Engineer"])
        submit_button2 = form2.form_submit_button(label="Login")

        if submit_button2:
            st.write(user_name.upper())


    else:
        st.subheader("About")
