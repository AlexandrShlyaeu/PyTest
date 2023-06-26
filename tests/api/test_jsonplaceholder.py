from pages.StartPage import StartPage
from tests.api.test_base_api import BaseTest
from config.config import Config
import pytest
import allure
import requests

@allure.feature('Page verification')
@pytest.mark.regression
class TestStartPage(BaseTest):

    @pytest.mark.smoke
    @pytest.mark.api
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story('Test JSON Placeholder')
    def test_health_check(self):
        try:
            print(Config.API_ENDPOINT+"post/1")
            response = requests.get(Config.API_ENDPOINT+"posts/1")
            print(response)
            assert response.status_code == 200
        except:
            print("Error")

