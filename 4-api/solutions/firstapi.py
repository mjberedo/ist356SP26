'''
curl -X 'GET' \
  'https://cent.ischool-iot.net/api/funnyname/random?n=3' \
  -H 'accept: application/json'

'''

import requests
import json

url = 'https://cent.ischool-iot.net/api/funnyname/random'
querystring = {"n":"3"}
response = requests.get(url, params=querystring)
response.raise_for_status() # check if the request was successful, if not it will raise an error
names = response.json() # create a python object from the json response
#print(names) # list of dicts, each dict has keys 'first' and 'last'
for name in names:
    print(name['first'], name['last'])
