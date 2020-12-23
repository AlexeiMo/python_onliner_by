import logging

from webium import BasePage

from pages.base_page_object import BasePageObject
from pages.main_page import MainPage

import allure

LOGGER = logging.getLogger(__name__)


class MainPageActions(BasePage, BasePageObject):

    # Get an instance driver, app, LoginPageLocators
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.main_page_actions = MainPage(driver=self.driver)

    @allure.step("Navigate to selected section")
    def navigate_to_section(self, name):
        LOGGER.info(f"Navigate to section '{name}'")
        for index, section in enumerate(self.main_page_actions.sections):
            if section.text == name:
                self.main_page_actions.click_section_link(index)
                break
        else:
            raise AttributeError("No such section was found")

    @allure.step("Click login button")
    def click_login(self):
        LOGGER.info("Click login button")
        self.main_page_actions.click_login()

    @allure.step("Verify authorization process")
    def verify_authorization(self):
        LOGGER.info("Verify authorization process")
        assert self.main_page_actions.profile_icon, "Test login failed"

    @allure.step("Switch to search frame")
    def switch_to_search_frame(self):
        LOGGER.info("Switch to search frame")
        self.driver.switch_to.frame(self.main_page_actions.search_frame)

    @allure.step("Navigate to cart page")
    def navigate_to_cart_page(self):
        LOGGER.info("Navigate to cart page")
        self.main_page_actions.click_cart_link()
