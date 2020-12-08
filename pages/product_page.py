from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import time, math


class PageObject(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()
        self.browser.implicitly_wait(5)

    def get_price_product(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_IN_PRODUCT)
        return float(product_price.text.replace('£', ''))  # возврящаем цену товара

    def get_final_price(self):
        total_price = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_IN_BASKET)
        return float(total_price.text.split()[2].replace('£', ''))  # возвращаем значение корзины

    def should_be_price_and_price_in_basket(self):  # возможно следует добавить этот метод в add_to_basket..
        assert self.get_price_product() == self.get_final_price(), 'несоответствие цены товара и цены в корзине'

    def should_be_product_in_basket(self):
        """проверяем соответствует ли товар положенный в карзину тому что мы положили
        метод не работает если ткать не на основную кнопку продажи
        но в принципе проверяет функционал"""
        assert self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_IN_BASKET).text == \
               self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text, "The item in the cart does not match the added item"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
