from pages.base import Base
from selenium.webdriver.common.by import By


class SignIn(Base):
    USERNAME_FIELD=(By.CSS_SELECTOR, "input[placeholder='Email']")
    PASSWORD_FIELD=(By.CSS_SELECTOR, "input[placeholder='Password']")
    CONTINUE_BUTTON=(By.CSS_SELECTOR, "a[wized='loginButton']")

    def print_sign_in_class(self):
        print('SignIn class:')

    def open_sign_in_page(self,site):
        self.open_page(site)

    def sign_in(self):
        self.input_field(self.USERNAME_FIELD, "")
        self.input_field(self.PASSWORD_FIELD, "")
        self.click_element(self.CONTINUE_BUTTON)