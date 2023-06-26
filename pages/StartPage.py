from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from config.config import Config
from data.TestData import TestData


class StartPage(BasePage):

    USER_NAME_LABEL = (By.ID, 'userName-label',)
    USER_NAME_FIELD = (By.ID, 'userName')
    USER_EMAIL_FIELD = (By.ID, 'userEmail')


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Config.BASE_URL)

    def get_start_page_title(self, title):
        return self.get_title(title)

    def do_user_name_input(self):
        return self.do_send_keys(self.USER_NAME_FIELD, TestData.USER_NAME)

    def do_user_email_click(self):
        return self.do_click(self.USER_EMAIL_FIELD)


    def get_user_name_input(self):
        return self.get_element_text(self.USER_NAME_FIELD)
