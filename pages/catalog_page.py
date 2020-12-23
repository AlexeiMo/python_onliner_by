from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds
from webium.wait import wait


class CatalogPage(BasePage):
    subsections = Finds(by=By.XPATH, value="//ul[@class='catalog-bar__list']/li/a")
    subsection_page_header = Find(by=By.CSS_SELECTOR, value="h1[class='schema-header__title']")
    products = Finds(by=By.XPATH, value="//a[@data-bind='attr: {href: product.html_url}']/span/..")
    compare_button = Find(by=By.CSS_SELECTOR, value="a[class ='compare-button__sub compare-button__sub_main']")
    remove_compare_icon = Find(by=By.CSS_SELECTOR, value="a[title='Очистить список сравнения']")
    remove_compare_button = Find(by=By.CSS_SELECTOR, value="a[class='compare-button__sub']")

    def click_subsection_link(self, index):
        self.subsections[index].click()

    def click_product_link(self, index):
        wait(self.subsection_page_header.is_displayed)
        self.products[index].click()

    def click_compare(self):
        wait(self.compare_button.is_displayed)
        self.compare_button.click()

    def click_remove_compare_icon(self):
        wait(self.remove_compare_icon.is_displayed)
        self.remove_compare_icon.click()

    def click_remove_compare_button(self):
        wait(self.remove_compare_button.is_displayed)
        self.remove_compare_button.click()
