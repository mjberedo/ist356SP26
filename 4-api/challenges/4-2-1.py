#For this challenge, use Azure entity recognition API to extract entities from the following text.

"The Dallas Cowboys are a far better team than the New York Giants this year. The Giants have not won a conference game yet."

#Using the API output, print each extracted entity and its type.

import requests

'''
curl -X 'POST' \
  'https://cent.ischool-iot.net/api/azure/entityrecognition' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'text=The%20Dallas%20Cowboys%20are%20a%20far%20better%20team%20than%20the%20New%20York%20Giants%20this%20year.%20The%20Giants%20have%20not%20won%20a%20conference%20game%20yet.'
'''

apikey = 'c53fc19d90f8ab0541886d4f'
url = 'https://cent.ischool-iot.net/api/azure/entityrecognition'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-API-Key': apikey
}
data = {
    'text': 'The Dallas Cowboys are a far better team than the New York Giants this year. The Giants have not won a conference game yet.'
}
response = requests.post(url, headers=headers, data=data)
response.raise_for_status()
results = response.json()
entities = results['results']['documents'][0]['entities']
for entity in entities:
    print(f"Entity: {entity['text']}, Type: {entity['category']}")
