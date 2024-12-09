import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://en.wikipedia.com/wiki/india")
driver.save_screenshot("sample.png")

driver.implicitly_wait(5)

print(f"Title: {driver.title}")
time.sleep(5)
driver.quit()
