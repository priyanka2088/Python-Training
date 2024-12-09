import requests
from bs4 import BeautifulSoup

URL = "https://example.com"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")
print(soup)

# Find
h1_tag = soup.find("h1")
if h1_tag:
    print(h1_tag.text)

links = soup.find_all("a")
for link in links:
    print(link.get("href"))

paragraphs = soup.find_all("p")
for para in paragraphs:
    print(para.text)
