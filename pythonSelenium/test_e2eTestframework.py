import os
import sys

# from Selenium.pageObjects import checkoutConfirmation

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.login import LoginPage
from pageObjects.shopPage import ShopPage
from pageObjects.checkoutConfirmation import CheckoutConfirmation


def test_e2e(browserInstance):
    driver = browserInstance
    # driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    # loginpage = LoginPage(driver)
    # shop_page = loginpage.login()
    driver.get("https://rahulshettyacademy.com/angularpractice/shop")
    shop_page = ShopPage(driver)
    shop_page.add_product_to_cart("Blackberry")
    shop_page.goTOCart()
    checkoutConfirmation.checkout()
    checkoutConfirmation.enter_delivery_address("ind")
    checkoutConfirmation.validate_order()

