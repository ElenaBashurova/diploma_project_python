import allure
from diploma_project.utils.configs_helper import Helpers
from selene import have
from selene import browser


class Page:
    def open_page(self):
        with allure.step('Открыть страницу https://www.officemag.ru'):
            browser.open('/')
            browser.element('#fancybox-close').click()
            browser.element('.js-cityDetector').click()
            browser.element('#fancybox-close').click()
        return self

    def product_category(self, category_name):
        with allure.step(f'Выбрать из категорий: "{category_name}"'):
            browser.element('.js-rubricatorButton').click()
            browser.element('[alt="Деловые аксессуары"]').click()
        return self

    def search_product_by_button(self, product_name):
        with allure.step('На странице сделать клик на кнопку поиска'):
            browser.element('[placeholder="Поиск по названию или коду товара"]').click()
        with allure.step(f'Ввести в строку поиска: "{product_name}"'):
            browser.element(".ui-autocomplete-input").set_value(product_name).press_enter()
            browser.element('.searchQuery').should(have.text('Вы искали')).click()
        return self


main_page = Page()
