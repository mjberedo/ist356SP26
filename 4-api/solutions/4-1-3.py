'''
Geocodes 

curl -X 'GET' \
  'https://cent.ischool-iot.net/api/google/geocode?location=syracuse%20ny' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: 632985c9646a0bc8f547f1d9'
  
  
  
  Weather
  
curl -X 'GET' \
  'https://cent.ischool-iot.net/api/weather/current?units=imperial%20&lon=76.1474&lat=43.0495' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: 632985c9646a0bc8f547f1d9'


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
  querystring = {"location": location}
  headers = {'X-API-KEY': '632985c9646a0bc8f547f1d9'}
  response = requests.get(url, headers=headers, params=querystring)
  response.raise_for_status() 
  geocode = response.json()
  #st.write(geocode)
  lon = geocode['results'][0]['geometry']['location']['lng']
  lat = geocode['results'][0]['geometry']['location']['lat']
  
  
  url1 = "https://cent.ischool-iot.net/api/weather/current"
  querystring1 = {"units": "imperial", "lon": lon, "lat": lat}
  response1 = requests.get(url1, headers=headers, params=querystring1)
  response1.raise_for_status()
  weather = response1.json()
  temp = weather['current']['temperature_2m']
  #humidity
  st.metric(label="Current Temperature (F)", value=temp)








