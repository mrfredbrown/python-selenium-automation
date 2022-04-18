

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.amazon.com'

    def open_url(self, end_url : str = ''):
        self.driver.get(f'{self.base_url}{end_url}')

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, \
            f"Expected text {expected_text} did not match actual {actual_text}"