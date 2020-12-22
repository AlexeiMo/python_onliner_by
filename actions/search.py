import logging

from webium import BasePage

from pages.base_page_object import BasePageObject
from pages.search_page import SearchPage

import allure

LOGGER = logging.getLogger(__name__)


class SearchActions(BasePage, BasePageObject):

    # Get an instance driver, app, SearchPageLocators
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.search_actions = SearchPage(driver=self.driver)

    @allure.step('Type search option into appropriate field')
    def search_item(self, name):
        LOGGER.info("Type search option")
        self.search_actions.type_search_option(name)

    @allure.step('Verify search results')
    def verify_search_results(self, name):
        LOGGER.info("Verify search results")
        name = name.upper().split(sep=' ')
        results = self.search_actions.get_search_results()
        for result in results:
            text = result.upper().split(sep=' ')
            for word in name:
                assert word in text, "Test search failed."
