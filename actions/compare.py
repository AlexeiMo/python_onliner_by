import logging
import time

from webium import BasePage

from pages.base_page_object import BasePageObject
from pages.compare_page import ComparePageLocators
from pages.navigate_menu_page import NavigateMenuPageLocators

import allure

LOGGER = logging.getLogger(__name__)


class CompareActions(BasePage, BasePageObject):

    # Get an instance driver, app, LoginPageLocators
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.navigate_actions = NavigateMenuPageLocators(driver=self.driver)
        self.compare_actions = ComparePageLocators(driver=self.driver)
        self.product_names = []

    @allure.step('Navigate to selected page through tab on main page')
    def navigate_to_tab(self):
        LOGGER.info("Navigate to tab")
        self.navigate_actions.tab_link.click()

    @allure.step('Navigate to selected page through section on current page')
    def navigate_to_section(self):
        LOGGER.info("Navigate to section")
        self.compare_actions.section_link.click()

    @allure.step('Navigate to selected page through section on current page')
    def navigate_to_section2(self):
        LOGGER.info("Navigate to section")
        self.compare_actions.section_link2.click()

    @allure.step('Navigate to product page from list of products')
    def get_product(self, id):
        LOGGER.info(f"Get product №{id + 1}")

        time.sleep(1)
        self.product_names.append(self.compare_actions.products[id].text)
        self.compare_actions.products[id].click()

    @allure.step('Set compare checkbox to "Checked" status"')
    def set_compare_checkbox(self):
        LOGGER.info("Set compare checkbox")
        time.sleep(1)
        self.compare_actions.compare_checkbox.click()

    @allure.step('Navigate to compare page through link on current page')
    def navigate_to_compare_page(self):
        LOGGER.info("Navigate to compare page")
        time.sleep(1)
        self.compare_actions.compare_button.click()

    @allure.step('Check if compare page contains selected products')
    def verify_comparison(self, url):
        LOGGER.info("Verify comparison")

        time.sleep(1)
        assert url in self.app.current_url(), "Test compare products failed. " \
                                              f"Expected url: https://catalog.onliner.by/compare/, " \
                                              f"Actual url: {self.app.current_url()}"
        assert self.product_names[0] == self.compare_actions.compared_products[0].text, "Test compare products failed." \
                                        f"Expected product 1 name: {self.product_names[0]}, " \
                                        f"Actual product 1 name: {self.compare_actions.compared_products[0].text}"
        assert self.product_names[1] == self.compare_actions.compared_products[1].text, "Test compare products failed." \
                                        f"Expected product 2 name: {self.product_names[1]}, " \
                                        f"Actual product 2 name: {self.compare_actions.compared_products[1].text}"
