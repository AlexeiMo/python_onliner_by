import logging

from webium import BasePage

from pages.base_page_object import BasePageObject
from pages.login_page import LoginPageLocators

import allure

LOGGER = logging.getLogger(__name__)


class LoginActions(BasePage, BasePageObject):

    # Get an instance driver, app, LoginPageLocators
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.login_actions = LoginPageLocators(driver=self.driver)

    @allure.step('Get login page through button on main page')
    def get_log_in_page(self):
        LOGGER.info("Get log in page")
        self.login_actions.log_in.click()

    @allure.step('Type user credentials in appropriate fields')
    def type_credentials(self, group):
        LOGGER.info("Type username")
        self.login_actions.username_input.send_keys(group.username)
        LOGGER.info("Type password")
        self.login_actions.password_input.send_keys(group.password)

    @allure.step('Click button to submit credentials')
    def submit_credentials(self):
        LOGGER.info("Click button to submit credentials")
        self.login_actions.submit.click()

    @allure.step('Verify authorization process')
    def verify_authorization(self):
        LOGGER.info("Verify authorization process")
        assert self.login_actions.profile_icon, "Test login failed"
