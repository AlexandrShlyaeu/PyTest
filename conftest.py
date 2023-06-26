from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest


@pytest.fixture(scope="class")
def init_driver (request, browser="chrome"):
    if browser == "chrome":
        options = Options()
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(options=options, service=service)
    elif browser == "firefox":
        options = Options()
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(options=options, service=service)
    elif browser == "edge":
        options = Options()
        service = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(options=options, service=service)
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption (parser):
    parser.addoption("--browser")



@pytest.fixture(scope="class", autouse=True)
def browser (request):
    return request.config.getoption("--browser")