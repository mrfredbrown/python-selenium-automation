from selenium.webdriver.common.by import By
from pages.base_page import Page

class VerifyCartPage(Page):
    RESULT = (By.TAG_NAME, 'h2')
    #RESULT = (By.XPATH, "//span[@class='nav-cart-icon nav-sprite']")
    #$x("//h1[@class='a-spacing-small']")
    SIGNIN = (By.XPATH, "//h1[@class='a-spacing-small']")
    pass

    def verify_cart(self):
        expected_result = "Your Amazon Cart is empty"
        actual_result = self.driver.find_element(*self.RESULT).text
        assert expected_result == actual_result, f"Expected text {expected_result} did not match {actual_result}"

    def verify_sign_in(self):
        expected_result = "Sign-In"
        actual_result = self.driver.find_element(*self.SIGNIN).text
        assert expected_result == actual_result, f"Expected text {expected_result} did not match {actual_result}"