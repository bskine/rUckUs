import requests
from pprint import *
import datetime
import ap_list

d = (input("Which ap(MAP) are we looking at?"))
e = ap_list.ap_list[d]

### disables InsecureRequestWarning 
requests.packages.urllib3.disable_warnings()

url_init = "https://136.226.130.97:8443/wsg/api/public/v8_2/serviceTicket"

payload = "{\r\n  \"username\": \"pboynto\",\r\n  \"password\": \"Alpine4911!\"\r\n}"
headers = {
  'Authorization': 'Basic cGJveW50bzpBbHBpbmU0OTExIQ==',
  'Content-Type': 'text/plain',
  'Cookie': 'JSESSIONID=7AD94AB1886B4C505459FF72DB5ADA50'}

reply = requests.request("POST", url_init, headers=headers, data = payload, verify=False)
r = reply.json()

service_ticket = r['serviceTicket']


url = ("https://136.226.130.97:8443/wsg/api/public/v8_2/aps/"+e+"/operational/neighbor?serviceTicket="+ service_ticket)

payload = {}
headers = {
  'Content-Type': '[application/json;charset=UTF-8',
  'Authorization': 'Basic cGJveW50bzpBbHBpbmU0OTExIQ==',
  'Cookie': 'JSESSIONID=89882A0E8E0EFD3E01622C0B3FDAB755'}

response = requests.request("GET", url, headers=headers, data = payload, verify=False)

x = response.json()
##  x is dictionary
y = (x['list'])
## y is now a list of dicts
for i in y:
    ip = i["externalIp"]
    ap_name = i['name']
    mac = i['mac']
    rssi = i['signal']
    print('-'*50)
    print([ap_name, ip, mac, rssi])
   

