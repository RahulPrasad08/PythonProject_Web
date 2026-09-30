from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):
    """Action methods for the Login / Account Page."""

    def enter_username(self, username):
        self.type_text(LoginPageLocators.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type_text(LoginPageLocators.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

      #  def click_men(self):
       #     self.click(MenPageLocators.MEN_BUTTON)

    def login(self, username, password):
        """Convenience method to execute full login flow."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()