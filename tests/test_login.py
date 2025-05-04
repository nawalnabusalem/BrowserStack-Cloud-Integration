import json
import logging
from enum import Enum

import pytest
from selenium import webdriver

from pages.login.login_page import LoginPage
from pages.main.main_page import MainPage


class LoginStatus(Enum):
    VALID_LOGIN = 'valid-login'
    INVALID_CREDENTIALS = 'Epic sadface: Username and password do not match any user in this service'
    LOCKED_USER = 'Epic sadface: Sorry, this user has been locked out.'
    MISSING_USERNAME = 'Epic sadface: Username is required'
    MISSING_PASSWORD = 'Epic sadface: Password is required'


class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self, browser, request):
        self.logger = logging.Logger(name=__name__, level=logging.DEBUG)

        file_handler = logging.FileHandler(filename="debug.log", encoding="utf-8")
        file_handler.setFormatter(logging.Formatter('[%(levelname)s] %(asctime)s - %(message)s'))
        self.logger.addHandler(file_handler)


        self.login_page = LoginPage(driver=browser, logger=self.logger)
        self.main_page = MainPage(driver=browser, logger=self.logger)

        self.logger.info(f'\n{"="*100}\nRunning: {request.node.name}\n{"="*100}\n')

    @pytest.mark.parametrize("username,password,expected_result", [
        ("standard_user", "any_pass", LoginStatus.INVALID_CREDENTIALS),
        ("locked_out_user", "secret_sauce", LoginStatus.LOCKED_USER),
        ("", "", LoginStatus.MISSING_USERNAME),
        ("standard_user", "", LoginStatus.MISSING_PASSWORD),
        ("standard_user", "secret_sauce", LoginStatus.VALID_LOGIN),
    ])
    def test_login_page(self,
                        username: str,
                        password: str,
                        expected_result: LoginStatus, browser) -> None:

        self.login_page.load()

        self.logger.info(f"Attempt login with credentials - User: {username}")
        self.login_page.login(username=username, password=password)

        if expected_result == LoginStatus.VALID_LOGIN:
            self.logger.info("Verify successful login")

            if not self.main_page.is_user_logged_in():
                self.set_remote_test_status(driver=browser, status="failed", reason="Login failed when it should success as expected")

            self.set_remote_test_status(driver=browser, status="passed", reason="Login successful when it should success")

            self.logger.info("Login successful - proceeding with logout")
            self.main_page.side_menu.logout()

        else:
            self.logger.info("Verify failed login as expected")

            if self.main_page.is_user_logged_in():
                self.set_remote_test_status(driver=browser, status="failed", reason="Login succeeded when it should fail as expected")

            self.set_remote_test_status(driver=browser, status="passed", reason="Login failed when it should fail")

    def set_remote_test_status(self, driver: webdriver, status: str, reason: str) -> None:
        executor_args = {
            "action": "setSessionStatus",
            "arguments": {"status": status, "reason": reason}
        }
        driver.execute_script(f"browserstack_executor: {json.dumps(executor_args)}")
