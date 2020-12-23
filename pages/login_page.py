from selenium.webdriver.common.by import By
from webium import BasePage, Find


class LoginPage(BasePage):
    username_input = Find(by=By.CSS_SELECTOR, value="input[type='text'][placeholder='Ник или e-mail']")
    password_input = Find(by=By.CSS_SELECTOR, value="input[type='password']")
    submit_button = Find(by=By.XPATH, value="//div/button")

    def type_username(self, username):
        self.username_input.send_keys(username)

    def type_password(self, password):
        self.password_input.send_keys(password)

    def click_submit(self):
        self.submit_button.click()
