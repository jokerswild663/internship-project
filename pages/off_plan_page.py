from pages.base import Base
from selenium.webdriver.common.by import By
from time import sleep

class OffPlanPage(Base):
    FIRST_LISTING = (By.CSS_SELECTOR, "div[class*='overflow-auto'] img[alt='Property Image']")
    VISUALIZATION_OPTION_ARCHITECTURE = (By.CSS_SELECTOR, "a.tab[data-w-tab='Tab 1']")
    VISUALIZATION_OPTION_INTERIOR = (By.CSS_SELECTOR, "a.tab[data-w-tab='Tab 2']")
    VISUALIZATION_OPTION_LOBBY = (By.CSS_SELECTOR, "a.tab[data-w-tab='Tab 3']")


    def click_first_listing(self):
        sleep(5)
        self.click_element(self.FIRST_LISTING)

    def check_visualization_option(self,text):
        if text=='Architecture':
            locator=self.VISUALIZATION_OPTION_ARCHITECTURE
        elif text=='Interior':
            locator=self.VISUALIZATION_OPTION_INTERIOR
        elif text=='Lobby':
            locator=self.VISUALIZATION_OPTION_LOBBY
        else:
            return

        self.verify_text(text, locator)
        self.verify_clickable(locator)