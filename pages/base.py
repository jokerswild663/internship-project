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

    def get_elements(self, locator):
        self.driver.wait.until(EC.presence_of_element_located(locator))
        elements = self.driver.find_elements(*locator)
        return elements

    def input_field(self, locator, text):
        self.driver.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def click_element(self,locator):
        self.driver.wait.until(EC.element_to_be_clickable(locator)).click()

    def verify_text(self, entries, locator):
        actual=self.driver.wait.until(EC.visibility_of_element_located(locator)).text
        expected=entries

        assert actual in expected, f'actual: {actual} Not in expected: {expected}'

    def verify_clickable(self,locator):
        assert EC.element_to_be_clickable(locator), f'{locator.text} is not clickable'