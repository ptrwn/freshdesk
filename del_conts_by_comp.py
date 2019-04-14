import requests
import json
from sys import argv
from crdz import domain, api_key, password

c_id = int(argv[1])

r = requests.get("https://"+ domain +".freshdesk.com/api/v2/contacts?company_id={}".format(c_id), auth = (api_key, password))
#print(json.loads(r.content))

for item in json.loads(r.content):
    r = requests.delete("https://" + domain + ".freshdesk.com/api/v2/contacts/{}/hard_delete?force=true".format(item['id']),
                    auth=(api_key, password))

r = requests.delete("https://" + domain + ".freshdesk.com/api/v2/companies/{}/".format(c_id),
                    auth=(api_key, password))
