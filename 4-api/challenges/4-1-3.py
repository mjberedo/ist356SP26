## Challenge 4-1-3

#Weather Example

#Figure out how to call these in the IoT portal:
#- Google geocode API to take a location and get a latitute and longitude
#- #Weather API to get the weather for a latitude and longitude

#Write a streamlit to input a location and return the current weather conditions. Use the `st.metric` to display the temperature and humidity with units. e.g. 56°F and 80% humidity.

from altair import Key
import streamlit as st
import requests


#curl -X 'GET' \
  #'https://cent.ischool-iot.net/api/google/geocode?location=Syracuse' \
  #-H 'accept: application/json'
#-H 'X-API-Key: c53fc19d90f8ab0541886d4f'

import streamlit as st

import json
import requests

st.title("Weather App")
location = st.text_input("Enter a location to get the current weather conditions:")
if st.button("Get Weather"):

    url = "https://cent.ischool-iot.net/api/google/geocode"
    querystring = {"location": location}
    headers = {"X-API-Key": "c53fc19d90f8ab0541886d4f"}
    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()
    geocode = response.json()
    st.write(geocode)

    lon = geocode["results"][0]["geometry"]["location"]["lng"]
    lat = geocode["results"][0]["geometry"]["location"]["lat"]

    url1 = "https://cent.ischool-iot.net/api/weather/current"
    querystring1 = {"units": "imperial", "lon": lon, "lat": lat}
    response1 = requests.get(url1, headers=headers, params=querystring1)
    response1.raise_for_status()
    weather = response1.json()
    temp = weather["current"]["temperature_2m"]
    humidity = weather["current"]["relative_humidity_2m"]
    st.metric(label="Current Temperature (F)", value=temp)
    st.metric(label="Current Humidity (%)", value=humidity)