import allure
from selene import browser



class PageProduct:
    def open_page(self):
        with allure.step('Открыть страницу https://www.officemag.ru'):
            browser.open('/')
            browser.element('#fancybox-close').click()
            browser.element('.js-cityDetector').click()
            browser.element('#fancybox-close').click()
        return self


    def search_product_enter(self, product_name):
        with allure.step('На странице сделать клик на кнопку поиска'):
            browser.element('[placeholder="Поиск по названию или коду товара"]').click()
        with allure.step(f'Ввести в строку поиска: "{product_name}"'):
            browser.element(".ui-autocomplete-input").set_value(product_name).press_enter()
        with allure.step('Выбрать товар'):
            browser.element("#bx_2973280320_11276354").click()
        return self

    def search_part_product(self, part_name):
        with allure.step('На странице сделать клик на кнопку поиска'):
            browser.element('[placeholder="Поиск по названию или коду товара"]').click()
        with allure.step(f'Ввести в строку поиска: "{part_name}"'):
            browser.element(".ui-autocomplete-input").set_value(part_name).press_enter()
        with allure.step('Выбрать товар'):
            browser.element("#bx_2973280320_262114").click()
        return self

    def search_foreign_product(self, foreign_name):
        with allure.step('На странице сделать клик на кнопку поиска'):
            browser.element('[placeholder="Поиск по названию или коду товара"]').click()
        with allure.step(f'Ввести в строку поиска: "{foreign_name}"'):
            browser.element(".ui-autocomplete-input").set_value(foreign_name).press_enter()
        with allure.step('Выбрать товар'):
            browser.element("#bx_2973280320_11393299").click()
        return self

    def search_keyboard_layout_product(self, keyboard_layout_name):
        with allure.step('На странице сделать клик на кнопку поиска'):
            browser.element('[placeholder="Поиск по названию или коду товара"]').click()
        with allure.step(f'Ввести в строку поиска: "{keyboard_layout_name}"'):
            browser.element(".ui-autocomplete-input").set_value(keyboard_layout_name).press_enter()
        with allure.step('Выбрать товар'):
            browser.element("#bx_2973280320_3936895").click()
        return self


search_name = PageProduct()