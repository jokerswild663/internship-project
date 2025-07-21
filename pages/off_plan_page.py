from pages.base import Base
from selenium.webdriver.common.by import By
from time import sleep

class OffPlanPage(Base):
    FIRST_LISTING = (By.CSS_SELECTOR, "div[class*='overflow-auto'] img[alt='Property Image']")
    VISUALIZATION_OPTION_TABS = (By.CSS_SELECTOR, "a.w-tab-link")

    def click_first_listing(self):
        sleep(5)
        self.click_element(self.FIRST_LISTING)

    def verify_visualization_options(self,options):
        elements = self.get_elements(self.VISUALIZATION_OPTION_TABS)
        for element in elements:
            self.verify_text(options,self.VISUALIZATION_OPTION_TABS)