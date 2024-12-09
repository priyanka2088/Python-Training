import requests
from bs4 import BeautifulSoup

URL = "https://www.python.org"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a", href=True)
for link in links:
    if link["href"].startswith("https://doc"):  
        print(link["href"])
