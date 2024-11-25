import pandas as pd
import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:
    print("Success")
else:
    print("Error", response.status_code)

print(pd.DataFrame(response.json()))
