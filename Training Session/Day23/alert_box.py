import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Type username and password
driver.get("https://www.demo.guru99.com/test/delete_customer.php")

search_box_username = driver.find_element(By.NAME, "cusid")
search_box_username.send_keys("priyanka2088/pgm")
search_box_username.send_keys(Keys.RETURN)

# Handling alert
alert = driver.switch_to.alert
print(f"Alert text: {alert.text}")
alert.accept()

search_box_username.send_keys(Keys.RETURN)

time.sleep(5)
driver.quit()
