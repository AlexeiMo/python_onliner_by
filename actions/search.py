import logging

from webium import BasePage

from pages.base_page_object import BasePageObject
from pages.search_page import SearchPageLocators

import allure

LOGGER = logging.getLogger(__name__)


class SearchActions(BasePage, BasePageObject):

    # Get an instance driver, app, SearchPageLocators
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.search_actions = SearchPageLocators(driver=self.driver)

    @allure.step('Switch to search frame')
    def switch_to_search_frame(self):
        LOGGER.info("Switch to search frame")
        self.driver.switch_to.frame(self.search_actions.search_frame)

    @allure.step('Type search option into appropriate field')
    def type_search_option(self, name):
        LOGGER.info("Type search option")
        self.search_actions.search_bar.send_keys(name)

    @allure.step('Verify search results')
    def verify_search_results(self, name):
        LOGGER.info("Verify search results")
        name = name.upper().split(sep=' ')
        for item in self.search_actions.results:
            text = item.text.upper().split(sep=' ')
            for word in name:
                assert word in text, "Test search failed."
