import requests
import json
import meraki_api_key

api_key = meraki_api_key.my_key()
base_url = 'https://api.meraki.com/api/v0'
header = {"X-Cisco-Meraki-API-Key": api_key, "Content-Type": "application/json"}

def get_orgs():
	org_id_list =[]
	counter = 0

	url = f'{base_url}/organizations' #URL 
	get_organizations = requests.get (url, headers = header) #Actual API Call
	organizations = get_organizations.json() #response is loaded as json and saved to variable 
	
	print ('Here is a list of the Organizations: ')
	for o in organizations:  #used to access each entry in the list
		organization_name = o['name']
		organization_id = o['id']
		print (str (counter) + " - " + str(organization_name) + " (id:"+ str(organization_id) +")")
		counter += 1
		org_id_list.append(organization_id)

	print (get_organizations.status_code) #response code
	#print (organizations) #json response
	#print (org_id_list) #json response
	return (org_id_list)


def get_organization_networks(org_id):
	organization = org_id
	counter = 0 

	url = f'{base_url}/organizations/{organization}/networks' #URL 
	get_networks = requests.get (url, headers = header) #Actual API Call
	networks = get_networks.json() #response is loaded as json and saved to variable 
	
	print ("Networks: ")
	for n in networks: 
		counter += 1 
		print(n['name'] + " - " + n['id'])

def get_uplink_loss_and_latency(org_id):
	organization = org_id
	url = f'{base_url}/organizations/{organization}/uplinksLossAndLatency'
	get_uplinksLossAndLatency = requests.get (url, headers = header)
	uplinksLossAndLatency = get_uplinksLossAndLatency.json()

	for lines in uplinksLossAndLatency: 
		for k, v in lines.items(): 

			if k == 'timeSeries':
				print (str(k) + " : ")
				print (pretty(v))
			else: 
				print (str(k) + " : " + str(v))
	#print(uplinksLossAndLatency)
	
def pretty(json_response):
	pretty_print = json.dumps(json_response, indent=4, sort_keys=True)
	return pretty_print


#pretty(get_orgs())
#get_uplink_loss_and_latency(838073)



#payload = {"enabled":"false"}
#data = json.dumps(payload))
#response = requests.get(url, headers = header)





