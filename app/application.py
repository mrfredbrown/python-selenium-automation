from pages.header import Header
from pages.main_page import MainPage
from pages.verify import VerifyCartPage

class Application:
    def __init__(self, driver):
        self.driver = driver
        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.verify = VerifyCartPage(self.driver)