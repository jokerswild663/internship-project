from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def get_element(self, locator):
        element = self.driver.wait.until(EC.presence_of_element_located(locator))
        return element

    def input_field(self, locator, text):
        self.driver.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def click_element(self,locator):
        self.driver.wait.until(EC.element_to_be_clickable(locator)).click()

    def verify_text(self, text,locator):
        actual=self.driver.wait.until(EC.visibility_of_element_located(locator)).text
        expected=text

        assert actual==expected, f'actual: {actual} != expected: {expected}'

    def verify_clickable(self,locator):
        assert EC.element_to_be_clickable(locator), f'{locator.text} is not clickable'