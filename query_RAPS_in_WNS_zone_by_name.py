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

url = ("https://136.226.130.97:8443/wsg/api/public/v8_2/query/mesh/"+e+"/topology?serviceTicket="+ service_ticket)

payload = "{\r\n  \"filters\": [\r\n    {\r\n      \"type\": \"ZONE\",\r\n      \"value\": \"e7c5e1cf-abc2-445c-abc8-ba0a6d0982f8\",\r\n      \"operator\": \"eq\"\r\n    }\r\n  ]\r\n}"

headers = {
  'Content-Type': '[application/json;charset=UTF-8',
  'Authorization': 'Basic cGJveW50bzpBbHBpbmU0OTExIQ==',
  'Cookie': 'JSESSIONID=D84F4173A7233F39B1F119F076756839'}

response = requests.request("POST", url, headers=headers, data = payload, verify=False)

x = response.json()

print('-'*125)
print('{:<25}{:<25}{:^25}{:^25}{:^25}'.format('NEIGHBOR NAME', 'MANAGEMENT IP', 'MAC ADDRESS', 'UPLINK RSSI', 'HOPS FROM RAP'))
print('-'*125)
print('\n')

for y in x:
    ip = y["ipAddress"]
    ap_name = y['apName']
    mac = y['apMac']
    rssi = y['uplinkRssi']
    hops = y['hops']
    print('*'*125)
    print('{:<25}{:<25}{:^25}{:^25}{:^25}'.format(ap_name, ip, mac, rssi, hops))
    print('*'*125)
    

