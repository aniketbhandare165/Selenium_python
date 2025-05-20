import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#chrome driver service selenium 160 -> 160 chrome driver

# if you are restricted to vpn or old version you are using you can use this method
# service_obj = Service("D:\Selenium_chrome_drive\chromedriver-win64\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(2)

# driver = webdriver.firefox()
# driver.get("https://rahulshettyacademy.com")
# driver.maximize_window()
# print(driver.title)
# print(driver.current_url)
# time.sleep(2)