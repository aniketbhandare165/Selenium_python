from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element(By.XPATH,"//div[@aria-label='Close']").click()
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I am able to automate frames")
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME,"h3").text)
