from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_SUBSTRING = 'login'
    REGISTER_EMAIL_FIELD = (By.TAG_NAME, 'input[id="id_registration-email"]')
    REGISTER_PASSWORD_FIELD_1 = (By.TAG_NAME, 'input[id="id_registration-password1"]')
    REGISTER_PASSWORD_FIELD_2 = (By.TAG_NAME, 'input[id="id_registration-password2"]')
    REGISTER_BUTTON = (By.TAG_NAME, 'button[name="registration_submit"]')
    LOGIN_EMAIL_FIELD = (By.TAG_NAME, 'input[id="id_login-username"]')
    LOGIN_PASSWORD_FIELD = (By.TAG_NAME, 'input[id="id_login-password"]')
    MESSAGE_REGISTER = (By.TAG_NAME, 'div[class="alertinner wicon"]')


class ProductPageLocators:
    NAME_PRODUCT = (By.TAG_NAME, 'div[class="col-sm-6 product_main"]>h1')
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    PRICE_PRODUCT = (By.TAG_NAME,
                     'div[class="col-sm-6 product_main"]>p[class="price_color"]')
    TOTAL_PRICE_IN_BASKET = (By.CSS_SELECTOR,  # удалить как сделаю классы BasketPage
                             '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs')
    # альтернативный адрес по Xpath //*[@id="default"]/header/div[1]/div/div[@class="basket-mini pull-right hidden-xs"]/text()
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,
                       '#messages > div:nth-child(1) > div > strong')
    PRODUCT_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')


class BasketPageLocators:
    BASKET_BUTTON = (By.TAG_NAME, 'a[class="btn btn-default"]')
    BASKET_TOTAL = (By.CSS_SELECTOR,
                    '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs')
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')
    BASKET_IS_FULL = (By.ID, 'basket_formset')
