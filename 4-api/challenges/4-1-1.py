#Write a streamlit to read from the url:

#https://jsonplaceholder.typicode.com/users/

#Then display the data in a pandas dataframe. 

 #- use the requests library to get the data
 #- use `json_normalize()` to convert the nested json data into a dataframe

'''
curl -X 'GET' \
'https://cent.ischool-iot.net/api/funnyname/random' \
-H 'accept: application/json'

'''

import streamlit as st
import requests
import pandas as pd

def main():
    st.title("User Data from JSONPlaceholder")

    url = 'https://jsonplaceholder.typicode.com/users/'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        
        # Normalize the nested JSON data into a flat table
        df = pd.json_normalize(data)
        
        st.dataframe(df)  # Display the dataframe in Streamlit
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        st.stop()

if __name__ == "__main__":
    main()

