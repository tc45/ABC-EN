"""This script validates the OSPFv3 configuration"""
import requests
import urllib3

urllib3.disable_warnings()

URL = "https://core-rtr4:443/restconf/data/Cisco-IOS-XE-native:native/router/"\
      "Cisco-IOS-XE-ospfv3:ospfv3"

headers = {
    "accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

response = requests.request("GET",
                            URL,
                            auth=("developer", "1234QWer!"),
                            headers=headers,
                            verify=False,
                            timeout=60)

print(response.status_code)
print(response.json())
