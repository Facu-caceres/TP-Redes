import json
import requests
api_url = "http://localhost:58001/api/v1/network-device"

headers={"X-Auth-Token": "NC-5-a4edda6d7ba54b8e8fc0-nbi"}

resp = requests.get(api_url, headers=headers)

print("Request status: ", resp.status_code)

response_json = resp.json()
print()
print()
print (response_json)
print()
print()
networkDevices = response_json["response"]

for networkDevice in networkDevices:
    if networkDevice["collectionStatus"] == "Managed":
        print(networkDevice["hostname"], "\t", networkDevice["platformId"], "\t", networkDevice["managementIpAddress"])
