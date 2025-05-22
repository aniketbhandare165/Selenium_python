import time

from selenium import webdriver
from selenium.webdriver.common.by import By

name = "rahul"
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alerttext = alert.text
print(alerttext)
alert.accept()
assert name in alerttext
# alert.dismiss()
time.sleep(2)
