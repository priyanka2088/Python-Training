import requests
from requests.auth import HTTPBasicAuth

url = "https://httpbin.org//basic-auth/user/pass"
authentication = HTTPBasicAuth("user", "pass")

response = requests.get(url, auth=authentication)

if response.status_code == 200:
    print("Success", response.json())
else:
    print("Error!", response.status_code)