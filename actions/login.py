import logging

from webium import BasePage

from pages.base_page_object import BasePageObject
from pages.login_page import LoginPage

import allure

LOGGER = logging.getLogger(__name__)


class LoginActions(BasePage, BasePageObject):

    # Get an instance driver, app, LoginPageLocators
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.login_actions = LoginPage(driver=self.driver)

    @allure.step("Type username and password")
    def type_credentials(self, group):
        LOGGER.info("Type username")
        self.login_actions.type_username(group.username)
        LOGGER.info("Type password")
        self.login_actions.type_password(group.password)

    @allure.step("Submit credentials")
    def submit_credentials(self):
        LOGGER.info("Click submit button")
        self.login_actions.click_submit()
