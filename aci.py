import json
import requests

class APIC():

    cookie = None
    cookiestring = None
    session = None

    def __init__(self, ip, user, password):
        self.ip = "https://"+ip
        self.user = user
        self.password = password
        self.generateCookie()
        self.generateCookiestring()
        
    def generateCookie(self):
        # get the token
        self.session = requests.Session()
        r = self.session.post(self.ip+'/api/aaaLogin.json', json={"aaaUser":{"attributes":{"name":self.user,"pwd":self.password}}}, verify=False)
        r_json = r.json()
        token = r_json["imdata"][0]["aaaLogin"]["attributes"]["token"] 
        self.cookie =  {'APIC-cookie':token}

    def generateCookiestring(self):
        # get the token
        r = requests.post(self.ip+'/api/aaaLogin.json', json={"aaaUser":{"attributes":{"name":self.user,"pwd":self.password}}}, verify=False)
        r_json = r.json()
        token = r_json["imdata"][0]["aaaLogin"]["attributes"]["token"]
        self.cookiestring =  {'APIC-cookie='+token}
    
    def getCookie(self):
        return self.cookie

    def getSession(self):
        return self.session
