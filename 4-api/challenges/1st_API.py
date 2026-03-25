import requests
import json 
import pandas as pd

url = "https://cent.ischool-iot.net/api/funnyname/random"
querystring = {"n":"3"}
response = requests.get(url, params=querystring)
response.raise_for_status() # check if the request was successful, if not it will raise an error and stop the program
names = response.json() # create a python object from the json response
print(names) #list of dicts with funny names and their ids
for name in names:
    print(name['first'], name['last']) # print just the funny name from each dict
