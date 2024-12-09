import streamlit as st

option = st.selectbox(
    "Select the operation",
    ("Add", "Subtract", "Multiply", "Divide")
)

number_a = st.text_input("Number A")
number_b = st.text_input("Number B")

if number_a and number_b:
    if option == "Add":
        st.text(int(number_a) + int(number_b))
    elif option == "Subtract":
        st.text(int(number_a) - int(number_b))
    elif option == "Multiply":
        st.text(int(number_a) * int(number_b))
    elif option == "Divide":
        st.text(int(number_a) / int(number_b))