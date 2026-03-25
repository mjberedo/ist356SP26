import requests
import pandas as pd
import json
import streamlit as st

st.title('API Example API to Pandas')


url = "https://jsonplaceholder.typicode.com/users/"

# Write your code here to call the API and display results in a dataframe

response = requests.get(url)
response.raise_for_status() # raise an error if the request failed
data = response.json() # parse the JSON response into a Python object (list of dicts)
st.write(data) # display the raw data in streamlit
df = pd.json_normalize(data) # convert the list of dicts into a pandas dataframe
st.dataframe(df) # display the dataframe in streamlit