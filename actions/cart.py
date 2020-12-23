import logging
import time

from webium import BasePage
from webium.wait import wait

from pages.base_page_object import BasePageObject
from pages.cart_page import CartPage

import allure

LOGGER = logging.getLogger(__name__)


class CartActions(BasePage, BasePageObject):

    # Get an instance driver, app, LoginPageLocators
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.cart_actions = CartPage(driver=self.driver)

    @allure.step("Navigate to order page")
    def navigate_to_order_page(self):
        LOGGER.info("Navigate to order page")
        self.cart_actions.click_order_link()

    @allure.step("Verify url of order page")
    def verify_url(self, url):
        LOGGER.info("Verify url")
        wait(self.cart_actions.order_form.is_displayed)
        assert self.driver.current_url == url, "Test order failed. " \
                                               f"Expected url: {url} " \
                                               f"Actual url: {self.driver.current_url}"

    @allure.step("Display remove field")
    def display_remove_field(self):
        LOGGER.info("Display remove field")
        self.cart_actions.click_remove_field()

    @allure.step("Remove product from customer cart")
    def click_remove(self):
        LOGGER.info("Remove product from customer cart")
        self.cart_actions.click_remove()
