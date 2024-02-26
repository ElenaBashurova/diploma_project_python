import allure
from pages.configs import Helpers
from selene import have
from selene import browser



class ProductPage(Helpers):
    def open_page(self):
        with allure.step('https://www.officemag.ru'):
            browser.open('/')
            self.click_element('#fancybox-close')
            self.click_element('.js-cityDetector')
            self.click_element('#fancybox-close')
        return self

    def page_name_product(self, name):
        with (allure.step(f'Страница "{name}" открыта')):
            self.elements('.ProductHead__name').should(have.text(name))
        return self


    def foreign_name_product(self, foreign_name):
        with (allure.step(f'Страница "{foreign_name}" открыта')):
            self.elements('.ProductHead__name').should(have.text(foreign_name))
        return self


product_name = ProductPage()