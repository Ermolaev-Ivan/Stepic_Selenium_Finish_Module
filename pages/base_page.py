# Для начала сделаем базовую страницу, от которой будут унаследованы все остальные классы.
# В ней мы опишем вспомогательные методы для работы с драйвером.
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)   # неявное ожидание

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
