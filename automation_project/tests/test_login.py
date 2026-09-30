import pytest
from config import Config
from pages.home_page import HomePage
from pages.login_page import LoginPage


class TestLogin:

    @pytest.mark.smoke
    def test_valid_user_login(self, driver):
        """Verify successful user login with valid credentials."""
        home_page = HomePage(driver, timeout=Config.EXPLICIT_WAIT)
        login_page = LoginPage(driver, timeout=Config.EXPLICIT_WAIT)

        home_page.navigate_to_login()
        login_page.login(Config.USERNAME, Config.PASSWORD)

        actual_title = home_page.get_title()
        assert "My Account" in actual_title or "Account Login" in actual_title

    @pytest.mark.regression
    def test_invalid_user_login(self, driver):
        """Verify error message displayed on invalid login attempt."""
        home_page = HomePage(driver, timeout=Config.EXPLICIT_WAIT)
        login_page = LoginPage(driver, timeout=Config.EXPLICIT_WAIT)

        home_page.navigate_to_login()
        login_page.login("InvalidUser", "WrongPassword123")

        error_text = login_page.get_error_message()
        assert "Error: Incorrect login or password provided." in error_text