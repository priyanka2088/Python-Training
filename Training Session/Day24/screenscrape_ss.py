import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI")
driver.implicitly_wait(5)

chart = driver.find_element(By.ID, "advchart")
driver.implicitly_wait(10)
chart.screenshot("sample.png")

time.sleep(5)
driver.quit()
