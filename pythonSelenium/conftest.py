import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome': #
        driver = webdriver.Chrome()
        driver.implicitly_wait(4)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
        driver.implicitly_wait(4)
    yield driver  #Before test function execution
    driver.close() #post your test function execution
