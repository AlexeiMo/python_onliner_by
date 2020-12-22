from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds


class SearchPage(BasePage):

    search_bar = Find(by=By.CSS_SELECTOR, value="input[class='search__input']")
    results = Finds(by=By.CSS_SELECTOR, value="a[class='product__title-link']")

    def type_search_option(self, name):
        self.search_bar.send_keys(name)

    def get_search_results(self):
        results = []
        for elem in self.results:
            results.append(elem.text)

        return results
