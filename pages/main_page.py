import allure
from pages.configs import Helpers
from selene import have
from selene import browser



class Page(Helpers):
    def open_page(self):
        with allure.step('https://www.officemag.ru'):
            browser.open('/')
            self.click_element('#fancybox-close')
            self.click_element('.js-cityDetector')
            self.click_element('#fancybox-close')
        return self

    def product_category(self, category_name):
        with allure.step(f'Выбрать из категорий: "{category_name}"'):
            self.click_element('.js-rubricatorButton')
            self.click_element('[alt="Деловые аксессуары"]')
        return self

    def search_product_by_button(self, product_name):
        with allure.step('На странице сделать клик на кнопку поиска'):
            self.click_element('[placeholder="Поиск по названию или коду товара"]')
        with allure.step(f'Ввести в строку поиска: "{product_name}"'):
            self.elements(".ui-autocomplete-input").set_value(product_name).press_enter()
            self.elements('.searchQuery').should(have.text('Вы искали'))
        return self


main_page = Page()