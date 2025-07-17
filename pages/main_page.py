from pages.base import Base
from selenium.webdriver.common.by import By

class MainPage(Base):
    MENU_BUTTON_OFF_PLAN=(By.CSS_SELECTOR, "div[class='menu-block-proparties game verefi'] a[wized='newOffPlanLink']")

    def click_off_plan(self):
        self.click_element(self.MENU_BUTTON_OFF_PLAN)
