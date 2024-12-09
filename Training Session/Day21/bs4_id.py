import requests
from bs4 import BeautifulSoup

URL = "https://www.w3schools.com/html/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

headers = soup.find(id="getdiploma")
print(headers.text.strip())
