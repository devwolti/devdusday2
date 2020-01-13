import requests
import json

"""
    1. Create Session to APIC
    2. Query Tenants
    3. List tenants

"""

ip = "198.18.133.200"
user = "admin"
password = "C1sco12345"

session = requests.Session()
session.post('https://'+ip+'/api/aaaLogin.json', json={"aaaUser":{"attributes":{"name":user,"pwd":password}}}, verify=False)

tenantlist = session.get('https://'+ip+'/api/node/class/fvTenant.json?query-target-filter=not(wcard(fvTenant.dn,%22__ui_%22))',  verify=False)

for tn in tenantlist.json()['imdata']:
    print(tn["fvTenant"]["attributes"]["name"])