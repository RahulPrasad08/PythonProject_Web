import pytest
from config import Config
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.men_page import MenPage
from tests.conftest import driver


class TestMen:

    @pytest.mark.smoke
    def test_addcart(self, driver):
        home_page = HomePage(driver, timeout=Config.EXPLICIT_WAIT)
        login_page = LoginPage(driver, timeout=Config.EXPLICIT_WAIT)
        men_page = MenPage(driver, timeout=Config.EXPLICIT_WAIT)

        # 1. Login user
        home_page.navigate_to_login()
        login_page.login(Config.USERNAME, Config.PASSWORD)

        men_page.add_to_cart()
        # Scroll down by 500 pixels
        driver.execute_script("window.scrollBy(0, 500);")
        men_page.add_to_cart()
        addcart_title = driver.title
        print("Print the title:",addcart_title)
        # Exact match check
        #assert addcart_title.text == "Shopping Cart", f"Expected 'Shopping Cart', got '{addcart_title.text}'"
        # ✅ CORRECT: addcart_title is already a string
        assert addcart_title == "Shopping Cart", f"Expected 'Shopping Cart', got '{addcart_title}'"
