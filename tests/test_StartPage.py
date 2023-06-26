from pages.StartPage import StartPage
from tests.test_base import BaseTest
from config.config import TestData
import pytest
import allure
from allure_commons.types import AttachmentType

@allure.feature('Тест страницы https://instagram.com')
@pytest.mark.regression
class TestStartPage(BaseTest):

    @pytest.mark.smoke
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story('Проверка видимости ссылки "SIGN UP"')
    def test_signup_link_visible(self):
        self.startPage = StartPage(self.driver)
        flag = self.startPage.is_signup_link_visible()
        assert flag

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story('Проверка видимости кнопки "LOG IN WITH FACEBOOK"')
    def test_log_in_with_facebook_button_visible(self):
        self.startPage = StartPage(self.driver)
        flag = self.startPage.is_log_in_with_facebook_button_visible()
        assert flag

    @pytest.mark.smoke
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story('Проверка видимости кнопки "LOG IN"')
    def test_log_in_button_visible(self):
        self.startPage = StartPage(self.driver)
        flag = self.startPage.is_log_in_button_visible()
        assert flag

    @allure.severity(allure.severity_level.MINOR)
    @allure.story('Проверка видимости иконки "GOOGLE PLAY"')
    def test_google_play_icon_visible(self):
        self.startPage = StartPage(self.driver)
        link = self.startPage.is_google_play_icon_visible('src')
        assert link == TestData.GOOGLE_PLAY_ICON_LINK

    @allure.severity(allure.severity_level.MINOR)
    @allure.story('Проверка видимости иконки "MICROSOFT"')
    def test_microsoft_icon_visible(self):
        self.startPage = StartPage(self.driver)
        link = self.startPage.is_microsoft_icon_visible('src')
        assert link == TestData.MICROSOFT_ICON_LINK

    @allure.severity(allure.severity_level.MINOR)
    @allure.story('Проверка адреса ссылки на приложение в "GOOGLE PLAY"')
    def test_google_play_app_link(self):
        self.startPage = StartPage(self.driver)
        link = self.startPage.get_google_play_app_link('href')
        assert TestData.GOOGLE_PLAY_APP_LINK in link

    @allure.severity(allure.severity_level.MINOR)
    @allure.story('Проверка адреса ссылки на приложение в "MICROSOFT"')
    def test_microsoft_app_link(self):
        self.startPage = StartPage(self.driver)
        link = self.startPage.get_microsoft_app_link('href')
        assert TestData.MICROSOFT_APP_LINK in link

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story('Проверка надписи рядом с ссылкой "SIGN UP"')
    def test_title_by_sign_up_link(self):
        self.startPage = StartPage(self.driver)
        text = self.startPage.get_title_by_sign_up_link()
        assert text == TestData.DONT_HAVE_AN_ACCOUNT_TITLE

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story('Проверка надписи "GET THE APP"')
    def test_title_get_the_app(self):
        self.startPage = StartPage(self.driver)
        text = self.startPage.get_title_get_the_app()
        assert text == TestData.GET_THE_APP_TITLE

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story('Проверка названия страницы')
    def test_start_page_title(self):
        self.startPage = StartPage(self.driver)
        title = self.startPage.get_start_page_title('Instagram')
        assert title == TestData.START_PAGE_TITLE

    @allure.severity(allure.severity_level.MINOR)
    @allure.story('Проверка видимости ссылки "Meta"')
    def test_meta_link_visible(self):
        self.startPage = StartPage(self.driver)
        flag = self.startPage.is_meta_link_visible()
        assert flag

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Проверка адреса ссылки "Meta"')
    def test_meta_link(self):
        self.startPage = StartPage(self.driver)
        link = self.startPage.get_meta_link('href')
        assert link == TestData.META_LINK

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Проверка видимости ссылки "About"')
    def test_about_link_visible(self):
        self.startPage = StartPage(self.driver)
        flag = self.startPage.is_about_link_visible()
        assert flag

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Проверка адреса ссылки "About"')
    def test_about_link(self):
        self.startPage = StartPage(self.driver)
        link = self.startPage.get_about_link('href')
        assert link == TestData.ABOUT_LINK

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story('Проверка видимости надписи "© 2023 Instagram from Meta"')
    def test_instagram_from_meta_title_visible(self):
        self.startPage = StartPage(self.driver)
        flag = self.startPage.is_instagram_from_meta_title_visible()
        assert flag

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story('Проверка надписи в поле "USERNAME"')
    def test_login_field_title(self):
        self.startPage = StartPage(self.driver)
        text = self.startPage.get_login_field_title()
        assert text == TestData.LOGIN_FIELD_TITLE

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story('Проверка надписи в поле "PASSWORD"')
    def test_password_field_title(self):
        self.startPage = StartPage(self.driver)
        text = self.startPage.get_password_field_title()
        assert text == TestData.PASSWORD_FIELD_TITLE

    @allure.severity(allure.severity_level.MINOR)
    @allure.story('Проверка наличия требуемого языка в выпадающем списке языков')
    @pytest.mark.parametrize("number", [i for i in range(5)])
    def test_languages(self, number):
        self.startPage = StartPage(self.driver)
        with allure.step('Проверяем наличие языка в списке'):
            text = self.startPage.get_language_text(number)
        assert text in TestData.LANGUAGE, f'нет языка {text} в списке языков'

    @pytest.mark.smoke
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story('Проверка адреса ссылки "Forgot password?"')
    def test_reset_password_link(self):
        self.startPage = StartPage(self.driver)
        link = self.startPage.get_reset_password_link('href')
        assert link == TestData.RESET_PASSWORD_LINK

    @pytest.mark.smoke
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story('Проверка адреса ссылки "SIGN UP"')
    def test_sign_up_link(self):
        self.startPage = StartPage(self.driver)
        link = self.startPage.get_sign_up_link('href')
        assert link == TestData.SIGN_UP_LINK

    @pytest.mark.smoke
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story('Проверка перехода по ссылке "SIGN UP" на нужную страницу')
    def test_sign_up_page_title(self):
        self.startPage = StartPage(self.driver)
        title = self.startPage.get_sign_up_page_title('Sign up • Instagram')
        assert title == TestData.SIGN_UP_PAGE_TITLE

    @pytest.mark.smoke
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story('Проверка перехода по ссылке "FORGOT PASSWORD?" на нужную страницу')
    def test_reset_password_page_title(self):
        self.startPage = StartPage(self.driver)
        title = self.startPage.get_forgot_password_page_title('Reset Password • Instagram')
        assert title == TestData.RESET_PASSWORD_PAGE_TITLE


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story('Проверка перехода по кнопке "LOG IN WITH FACEBOOK" на нужную страницу')
    def test_log_in_with_facebook_page_title(self):
        self.startPage = StartPage(self.driver)
        title = self.startPage.get_log_in_with_facebook_page_title('Log into Facebook | Facebook')
        assert title == TestData.LOG_IN_WITH_FACEBOOK_PAGE_TITLE

    @allure.severity(allure.severity_level.MINOR)
    @allure.story('Проверка перехода по ссылке "Meta" на нужную страницу')
    def test_meta_page_title(self):
        self.startPage = StartPage(self.driver)
        title = self.startPage.get_meta_page_title('Meta | Social Metaverse Company')
        assert title == TestData.META_PAGE_TITLE

    @pytest.mark.smoke
    @allure.story('Тест авторизации с использованием логина и пароля')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login(self):
        self.startPage = StartPage(self.driver)
        flag = self.startPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        with allure.step('Скриншот страницы при авторизации'):
            allure.attach(self.driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
        assert flag
