import actions as action

organization_list = action.get_orgs()

which_org = input("Which organization would you like to run calls against? (enter number) ")
org_id = organization_list[int(which_org)]

print ("\nListing networks for Organization ID: " + org_id )
action.get_organization_networks(org_id)

print ("\nListing Latency and Loss for Organization ID: " + org_id)
action.get_uplink_loss_and_latency(org_id)

