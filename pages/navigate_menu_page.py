from selenium.webdriver.common.by import By
from webium import BasePage, Find


class NavigateMenuPageLocators(BasePage):
    tab_link = Find(by=By.CSS_SELECTOR, value="a[href='https://catalog.onliner.by/']")
