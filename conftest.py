import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from config.config import TestData


@pytest.fixture(scope='class')
def init_driver(request):
    options = Options()
    service = Service(TestData.CHROMEDRIVER_PATH)
    # options.add_argument("--headless")
    options.add_argument('--lang=en')
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options, service=service)
    request.cls.driver = browser
    yield browser
    print("\nquit browser..")
    browser.quit()
