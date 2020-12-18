from selenium.webdriver.common.by import By
from webium import BasePage, Find


class OrderPageLocators(BasePage):
    traders_link = Find(by=By.XPATH,
                        value="//a/span[.='Предложения продавцов']/..")

    buy_button = Find(by=By.XPATH,
                      value="//div[@class='offers-list__control offers-list__control_default']/a")

    cart_link = Find(by=By.XPATH, value="//div[@id='cart-desktop']/a")

    order_link = Find(by=By.CSS_SELECTOR,
                      value="a[class='button-style button-style_primary button-style_small cart-form__button']")

    remove = Find(by=By.XPATH, value="//div[@class='cart-form__offers-part cart-form__offers-part_remove']/div/a")
    remove_field = Find(by=By.XPATH, value="//div[@class='cart-form__control']//input")
