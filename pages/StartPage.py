from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from config.config import TestData


class StartPage(BasePage):
    USERNAME = (By.NAME, 'username')
    PASSWORD = (By.NAME, 'password')
    LOG_IN_BUTTON = (By.XPATH, '//button[normalize-space()="Log in"]')
    SIGN_UP_LINK = (By.LINK_TEXT, 'Sign up')
    FACEBOOK_LINK = (By.XPATH, '//button[normalize-space()="Log in with Facebook"]')
    RESET_PASSWORD_LINK = (By.LINK_TEXT, 'Forgot password?')
    GOOGLE_PLAY_ICON_LINK = (By.CLASS_NAME, '_aa5q')
    MICROSOFT_ICON_LINK = (By.CLASS_NAME, '_aa5q')
    GOOGLE_PLAY_APP_LINK = (By.CSS_SELECTOR, 'div._aa4v a')
    MICROSOFT_APP_LINK = (By.CSS_SELECTOR, 'div._aa4v a')
    DONT_HAVE_AN_ACCOUNT = (By.CLASS_NAME, '_ab25')
    GET_THE_APP = (By.CLASS_NAME, '_aa4u')
    FOOTER_LINKS = (By.CSS_SELECTOR, 'footer a')
    META_LINK = (By.LINK_TEXT, 'Meta')
    ABOUT_LINK = (By.LINK_TEXT, 'About')
    INSTAGRAM_FROM_META_TITLE = (By.XPATH, "//*[contains(text(), '© 2023 Instagram from Meta')]")
    LOGIN_FIELD_TITLE = (By.CLASS_NAME, '_aa4a')
    PASSWORD_FIELD_TITLE = (By.CLASS_NAME, '_aa4a')
    LANGUAGES = (By.TAG_NAME, 'option')
    LOG_IN_INDICATOR = (By.CLASS_NAME, '_ab6-')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_start_page_title(self, title):
        return self.get_title(title)

    def is_signup_link_visible(self):
        return self.is_visible(self.SIGN_UP_LINK)

    def is_log_in_with_facebook_button_visible(self):
        return self.is_visible(self.FACEBOOK_LINK)

    def is_log_in_button_visible(self):
        return self.is_visible(self.LOG_IN_BUTTON)

    def is_reset_password_link_visible(self):
        return self.is_visible(self.RESET_PASSWORD_LINK)

    def is_google_play_icon_visible(self, attribute):
        return self.get_attribute(self.GOOGLE_PLAY_ICON_LINK, attribute, 0)

    def is_microsoft_icon_visible(self, attribute):
        return self.get_attribute(self.MICROSOFT_ICON_LINK, attribute, 1)

    def get_google_play_app_link(self, attribute):
        return self.get_attribute(self.GOOGLE_PLAY_APP_LINK, attribute, 0)

    def get_microsoft_app_link(self, attribute):
        return self.get_attribute(self.MICROSOFT_APP_LINK, attribute, 1)

    def get_title_by_sign_up_link(self):
        return self.get_element_text(self.DONT_HAVE_AN_ACCOUNT)

    def get_title_get_the_app(self):
        return self.get_element_text(self.GET_THE_APP)

    def get_reset_password_link(self, attribute):
        return self.get_attribute(self.RESET_PASSWORD_LINK, attribute, 0)

    def get_sign_up_link(self, attribute):
        return self.get_attribute(self.SIGN_UP_LINK, attribute, 0)

    def is_meta_link_visible(self):
        return self.is_visible(self.META_LINK)

    def get_meta_link(self, attribute):
        return self.get_attribute(self.FOOTER_LINKS, attribute, 0)

    def is_about_link_visible(self):
        return self.is_visible(self.META_LINK)

    def get_about_link(self, attribute):
        return self.get_attribute(self.FOOTER_LINKS, attribute, 1)

    def is_instagram_from_meta_title_visible(self):
        return self.is_visible(self.INSTAGRAM_FROM_META_TITLE)

    def get_login_field_title(self):
        return self.get_element_text(self.LOGIN_FIELD_TITLE, 0)

    def get_password_field_title(self):
        return self.get_element_text(self.PASSWORD_FIELD_TITLE, 1)

    def get_language_text(self, i):
        return self.get_element_text(self.LANGUAGES, i)

    def do_login(self, username, password):
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOG_IN_BUTTON)
        return self.is_visible(self.LOG_IN_INDICATOR)

    def get_sign_up_page_title(self, title):
        self.do_click(self.SIGN_UP_LINK)
        return self.get_title(title)

    def get_forgot_password_page_title(self, title):
        self.do_click(self.RESET_PASSWORD_LINK)
        return self.get_title(title)

    def get_log_in_with_facebook_page_title(self, title):
        self.do_click(self.FACEBOOK_LINK)
        return self.get_title(title)

    def get_meta_page_title(self, title):
        self.do_click(self.META_LINK)
        self.switch_to_window(1)
        return self.get_title(title)
