import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Type username and password
driver.get("https://www.github.com/login")

search_box_username = driver.find_element(By.ID, "login_field")
search_box_username.send_keys("priyanka2088/pgm")

search_box_password = driver.find_element(By.ID, "password")
search_box_password.send_keys("mypass")

search_box_username.send_keys(Keys.RETURN)

driver.implicitly_wait(5)

# Get links
driver.get("https://en.wikipedia.com/wiki/india")

tags = driver.find_elements(By.TAG_NAME, "a")

for link in tags:
    print("Link: ", link.text)

driver.implicitly_wait(5)

# Get data by link text
driver.get("https://en.wikipedia.com/wiki/india")

link = driver.find_element(By.LINK_TEXT, "Zoroastrianism")

print("Data: ", link.text)
driver.get(link.get_attribute("href"))  # Goto

driver.implicitly_wait(5)

print(f"Title: {driver.title}")
time.sleep(5)
driver.quit()
