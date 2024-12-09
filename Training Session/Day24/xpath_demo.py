import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Type username and password
driver.get("https://www.wikipedia.org")
driver.implicitly_wait(5)

search_box = driver.find_element(By.XPATH, """//input[@id='searchInput']""")
search_box.send_keys("India")
search_box.send_keys(Keys.RETURN)

time.sleep(5)
driver.quit()
