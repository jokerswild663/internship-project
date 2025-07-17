from pages.base import Base
from pages.main_page import MainPage
from pages.off_plan_page import OffPlanPage
from pages.sign_in import SignIn


class Application:
    def __init__(self,driver):
        self.title='test'
        self.sign_in_page = SignIn(driver)
        self.main_page = MainPage(driver)
        self.off_plan_page = OffPlanPage(driver)

    def print_var(self):
        print(self.title)