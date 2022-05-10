from http.client import responses
import requests
import json


response = requests.get("https://api.covid19api.com/countries")

# Serializing json
json_object = json.dumps(response.text, indent=4)

# Writing to sample.json

with open("sample.json", "w") as outfile:
    outfile.write(json_object)
