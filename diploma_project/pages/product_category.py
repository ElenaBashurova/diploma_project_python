import allure
from selene import browser



class ChapterProducts:

    def open_page_heaters(self):
        browser.open('/')
        with allure.step('Страница "Обогреватели" открыта'):
            browser.element('.js-rubricatorButton').click()
            browser.element('[data-id="458731"]').click()

    def select_first_product(self):
        with allure.step('Выбор первого товара'):
            browser.element('.js-rubricatorButton').click()
            browser.element('[data-id="458731"]').click()
            browser.element("#bx_2973280320_8138402").click()


category_p = ChapterProducts()
