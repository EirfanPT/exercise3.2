import streamlit as st

num1 = st.text_input("Enter first number:")
num2 = st.text_input("Enter second number:")

if st.button("Divide"):
    try:
        n1 = float(num1)
        n2 = float(num2)
        result = n1 / n2
    except ValueError:
        st.error("Invalid input! Please enter numeric values.")
    except ZeroDivisionError:
        st.error("Error! Cannot divide by zero.")
    else:
        st.success(f"Division successful. Result: {result}")