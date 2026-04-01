import streamlit as st

num = st.text_input("Enter a number:")

if st.button("Calculate Square"):
    try:
        n = float(num)
        st.success(f"Square: {n ** 2}")
    except ValueError:
        st.error("Invalid input! Please enter a number.")