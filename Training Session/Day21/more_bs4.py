import os
import uuid
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://realpython.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


titles = soup.find_all(class_="card-title")
for title in titles:
    print(title.text)
print("\n")


url = "https://worldometers.info/world-population/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table")
rows = soup.find_all("tr")

master_list = []

for row in rows:
    cells = soup.find_all("td")
    data = [cell.text.strip() for cell in cells]
    master_list.append(data)

print(pd.DataFrame(master_list), "\n")


url = "https://unsplash.com/s/photos/nature"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


os.makedirs("images", exist_ok=True)

images = soup.find_all("img", {"srcset": True})
for img in images:
    print(img.get("src"))

   
    image_data = requests.get(img.get("src")).content

    
    with open(f"images/sample_{str(uuid.uuid4())[:8]}.png", "wb") as file:
        file.write(image_data)
