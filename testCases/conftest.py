import pytest
import selenium.webdriver.chrome
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print("Test run chrome")
        driver = webdriver.Chrome()
    elif browser == "edge":
        print("Test run Edge")
        driver = webdriver.Edge()
    else:
        print("Test run in Headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://bankapp.credence.in/login.html")
        yield driver
        driver.quit()


@pytest.fixture(params=[
        ("Chetna1", "Netra@123", "Login_pass"),
        ("Chetna2", "Netra@123", "Login_fail"),
        ("Chetna1", "Netra", "Login_fail"),
        ("Chetna2", "Netra", "Login_fail")
])
def GetDataForLogin(request):
    return request.param
