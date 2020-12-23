from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds


class MainPage(BasePage):
    sections = Finds(by=By.XPATH, value="//ul[@class='b-main-navigation']/li/a")
    login_button = Find(by=By.XPATH, value="//div[@class='auth-bar__item auth-bar__item--text']")
    profile_icon = Find(by=By.CSS_SELECTOR, value='div[class="b-top-profile__image js-header-user-avatar"]')
    search_frame = Find(by=By.CSS_SELECTOR, value="iframe[class='modal-iframe']")
    cart = Find(by=By.XPATH, value="//div[@id='cart-desktop']/a")

    def click_login(self):
        self.login_button.click()

    def click_section_link(self, index):
        self.sections[index].click()

    def click_cart_link(self):
        self.cart.click()
