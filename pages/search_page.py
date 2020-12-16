from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds


class SearchPageLocators(BasePage):
    search_frame = Find(by=By.CSS_SELECTOR, value="iframe[class='modal-iframe']")
    search_bar = Find(by=By.CSS_SELECTOR, value="input[class='search__input']")
    results = Finds(by=By.CSS_SELECTOR, value="a[class='product__title-link']")
