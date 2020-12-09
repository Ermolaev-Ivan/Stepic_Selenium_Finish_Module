from .base_page import BasePage
from .locators import BasketPageLocators



class BasketPage(BasePage):
    def basket_is_empty(self):
        self.go_to_basket()
        return self.is_not_element_present(*BasketPageLocators.BASKET_IS_EMPTY)

    def basket_is_full(self):
        self.go_to_basket()
        return self.is_not_element_present(*BasketPageLocators.BASKET_IS_FULL)
