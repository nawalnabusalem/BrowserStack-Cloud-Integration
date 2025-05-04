import pytest

from selenium import webdriver

USERNAME = "your_username"
PASSWORD = "<PASSWORD>"
ACCESS_KEY = "your_access_key"

@pytest.fixture(scope="session")
def browser(request):
    driver = webdriver.Remote(
        command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
    )

    yield driver

    driver.quit()