from .pages.product_page import PageObject
from .pages.base_page import BasePage
from .pages.locators import ProductPageLocators


# def test_guest_can_add_product_to_basket(browser):  # получаем число для степика)
#     link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear'
#     page = PageObject(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'
    page = PageObject(browser, link)
    page.open()
    page.add_to_basket()
