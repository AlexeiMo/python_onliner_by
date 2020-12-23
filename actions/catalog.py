import logging
import time

import allure
from selenium.webdriver.common.action_chains import ActionChains
from webium import BasePage

from pages.base_page_object import BasePageObject
from pages.catalog_page import CatalogPage

LOGGER = logging.getLogger(__name__)

class CatalogActions(BasePageObject, BasePage):

    # Get an instance driver, app, SearchPageLocators
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.catalog_actions = CatalogPage(driver=self.driver)

    @allure.step("Verify navigate menu process")
    def verify_url(self, url):
        LOGGER.info("Verify navigate menu process")
        assert self.driver.current_url == url, "Test menu navigate failed" \
                                               f"Expected: {url}, " \
                                               f"Actual: {self.driver.current_url}"

    @allure.step("Navigate to selected subsection")
    def navigate_to_subsection(self, name):
        LOGGER.info(f"Navigate to subsection '{name}'")
        for index, section in enumerate(self.catalog_actions.subsections):
            if section.text == name:
                self.catalog_actions.click_subsection_link(index)
                break
        else:
            raise AttributeError("No such subsection was found")

    @allure.step("Navigate to selected product")
    def navigate_to_product(self, index=0):
        LOGGER.info(f"Navigate to product {index}")
        time.sleep(1)
        self.catalog_actions.click_product_link(index)

    @allure.step("Navigate to compare page through link on current page")
    def navigate_to_compare_page(self):
        LOGGER.info("Navigate to compare page")
        self.catalog_actions.click_compare()

    @allure.step("Remove compare")
    def remove_compare_icon(self):
        LOGGER.info("Remove compare")
        self.catalog_actions.click_remove_compare_icon()
        self.catalog_actions.click_remove_compare_button()

    def scroll_down(self):
        ActionChains(driver=self.driver).send_keys('ue015').perform()
