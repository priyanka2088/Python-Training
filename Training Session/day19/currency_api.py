import datetime

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("CURRENCY_API_KEY")

URL = "https://api.exchangerate.host/live?access_key=" + API_KEY
params = {"base": "USD"}

response = requests.get(URL, params)

if response.status_code == 200:
    quotes = response.json()["quotes"]
    filename = f"exchange_rates_{datetime.date.today()}.json"

    with open(filename, "w") as file:
        json.dump(quotes, file)  # Dumping all data to file as JSON
    print("Data dumped in file.")
