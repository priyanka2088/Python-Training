import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")


master_class = soup.find(class_="quote")
quote_obj = master_class.find(class_="text")  
author_obj = master_class.find(class_="author")  

print(f"{quote_obj.text.strip()}\n{author_obj.text.strip()}")

quote_obj = soup.select(".quote .text")
author_obj = soup.select(".quote .author")

for quote, author in zip(quote_obj, author_obj):    
    print(f"{quote.text.strip()} - {author.text.strip()}\n")

    
    with open("quotes.txt", "a") as file:
        file.write(f"{quote.text.strip()} - {author.text.strip()}\n")
