from selenium.webdriver.common.by import By
from webium import BasePage, Finds, Find


class ComparePageLocators(BasePage):
    section_link = Find(by=By.CSS_SELECTOR,
                   value="a[href='https://catalog.onliner.by/tv'][class ='catalog-bar__link catalog-bar__link_strong']")
    section_link2 = Find(by=By.CSS_SELECTOR, value="a[href='https://catalog.onliner.by/tv'][class='breadcrumbs__link']")
    products = Finds(by=By.XPATH, value="//a[@data-bind='attr: {href: product.html_url}']/span/..")
    compare_checkbox = Find(by=By.XPATH, value="//li[@id='product-compare-control']/label/span")
    compare_button = Find(by=By.CSS_SELECTOR, value="a[class ='compare-button__sub compare-button__sub_main']")
    compared_products = Finds(by=By.XPATH, value="//th[@class='product-table__cell']/div/div/a")
