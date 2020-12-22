import logging
import time

from webium import BasePage
from webium.wait import wait

from pages.base_page_object import BasePageObject
from pages.compare_page import ComparePage

import allure

LOGGER = logging.getLogger(__name__)


class CompareActions(BasePage, BasePageObject):

    # Get an instance driver, app, LoginPageLocators
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.compare_actions = ComparePage(driver=self.driver)

    @allure.step("Verify name of compared product")
    def verify_product_name(self, name, index):
        LOGGER.info("Verify name of compared product")
        assert name == self.compare_actions.get_product_name(index), "Test compare products failed." \
                                        f"Expected product {index+1} name: {name}, " \
                                        f"Actual product {index+1} name: {self.compare_actions.get_product_name(index)}"

    @allure.step("Verify url of compare page")
    def verify_url(self, url):
        LOGGER.info("Verify url")

        wait(self.compare_actions.compare_page_title.is_displayed)
        assert url in self.driver.current_url, "Test compare products failed. " \
                                               f"Expected url: {url}, " \
                                               f"Actual url: {self.driver.current_url}"
