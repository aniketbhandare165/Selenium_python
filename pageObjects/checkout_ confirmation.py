from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Checkout_confirmation:
    def __init__(self,driver):
        self.driver = driver
        self.checkout_button = (By.XPATH, "//button[@class='btn btn-success']")
        self.country_input = (By.ID, "country")
        self.country_option = (By.LINK_TEXT, "India")
        self.checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.submit_button = (By.XPATH, "//input[@type='submit']")
    def checkout(self):

    def enter_delivery_address(self):
        self.driver.find_element(*self.checkout_button).click()
        self.driver.find_element(*self.country_input).send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(*self.country_option))
        self.driver.find_element(*self.country_option).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit_button).click()

    def validate_order(self):
