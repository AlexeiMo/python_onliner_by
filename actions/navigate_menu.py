from pages.base_page_object import BasePageObject
from pages.navigate_menu_page import NavigateMenuPageLocators
import logging
from webium import BasePage
import allure

LOGGER = logging.getLogger(__name__)


class NavigateMenuActions(BasePage, BasePageObject):

    # Get an instance driver, app, LoginPageLocators
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.catalog_actions = NavigateMenuPageLocators(driver=self.driver)

    @allure.step('Navigate browser to selected tab on main page')
    def navigate_to_tab(self):
        LOGGER.info("Click tab")
        self.catalog_actions.tab_link.click()

    @allure.step('Check if current browser url matches given url')
    def verify_url(self, url):
        LOGGER.info("Verify url")
        assert self.driver.current_url == url, "Test menu navigate failed" \
                                               f"Expected: {url}, " \
                                               f"Actual: {self.driver.current_url}"
