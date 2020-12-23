import logging
import time

import allure
from webium import BasePage

from pages.base_page_object import BasePageObject
from pages.product_page import ProductPage

LOGGER = logging.getLogger(__name__)


class ProductActions(BasePage, BasePageObject):

    # Get an instance driver, app, LoginPageLocators
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.product_actions = ProductPage(driver=self.driver)
        self.name = ""

    @allure.step('Set compare checkbox to "Checked" status"')
    def set_compare_checkbox(self):
        LOGGER.info("Set compare checkbox")
        self.product_actions.set_compare_checkbox()

    @allure.step("Return back to subsection")
    def navigate_to_subsection(self):
        LOGGER.info("Return back to subsection")
        self.product_actions.click_subsection_link()

    @allure.step("Get product name")
    def get_product_name(self):
        LOGGER.info("Get product name")
        return self.product_actions.get_product_name()

    @allure.step("Navigate to product traders list")
    def navigate_to_product_traders(self):
        LOGGER.info("Navigate to product traders list")
        self.product_actions.click_traders_link()

    @allure.step("Click button to buy product")
    def click_buy(self):
        LOGGER.info("Click button to buy product")
        self.product_actions.click_buy()
