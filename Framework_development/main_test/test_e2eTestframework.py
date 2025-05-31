import json

import pytest

from Selenium.Framework_development.pageObjects.shopPage import ShopPage
test_data_path = '../data/test_e2eTestframework.json'
with open(test_data_path) as f:
    testdata = json.load(f)
    test_list = testdata['data']

@pytest.mark.parametrize("test_list_item",test_list)
def test_e2e(browserInstance,test_list_item):
    driver = browserInstance
    # driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    # loginpage = LoginPage(driver)
    # shop_page = loginpage.login(test_list_item["userEmail"],test_list_item["userPassword"])
    driver.get("https://rahulshettyacademy.com/angularpractice/shop")
    shop_page = ShopPage(driver)
    shop_page.add_product_to_cart(test_list_item["productName"])
    checkout_page = shop_page.goTOCart()
    checkout_page.checkout()
    checkout_page.enter_delivery_address("ind")
    checkout_page.validate_order()


