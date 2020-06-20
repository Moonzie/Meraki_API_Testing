import actions as action

#dispatcher = {'get_orgs': 'List organizations for this API key'} #dictionary for function and description


organization_list = action.get_orgs()

#for d in dispatcher.keys(): 
#	print(d)

# grabs Organization ID's via API
which_org = input("Which organization would you like to run calls against? (enter number) ")
org_id = organization_list[int(which_org)]

action.get_organization_networks(org_id)


