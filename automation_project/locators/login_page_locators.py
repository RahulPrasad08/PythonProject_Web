from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Object Repository for Login Page Elements."""

    USERNAME_INPUT = (By.ID, "loginFrm_loginname")
    PASSWORD_INPUT = (By.ID, "loginFrm_password")
    LOGIN_BUTTON = (By.XPATH, "//button[@title='Login']")

    # Registration options
    CONTINUE_BUTTON = (By.XPATH, "//button[@title='Continue']")
    ERROR_ALERT = (By.XPATH, "//div[contains(@class,'alert-error')]")