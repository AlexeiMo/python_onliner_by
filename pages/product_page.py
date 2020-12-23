from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds
from webium.wait import wait


class ProductPage(BasePage):
    subsection = Find(by=By.CSS_SELECTOR, value="a[href='https://catalog.onliner.by/tv'][class='breadcrumbs__link']")
    compare_checkbox = Find(by=By.XPATH, value="//li[@id='product-compare-control']/label/span")
    product_name = Find(by=By.CSS_SELECTOR, value="h1[itemprop='name']")
    traders = Find(by=By.XPATH, value="//a/span[.='Предложения продавцов']/..")
    buy_button = Find(by=By.XPATH, value="//div[@class='offers-list__control offers-list__control_default']/a")
    cart = Find(by=By.XPATH, value="//div[@id='cart-desktop']/a")

    def click_subsection_link(self):
        wait(self.subsection.is_displayed)
        self.subsection.click()

    def set_compare_checkbox(self):
        wait(self.compare_checkbox.is_displayed)
        self.compare_checkbox.click()

    def get_product_name(self):
        wait(self.product_name.is_displayed)
        return self.product_name.text

    def click_traders_link(self):
        wait(self.traders.is_displayed)
        self.traders.click()

    def click_buy(self):
        wait(self.buy_button.is_displayed)
        self.buy_button.click()
