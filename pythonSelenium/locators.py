import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
#locators ,xpath ,css selector, id, Name, linktext
print(driver.title)
print(driver.current_url)
driver.find_element(By.NAME, "email").send_keys("rahulshetty@123")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("zaq12wsx")
driver.find_element(By.ID, "exampleCheck1").click()

# xpath //tagname[@attribute='value'] -> //input[@type='submit']
# css tagname[attribute='value'] -> input[type='submit'], #id -> #inputRadio1, .classname

#Static dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female")
# dropdown.select_by_value()

driver.find_element(By.CSS_SELECTOR, "input[name=name]").send_keys("Rahul")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "success" in message
driver.find_element(By.XPATH,"(//input[@name ='name'])[2]").send_keys("hello Aniket")
driver.find_element(By.XPATH, "(//input[@name ='name'])[2]").clear()
time.sleep(2)