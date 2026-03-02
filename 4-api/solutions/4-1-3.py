'''
Geocodes 

curl -X 'GET' \
  'https://cent.ischool-iot.net/api/google/geocode?location=syracuse%20university' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: ec25dc1e1297cfba51838bd3'
  
  
  
  Weather
  
curl -X 'GET' \
  'https://cent.ischool-iot.net/api/weather/current?units=imperial%20&lon=-76&lat=43' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: ec25dc1e1297cfba51838bd3'


'''


import pandas as pd
import numpy as np  
import requests
import json

import streamlit as st

st.title("Geocode and Weather API Example")
location = st.text_input("Enter a location to get current weather:")
if st.button("Get Weather"):
  
    url = "https://cent.ischool-iot.net/api/google/geocode"
    querystring = {"location":location}
    headers = {'X-API-KEY': '632985c9646a0bc8f547f1d9'}
    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()
    geocode = response.json()
    st.write(geocode)
    #lon = geocode['results'][0]['geometry']['location']['lng']
    #lat = geocode['results'][0]['geometry']['location']['lat']










