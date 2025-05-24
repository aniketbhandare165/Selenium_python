import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
time.sleep(2)
vegetables = driver.find_elements(By.XPATH,"//div[@class='products']/div") #list
count = len(vegetables)
assert count > 0
for vegetable in vegetables:
    # driver.find_element(By.XPATH,"//div[@class='product']/descendant::button[normalize-space()='ADD TO CART']")
    vegetable.find_element(By.XPATH,"div/button").click()
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.XPATH,"//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[normalize-space()='Apply']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[@class='promoInfo']")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

#Sum validations
prices = driver.find_elements(By.XPATH,"//td[5]/p[@class ='amount']")
sum = 0
for price in prices:
    sum = sum + int(price.text)
print(sum)
totalAmount = int(driver.find_element(By.XPATH,"//span[@class ='totAmt']").text)
assert sum == totalAmount

discount_amt = float(driver.find_element(By.XPATH,"//span[@class='discountAmt']").text)
orig_amt = int(driver.find_element(By.XPATH,"//span[@class='totAmt']").text)
assert discount_amt < orig_amt

driver.back()
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
time.sleep(2)
Expected_list = ["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]
runtime_list = []
sample_list = driver.find_elements(By.XPATH,"//div[@class='products']/descendant::h4")
for element in sample_list:
    runtime_list.append(element.text)
print(runtime_list)
assert Expected_list == runtime_list
# Expected_list = [""]