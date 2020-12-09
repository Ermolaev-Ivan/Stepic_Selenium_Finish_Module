from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        self.browser.implicitly_wait(5)

    def get_price_product(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        return float(product_price.text.replace('£', ''))  # возврящаем цену товара

    def get_final_price(self):
        total_price = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_IN_BASKET)
        return float(total_price.text.split()[2].replace('£', ''))  # возвращаем значение корзины

    def should_be_price_and_price_in_basket(self):  # возможно следует добавить этот метод в add_to_basket..
        assert self.get_price_product() == self.get_final_price(), 'несоответствие цены товара и цены в корзине'

    def should_be_product_in_basket(self):
        """проверяем соответствует ли товар положенный в корзину тому что мы положили
        метод не работает если тыкать не на основную кнопку продажи
        но в принципе проверяет функционал"""
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_IN_SUCCESS_MESSAGE).text == \
               self.browser.find_element(
                   *ProductPageLocators.NAME_PRODUCT).text, "The item in the cart does not match the added item"

    def should_not_be_success_message(self):
        return self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
               "Success message is presented, but should not be"

    def should_is_disappeared(self):
        return self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
               "The success message does not disappear, but should"
