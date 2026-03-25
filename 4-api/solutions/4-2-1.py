'''
Post curl here
curl -X 'POST' \
  'https://cent.ischool-iot.net/api/azure/entityrecognition' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: 'your own key' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'text=pizza%20is%20good%20not%20customer%20service'


'''



import pandas as pd
import numpy as np
import streamlit as st
import requests
import json 


def extract_entities(text:str) -> dict:
  '''Extract entities from text using Azure Entity Recognition API.'''

#Complete function
    url = "https://cent.ischool-iot.net/api/azure/entityrecognition"
    headers = {
        "accept": "application/json",
        "X-API-KEY": "your own key}


# Create a dashboard using Streamlit to test the function
st.title("Azure Entity Recognition")

