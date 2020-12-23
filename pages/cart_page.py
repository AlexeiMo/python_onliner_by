from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds
from webium.wait import wait


class CartPage(BasePage):
    order = Find(by=By.CSS_SELECTOR,
                 value="a[class='button-style button-style_primary button-style_small cart-form__button']")
    order_form = Find(by=By.CSS_SELECTOR, value="div[class='cart-form__flex']")
    remove = Find(by=By.XPATH, value="//div[@class='cart-form__offers-part cart-form__offers-part_remove']/div/a")
    remove_field = Find(by=By.XPATH, value="//div[@class='cart-form__control']//input")

    def click_order_link(self):
        wait(self.order.is_displayed)
        self.order.click()

    def click_remove_field(self):
        wait(self.remove_field.is_displayed)
        self.remove_field.click()

    def click_remove(self):
        wait(self.remove.is_displayed)
        self.remove.click()
