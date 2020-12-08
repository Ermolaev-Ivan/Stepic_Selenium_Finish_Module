from .base_page import BasePage
from .locators import ProductPageLocators
import time


class PageObject(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()
        time.sleep(5)
        self.should_be_product_in_basket()
        assert self.get_price_product() == self.get_final_price(), 'несоответствие цены товара и цены в корзине'

    """получение цены товара и корзины, могут нам еще понадобиться"""
    def get_price_product(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_IN_PRODUCT)
        return float(product_price.text.replace('£', ''))  # возврящаем цену товара

    def get_final_price(self):
        total_price = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_IN_BASKET)
        return float(total_price.text.split()[2].replace('£', ''))  # возвращаем значение корзины

    def should_be_product_in_basket(self):
        """проверяем соответствует ли товар положенный в карзину тому что мы положили
        метод не работает если ткать не на основную кнопку продажи
        но в принципе проверяет функционал"""
        assert self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_IN_BASKET).text == \
               f'{self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text} has been added to your basket.'
