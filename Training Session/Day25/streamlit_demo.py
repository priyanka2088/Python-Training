import streamlit as st

username = st.text_input("Username")
st.write("The current username is", username)

username = st.text_input("Password", type="password")

st.button("Login", type="primary")
