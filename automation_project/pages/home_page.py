from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators

class HomePage(BasePage):
    """Action methods for the Landing Page."""

    def navigate_to_login(self):
        """Click the 'Login or register' link in the top menu."""
        self.click(HomePageLocators.LOGIN_REGISTER_LINK)