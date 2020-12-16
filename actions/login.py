from pages.base_page_object import BasePageObject
from pages.login_page import LoginPageLocators
import logging
from webium import BasePage

LOGGER = logging.getLogger(__name__)


class LoginActions(BasePage, BasePageObject):

    # Get an instance driver, app, LoginPageLocators
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.login_actions = LoginPageLocators(driver=self.driver)

    def click_log_in(self):
        LOGGER.info("Click log in")
        self.login_actions.log_in.click()

    def type_credentials(self, group):
        LOGGER.info("Type username")
        self.login_actions.username_input.send_keys(group.username)
        LOGGER.info("Type password")
        self.login_actions.password_input.send_keys(group.password)

    def click_submit(self):
        LOGGER.info("Click submit")
        self.login_actions.submit.click()

    def verify_profile_icon(self):
        LOGGER.info("Verify profile icon")
        assert self.login_actions.profile_icon, "Test login failed"
