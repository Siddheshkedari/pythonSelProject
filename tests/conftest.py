import pytest

from selenium import webdriver


from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


#command line terminal browser
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )



@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        service_obj = Service()
        driver = webdriver.Chrome(service=service_obj)

    elif browser_name == "firefox":
        service_obj = Service()
        driver = webdriver.Firefox(service=service_obj)

    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")#


    request.cls.driver = driver  #driver object send request to the class object.
    yield
    driver.close()