from pages.base import Base
from selenium.webdriver.common.by import By
from time import sleep

class MainPage(Base):
    MENU_BUTTON_OFF_PLAN=(By.CSS_SELECTOR, "a[wized='newOffPlanLink'] div.menu-text")

    def click_off_plan(self):
        sleep(5)
        self.click_element(self.MENU_BUTTON_OFF_PLAN)
