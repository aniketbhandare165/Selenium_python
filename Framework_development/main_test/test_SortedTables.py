
from selenium.webdriver.common.by import By

def test_sort(browserInstance):
    driver = browserInstance
    BrowserSortedveggieList = []
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    driver.maximize_window()

    # click on column header
    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
    # collect all veggie names --> BrowserSortedveggieList(A,B,C)

    veggieWebelements = driver.find_elements(By.XPATH, "//tbody/tr/td[1]")
    for ele in veggieWebelements:
        BrowserSortedveggieList.append(ele.text)
    originalBrowserSortedlist = BrowserSortedveggieList.copy()
    # sort this BrowserSortedveggieList --> newSortedList --> (A,B,C)
    BrowserSortedveggieList.sort()
    # BrowserSortedveggieList == newSortedList
    assert BrowserSortedveggieList == originalBrowserSortedlist