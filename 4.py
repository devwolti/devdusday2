import requests
import json

"""
    1. get VLANs from Switch, as done in 2.py
    2. Connect to APIC as done in 3
    3. Create Tenant, VRF, AP
    4. Crate BDs/EPGs with VLAN names

"""

#get VLANs from Switch

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

#done

#connect to APIC

ip = "198.18.133.200"
user = "admin"
password = "C1sco12345"

tenant_name = "Daniel"
ap_name = "Devnet"

session = requests.Session()
session.post('https://'+ip+'/api/aaaLogin.json', json={"aaaUser":{"attributes":{"name":user,"pwd":password}}}, verify=False)

# done

#create tenant,VRF,AP

tenant = session.post('https://'+ip+'/api/node/mo/uni.json', json={"fvTenant":{"attributes":{"descr":"","dn":"uni/tn-"+tenant_name,"name":tenant_name,"ownerKey":"","ownerTag":""},"children":[]}},verify=False)
vrf = session.post('https://'+ip+'/api/node/mo/uni/tn-'+tenant_name+'.json', json={"fvCtx":{"attributes":{"descr":"","dn":"uni/tn-"+tenant_name+"/ctx-"+ap_name,"knwMcastAct":"permit","name":ap_name,"ownerKey":"","ownerTag":"","pcEnfDir":"ingress","pcEnfPref":"enforced"},"children":[]}},verify=False)
ap = session.post('https://'+ip+'/api/node/mo/uni/tn-'+tenant_name+'.json', json={"fvAp":{"attributes":{"dn":"uni/tn-"+tenant_name+"/ap-"+ap_name,"name":ap_name,"rn":"ap-DoC","status":"created"},"children":[]}},verify=False)

#done

#create BDs, EPGs

for vlan in response["result"]["body"]["TABLE_vlanbriefxbrief"]["ROW_vlanbriefxbrief"]:

    epg_name = "EPG_"+vlan["vlanshowbr-vlanid"]
    bd = session.post('https://'+ip+'/api/node/mo/uni/tn-'+tenant_name+'.json', json={"fvBD":{"attributes":{"dn":"uni/tn-"+tenant_name+"/BD-"+epg_name,"name":epg_name,"rn":"BD-"+epg_name,"status":"created"},"children":[{"fvRsCtx":{"attributes":{"tnFvCtxName":ap_name,"status":"created,modified"},"children":[]}}]}},verify=False)
    epg = session.post('https://'+ip+'/api/node/mo/uni/tn-'+tenant_name+'/ap-'+ap_name+'/epg-'+epg_name+'.json', json={"fvAEPg":{"attributes":{"dn":"uni/tn-"+tenant_name+"/ap-"+ap_name+"/epg-"+epg_name,"name":epg_name,"rn":"epg-"+epg_name,"status":"created"},"children":[{"fvRsBd":{"attributes":{"tnFvBDName":epg_name,"status":"created,modified"},"children":[]}}]}},verify=False)

#done