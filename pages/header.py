from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):
    CART_ICON = (By.XPATH, "//span[@class='nav-cart-icon nav-sprite']")
    ORDERS_ICON =(By.XPATH, "//a[@id='nav-orders']")



    pass

    def click_cart(self):
        self.click(*self.CART_ICON)

    def click_orders(self):
        self.click(*self.ORDERS_ICON)

