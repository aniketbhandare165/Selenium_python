import os
import sys



sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.login import LoginPage
from pageObjects.shopPage import ShopPage


def test_e2e(browserInstance):
    driver = browserInstance
    # driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    # loginpage = LoginPage(driver)
    # shop_page = loginpage.login()
    driver.get("https://rahulshettyacademy.com/angularpractice/shop")
    shop_page = ShopPage(driver)
    shop_page.add_product_to_cart("Blackberry")
    shop_page.goTOCart()

    driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    driver.find_element(By.ID, "country").send_keys("ind")
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
    driver.find_element(By.LINK_TEXT, "India").click()
    driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    successText = driver.find_element(By.CLASS_NAME, "alert-success").text
    assert 'Success! Thank you!' in successText