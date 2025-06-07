import json
# import os
import sys

import pytest



# test_data_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'test_e2eTestframework.json')
# test_data_path = os.path.abspath(test_data_path)
sys.path.append(r"D:\New_project_3")
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Selenium_project.Framework_development.pageObjects.shopPage import ShopPage
# from Selenium_project.Framework_development.pageObjects.login import LoginPage
# from pageObjects.shopPage import ShopPage
test_data_path = '../data/test_e2eTestframework.json'
with open(test_data_path) as f:
    testdata = json.load(f)
    test_list = testdata['data']

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item",test_list)
def test_e2e(browserInstance,test_list_item):
    driver = browserInstance
    # driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    # loginpage = LoginPage(driver)
    # print(loginpage.getTitle())
    # shop_page = loginpage.login(test_list_item["userEmail"],test_list_item["userPassword"])
    driver.get("https://rahulshettyacademy.com/angularpractice/shop")
    shop_page = ShopPage(driver)
    print(shop_page.getTitle())
    shop_page.add_product_to_cart(test_list_item["productName"])
    checkout_page = shop_page.goTOCart()
    checkout_page.checkout()
    checkout_page.enter_delivery_address("ind")
    checkout_page.validate_order()


