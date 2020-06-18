import requests
import json
import meraki_api_key

api_key = meraki_api_key.my_key()
url = 'https://api.meraki.com/api/v0/organizations'

header = {"X-Cisco-Meraki-API-Key": api_key, "Content-Type": "application/json"}
#payload = {"enabled":"false"}

get_command = requests.get (url, headers = header) #data = json.dumps(payload))
command = get_command.json()

print (get_command.response_code) #response code
print (command) #json response



