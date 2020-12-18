import logging
import time

from webium import BasePage

from pages.base_page_object import BasePageObject
from pages.compare_page import ComparePageLocators
from pages.navigate_menu_page import NavigateMenuPageLocators
from pages.order_page import OrderPageLocators

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import allure

LOGGER = logging.getLogger(__name__)


class OrderActions(BasePage, BasePageObject):

    # Get an instance driver, app, LoginPageLocators
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.order_actions = OrderPageLocators(driver=self.driver)
        self.navigate_menu_actions = NavigateMenuPageLocators(driver=self.driver)
        self.compare_page_actions = ComparePageLocators(driver=self.driver)

    @allure.step('Navigate to selected page through tab on main page')
    def navigate_to_tab(self):
        LOGGER.info("Navigate to tab")
        self.navigate_menu_actions.tab_link.click()

    @allure.step('Navigate to selected page through section on current page')
    def navigate_to_section(self):
        LOGGER.info("Navigate to section")
        self.compare_page_actions.section_link.click()

    @allure.step('Navigate to product page from list of products')
    def get_product(self):
        LOGGER.info("Get product")

        time.sleep(1)
        self.compare_page_actions.products[0].click()

    @allure.step('Navigate to product\'s traders page from product page')
    def get_product_traders(self):
        LOGGER.info("Get product traders")
        self.order_actions.traders_link.click()

    @allure.step('Add product to shopping cart by clicking "Buy" button of any trader')
    def add_product_to_cart(self):
        LOGGER.info("Add product to cart")

        time.sleep(1)
        self.order_actions.buy_button.click()

    @allure.step('Navigate to shopping cart page from current page')
    def navigate_to_cart(self):
        LOGGER.info("Navigate to cart")
        self.order_actions.cart_link.click()

    @allure.step('Navigate to order creating page from shopping cart page')
    def navigate_to_order_menu(self):
        LOGGER.info("Navigate to order menu")

        time.sleep(1)
        self.order_actions.order_link.click()

    @allure.step('Check if browser url matches order creating page url')
    def verify_order_menu(self, url):
        LOGGER.info("Verify order menu")
        time.sleep(1)
        assert self.app.driver.current_url == url, "Test order failed. " \
                                                   f"Expected url: {url} " \
                                                   f"Actual url: {self.driver.current_url}"

    @allure.step('Deleting product from shopping cart')
    def clear_cart(self):
        time.sleep(1)
        self.driver.get(url=self.app.config['order']['cart_url'])
        ActionChains(self.driver).move_to_element(self.order_actions.remove_field).click().perform()
        time.sleep(1)
        # WebDriverWait(self.driver, 10).until_not(EC.visibility_of(self.order_actions.remove))
        self.order_actions.remove.click()
