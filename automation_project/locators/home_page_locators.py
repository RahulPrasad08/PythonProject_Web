from selenium.webdriver.common.by import By


class HomePageLocators:
    """Object Repository for Home Page Elements."""

    LOGIN_REGISTER_LINK = (By.XPATH, "//ul[@id='customer_menu_top']//a")
    SEARCH_INPUT = (By.ID, "filter_keyword")