from pages.base import Base
from selenium.webdriver.common.by import By

class OffPlanPage(Base):
    FIRST_LISTING = (By.CSS_SELECTOR, "a[class='outline-none'] div.bg-card")
    VISUALIZATION_OPTION_ARCHITECTURE = (By.CSS_SELECTOR, "a.tab[data-w-tab='Tab 1']")
    VISUALIZATION_OPTION_INTERIOR = (By.CSS_SELECTOR, "a.tab[data-w-tab='Tab 2']")
    VISUALIZATION_OPTION_LOBBY = (By.CSS_SELECTOR, "a.tab[data-w-tab='Tab 3']")


    def click_first_listing(self):
        self.click_element(self.FIRST_LISTING)

    def check_visualization_architecture(self, text):
        self.verify_text(text, self.VISUALIZATION_OPTION_ARCHITECTURE)
        self.verify_clickable(self.VISUALIZATION_OPTION_ARCHITECTURE)

    def check_visualization_interior(self, text):
        self.verify_text(text, self.VISUALIZATION_OPTION_INTERIOR)
        self.verify_clickable(self.VISUALIZATION_OPTION_INTERIOR)

    def check_visualization_lobby(self, text):
        self.verify_text(text, self.VISUALIZATION_OPTION_LOBBY)
        self.verify_clickable(self.VISUALIZATION_OPTION_LOBBY)