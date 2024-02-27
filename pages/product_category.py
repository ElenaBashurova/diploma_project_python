import allure
from selene import browser
from pages.configs_helper import Helpers


class ChapterProducts(Helpers):

    def open_page_heaters(self):
        browser.open('/')
        with allure.step('Страница "Обогреватели" открыта'):
            self.click_element('.js-rubricatorButton')
            self.click_element('[data-id="458731"]')

    def select_first_product(self):
        with allure.step('Выбор первого товара'):
            self.click_element('.js-rubricatorButton')
            self.click_element('[data-id="458731"]')
            self.click_element("#bx_2973280320_8138402")


category_p = ChapterProducts()
