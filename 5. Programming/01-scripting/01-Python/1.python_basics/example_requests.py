# import modules needed
import requests
import json

# send the request and get the response
response = requests.get('https://api.ipify.org?format=json')

# check the response validity
if response.status_code != 200:
    print("Error: Invalid HTTP code: %s" % response.status_code)
else:
    # parse the response
    json_text = json.loads(response.text)
    print(json_text['ip'])