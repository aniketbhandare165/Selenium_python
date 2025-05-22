import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
time.sleep(2)
vegetables = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(vegetables)
assert count > 0
for vegetable in vegetables:
    # driver.find_element(By.XPATH,"//div[@class='product']/descendant::button[normalize-space()='ADD TO CART']")
    vegetable.find_element(By.XPATH,"div/button").click()
