import allure
from pages.configs_helper import Helpers
from selene import browser



class PageProduct(Helpers):
    def open_page(self):
        with allure.step('Открыть страницу https://www.officemag.ru'):
            browser.open('/')
            self.click_element('#fancybox-close')
            self.click_element('.js-cityDetector')
            self.click_element('#fancybox-close')
        return self


    def search_product_enter(self, product_name):
        with allure.step('На странице сделать клик на кнопку поиска'):
            self.click_element('[placeholder="Поиск по названию или коду товара"]')
        with allure.step(f'Ввести в строку поиска: "{product_name}"'):
            self.elements(".ui-autocomplete-input").set_value(product_name).press_enter()
        with allure.step('Выбрать товар'):
            self.click_element("#bx_2973280320_11276354")
        return self

    def search_part_product(self, part_name):
        with allure.step('На странице сделать клик на кнопку поиска'):
            self.click_element('[placeholder="Поиск по названию или коду товара"]')
        with allure.step(f'Ввести в строку поиска: "{part_name}"'):
            self.elements(".ui-autocomplete-input").set_value(part_name).press_enter()
        with allure.step('Выбрать товар'):
            self.click_element("#bx_2973280320_262114")
        return self

    def search_foreign_product(self, foreign_name):
        with allure.step('На странице сделать клик на кнопку поиска'):
            self.click_element('[placeholder="Поиск по названию или коду товара"]')
        with allure.step(f'Ввести в строку поиска: "{foreign_name}"'):
            self.elements(".ui-autocomplete-input").set_value(foreign_name).press_enter()
        with allure.step('Выбрать товар'):
            self.click_element("#bx_2973280320_11393299")
        return self

    def search_keyboard_layout_product(self, keyboard_layout_name):
        with allure.step('На странице сделать клик на кнопку поиска'):
            self.click_element('[placeholder="Поиск по названию или коду товара"]')
        with allure.step(f'Ввести в строку поиска: "{keyboard_layout_name}"'):
            self.elements(".ui-autocomplete-input").set_value(keyboard_layout_name).press_enter()
        with allure.step('Выбрать товар'):
            self.click_element("#bx_2973280320_3936895")
        return self


search_name = PageProduct()