import requests
import streamlit as st

URL = "https://api.open-meteo.com/v1/forecast"

latitude = st.text_input("Latitude")
longitude = st.text_input("Longitude")

params = {
    "latitude": latitude,
    "longitude": longitude,
    "current_weather": "true"
}

if len(longitude) != 0:
    response = requests.get(URL, params)

    if response.status_code == 200:
        st.button("Success", type="secondary")
    else:
        st.button("Error", type="primary")
    st.json(response.json()["current_weather"])
