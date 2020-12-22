from selenium.webdriver.common.by import By
from webium import BasePage, Finds, Find


class ComparePage(BasePage):
    compare_page_title = Find(by=By.CSS_SELECTOR, value="h1[class='b-offers-title']")
    compared_products = Finds(by=By.XPATH, value="//th[@class='product-table__cell']/div/div/a")

    def get_product_name(self, index):
        return self.compared_products[index].text
