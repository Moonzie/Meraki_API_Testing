import actions as action


# grabs Organization ID's via API
organization_list = action.get_orgs()
which_org = input("Which organization would you like to run calls against? (enter org id) ")
org_id = organization_list[int(which_org)]

action.get_organization_networks(org_id)
#action.get_uplink_loss_and_latency(org_id)
