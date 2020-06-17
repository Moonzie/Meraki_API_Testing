import requests
import json
import meraki_api_key

api_key = meraki_api_key.my_key()
url = 'https://api.meraki.com/api/v0/organizations'

header = {"X-Cisco-Meraki-API-Key": api_key, "Content-Type": "application/json"}
#payload = {"enabled":"false"}

org_list = requests.get (url, headers = header) #data = json.dumps(payload))

#response = requests.get(url, headers = header)

print (org_list) #response code
print (org_list.text) #json response



