from logging import Logger
from typing import Tuple

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SideMenu(BasePage):
    def __init__(self, driver: webdriver, logger: Logger, timeout: int = 10) -> None:
        super().__init__(driver=driver, logger=logger, timeout=timeout)

        self._open_menu_button: Tuple[str, str] = (By.ID, 'react-burger-menu-btn')
        self._logout: Tuple[str, str] = (By.ID, 'logout_sidebar_link')

    def open_menu(self) -> None:
        self.logger.debug(msg=f"Open the main side menu")

        if self.is_element_visible(locator=self._open_menu_button):
            self.click(self._open_menu_button)

    def logout(self) -> None:
        self.open_menu()

        self.logger.debug(msg=f"Click logout button")
        self.click(self._logout)


