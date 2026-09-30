from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Base class that all page objects inherit from."""

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        """Wait for an element to be visible before returning it."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Wait for an element to be clickable and click it."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()


    def type_text(self, locator, text):
        """Wait for an input field, clear existing text, and type new text."""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_title(self):
        """Return the current page title."""
        return self.driver.title