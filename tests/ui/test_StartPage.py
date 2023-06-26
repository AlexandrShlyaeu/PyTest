from pages.StartPage import StartPage
from tests.ui.test_base_ui import BaseTest
import pytest
import allure
from data.TestData import TestData


@allure.feature('Page verification')
@pytest.mark.regression
class TestStartPage(BaseTest):

    @pytest.mark.smoke
    @pytest.mark.ui
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story('Check that page is loaded')
    def test_title_check(self):
        self.startPage = StartPage(self.driver)
        flag = self.startPage.get_title('DEMOQA')
        assert flag

    @pytest.mark.regression
    @pytest.mark.ui
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story('Check input field')
    @allure.description("Check input field")
    def test_validate_input_field(self):
        self.startPage = StartPage(self.driver)
        self.startPage.do_user_name_input()
        self.startPage.do_user_email_click()
        flag = self.startPage.get_user_name_input()
        assert flag == TestData.USER_NAME
