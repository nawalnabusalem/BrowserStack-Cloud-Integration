from logging import Logger
from typing import Tuple

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.main.side_menu import SideMenu


class MainPage(BasePage):
    def __init__(self, driver: webdriver, logger: Logger, timeout: int = 10) -> None:
        super().__init__(driver=driver, logger=logger, timeout=timeout)

        self.side_menu: SideMenu = SideMenu(driver=driver, logger=logger, timeout=timeout)

        self._cart_button: Tuple[str, str] = (By.CLASS_NAME, 'shopping_cart_link')
        self._cart_badge: Tuple[str, str] = (By.CLASS_NAME, 'shopping_cart_badge')


    def is_user_logged_in(self) -> bool:
        self.logger.debug(msg="Check if the user is logged in")

        return self.is_element_visible(locator=self._cart_button)

