import json 

#Loads json files in to a database
def load_db():

  files = ['1.json', '2.json', '3.json', '4.json', '5.json', '6.json', '7.json', '8.json']

  for file in files:
    with open(file) as f: 
      return json.load(f)

#saves the database into a variable
db = load_db()

#loops through the data to count the number of timestamps

network_alerts = {}

for data in db: 
  time_counter = len(data['timeSeries'])
  timestamps = data['timeSeries']
  timestamp_list = []

  #counts the timestamps and alerts
  if time_counter <= 2: 
    print ("Network ID: " + data['networkId'] + " - ALERT - " + str(time_counter) + " entries found ")
    #print ("This network only has " + str(time_counter) + " entries! ")
    #network_alerts.update({'Network ID': data['networkId'], "timeSeries": data['timeSeries']})

    for t in timestamps:
      timestamp_list.append(t)
      network_alerts[data['networkId']] = timestamp_list
   
  #if the correct number of entries are found, it will print 'OK' and the count
  else:
    print("Network ID: " + data['networkId'] + " - OK - " + str(time_counter) + " entries found")

print (network_alerts.keys())

print ("End of results.")
