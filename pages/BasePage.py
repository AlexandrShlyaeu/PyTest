from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator, webdriver_element_number=0):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))[webdriver_element_number].text

    def is_visible(self, by_locator, webdriver_element_number=0):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))[webdriver_element_number].text
        return bool(element)

    def get_attribute(self, by_locator, attribute, webdriver_element_number=0):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))[webdriver_element_number].get_attribute(attribute)

    def switch_to_window(self, number_of_window):
        return self.driver.switch_to.window(self.driver.window_handles[number_of_window])



