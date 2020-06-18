import requests
import json
import meraki_api_key

api_key = meraki_api_key.my_key()
base_url = 'https://api.meraki.com/api/v0'
header = {"X-Cisco-Meraki-API-Key": api_key, "Content-Type": "application/json"}

def get_orgs():

	url = f'{base_url}/organizations' #URL 
	get_organizations = requests.get (url, headers = header) #Actual API Call
	organizations = get_organizations.json() #response is loaded as json and saved to variable 
	
	print ('Here is a list of the Organizations: ')
	for o in organizations:  #used to access each entry in the list
		org = o['name']
		print (str(org))

	print (get_organizations.status_code) #response code
	#print (organizations) #json response

def get_uplink_loss_and_latency(org_id):
	organization = org_id
	url = f'{base_url}/organizations/{organization}/uplinksLossAndLatency'
	get_uplinksLossAndLatency = requests.get (url, headers = header)
	uplinksLossAndLatency = get_uplinksLossAndLatency.json()


	print(uplinksLossAndLatency)
	#print(get_uplinksLossAndLatency.text) #respons, not loaded as json


#get_orgs()
get_uplink_loss_and_latency(838073)


#payload = {"enabled":"false"}

 #data = json.dumps(payload))

#response = requests.get(url, headers = header)





