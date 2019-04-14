import requests
import json
from crdz import domain, api_key, password, headers

def create_groups():
    new_group_ids = []

    for i in range(4):
        group_info = {
            "name": "Team{}".format(i),
            "description": "Support team #{}".format(i)
        }
        #create groups, get group IDs
        r = requests.post("https://" + domain + ".freshdesk.com/api/v2/groups", auth=(api_key, password), data=json.dumps(group_info), headers=headers)
        new_group_ids.append(json.loads(r.content)['id'])

    return (new_group_ids)

def get_groups():
    groups = []
    r = requests.get("https://" + domain + ".freshdesk.com/api/v2/groups", auth=(api_key, password), headers=headers)
    groups = json.loads(r.content)
    return groups

def delete_groups(ids):
    for grid in ids:
        r = requests.delete("https://" + domain + ".freshdesk.com/api/v2/groups/{}/".format(grid),
                            auth=(api_key, password))

def get_roles_prods():
    # get roles
    r = requests.get("https://" + domain + ".freshdesk.com/api/v2/roles/", auth=(api_key, password))
    roles = json.loads(r.content)
    for role in roles:
        print(role['id'], role['name'])

    # get products
    r = requests.get("https://" + domain + ".freshdesk.com/api/v2/products/", auth=(api_key, password))
    products = json.loads(r.content)
    for product in products:
        print(product['id'], product['name'])


# create skills, as well  -- sme,
# skills can be imported ^_____^ - generate a .CSV and put it there

# create contacts
def create_cont():
    contact_info = {
            "name": "Example3 Contact3",
            "email": "email3@1374688.com"
            }
    r = requests.post("https://"+ domain +".freshdesk.com/api/v2/contacts", data = json.dumps(contact_info), auth = (api_key, password), headers = headers)
    print('got this back', json.loads(r.content)['id'])
    ag_id = json.loads(r.content)['id']
    return  ag_id

agent = create_cont()

# make them agents
agent_data = {
    "occasional": False,
    "ticket_scope": 1,
    "group_ids": create_groups()
}
r = requests.put("https://"+ domain +".freshdesk.com/api/v2/contacts/{}/make_agent".format(agent),auth = (api_key, password), data = json.dumps(agent_data), headers = headers)
print('got this back', json.loads(r.content))
