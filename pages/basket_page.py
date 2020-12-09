from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException


class BasketPage(BasePage):
    def basket_is_empty(self):
        self.go_to_basket()
        try:
            assert self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE)
        except NoSuchElementException():
            return False

        return True

    def basket_is_full(self):
        self.go_to_basket()
        try:
            assert self.browser.find_element(*BasketPageLocators.BASKET_IS_FULL)
        except NoSuchElementException():
            return False
        return True
