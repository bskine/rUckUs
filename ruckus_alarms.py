import requests
from pprint import *
import datetime

url = "https://136.226.130.97:8443/wsg/api/public/v8_2/alert/alarm/list?serviceTicket=ST-80-pb29SiHzCpOf3QiejVTV-Ruckus-One"

payload = "{\r\n  \"filters\": [\r\n    {\r\n      \"type\": \"ZONE\",\r\n      \"value\": \"e7c5e1cf-abc2-445c-abc8-ba0a6d0982f8\",\r\n      \"operator\": \"eq\"\r\n    }\r\n  ]\r\n} "
headers = {
  'Content-Type': '[application/json;charset=UTF-8',
  'Authorization': 'Basic cGJveW50bzpBbHBpbmU0OTExIQ==',
  'Cookie': 'JSESSIONID=882B3E8477E1730E7439B2BF6066FFFE'
}

response = requests.request("POST", url, headers=headers, data = payload, verify=False)
x = response.json()
#pprint(x)
#  x is dictionary
y = (x['list'])
# y is now a list of dicts
for i in y:
    q = int(i["insertionTime"]/1000)
    alarm_time = datetime.datetime.fromtimestamp(int(q))    
    print('-'*50)
    print(alarm_time)
    print(i["activity"])
