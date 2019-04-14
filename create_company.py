import requests
import json
from crdz import domain, api_key, password, headers
from random import choice, randint


class Contact:
    def __init__(self):
        # getting a random line from almost 8k first names
        with open('data/f_names.txt') as in_fd:
            rname = next(in_fd)
            for i, line in enumerate(in_fd, start=1):
                j = randint(0, i)
                if j == 0:
                    rname = line
        self.fname = rname.strip()

        with open('data/l_names.txt', 'r') as f:
            lines = f.readlines()[0].split(', ')
        self.lname = choice(lines)

    def Name(self):
        return self.fname + " " + self.lname

    def Email(self, domain):
        return "{}.{}@{}".format(self.fname, self.lname, domain)


class Company(Contact):
    pass




comp_info = json.loads(open('data/companies.txt').read())
for item in comp_info:
    #print(item["name"], item["account_tier"], item["health_score"])
    r = requests.post("https://" + domain + ".freshdesk.com/api/v2/companies", auth=(api_key, password), data=json.dumps(item), headers=headers)
    print('got this back', json.loads(r.content))
    new_comp_id = json.loads(r.content)['id']

    for i in range(10):
        cont = Contact()
        contact_info = {
            "name": cont.Name(),
            "email": cont.Email(item["domains"][0]),
            "company_id": new_comp_id
            }
        r = requests.post("https://"+ domain +".freshdesk.com/api/v2/contacts", auth = (api_key, password), data = json.dumps(contact_info), headers = headers)
        print('got this back', json.loads(r.content))
