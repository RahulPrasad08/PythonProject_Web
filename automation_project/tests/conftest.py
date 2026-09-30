import pytest
from selenium import webdriver
from config import Config


@pytest.fixture(scope="function")
def driver():
    """
    Fixture to initialize WebDriver before a test function
    and automatically close it after completion.
    """
    browser = Config.BROWSER.lower()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        _driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        _driver = webdriver.Firefox()
        _driver.maximize_window()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    _driver.get(Config.BASE_URL)

    # Yield control to the test function
    yield _driver

    # Teardown: Executes after test function completes
    _driver.quit()