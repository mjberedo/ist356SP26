#Use the IoT portal for the URI to search for funny names. Once you understand how to invoke the REST API, write a streamlit to 
#input a name and return the matches in a dataframe. 

import streamlit as st
import requests
import pandas as pd

st.title("Funny Name Search")

name = st.text_input("Enter a name to search for funny names:")
if st.button("Search"):
    # Call the REST API to search for funny names
    response = requests.get(f"https://cent.ischool-iot.net/api/funnyname/random?name={name}")
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.error("Error fetching data from API")
        st.stop()