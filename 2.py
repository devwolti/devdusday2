import requests
import json

"""
    1. activate the api feature the switch
        conf t
            feature nxapi
    2. access webgui
    3. enter "show vlan brief" in the form. Choose json-rpc -> cli from the options on the right
    4. click post
    5. examine output
    6. click python and copy paste code
    7. edit code to match creds
    8. print vlans from returned json

"""

import requests
import json

"""
Modify these please
"""
url='http://198.18.134.140/ins'
switchuser='admin'
switchpassword='C1sco12345'

myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show vlan brief",
      "version": 1
    },
    "id": 1
  }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()


for vlan in response["result"]["body"]["TABLE_vlanbriefxbrief"]["ROW_vlanbriefxbrief"]:
    print(vlan["vlanshowbr-vlanid"])


