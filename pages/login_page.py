from selenium.webdriver.common.by import By
from webium import BasePage, Find


class LoginPageLocators(BasePage):
    log_in = Find(by=By.XPATH, value="//div[@class='auth-bar__item auth-bar__item--text']")

    username_input = Find(by=By.CSS_SELECTOR, value="input[type='text'][placeholder='Ник или e-mail']")
    password_input = Find(by=By.CSS_SELECTOR, value="input[type='password']")
    submit = Find(by=By.XPATH, value="//div/button")

    profile_icon = Find(by=By.CSS_SELECTOR, value='div[class="b-top-profile__image js-header-user-avatar"]')