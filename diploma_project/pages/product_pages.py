import allure
from selene import have
from selene import browser


class ProductPage:
    def open_page(self):
        with allure.step('Открыть страницу https://www.officemag.ru'):
            browser.open('/')
            browser.element('#fancybox-close').click()
            browser.element('.js-cityDetector').click()
            browser.element('#fancybox-close').click()
        return self

    def page_name_product(self, name):
        with (allure.step(f'Страница "{name}" открыта')):
            browser.element('.ProductHead__name').should(have.text(name))
        return self

    def foreign_name_product(self, foreign_name):
        with (allure.step(f'Страница "{foreign_name}" открыта')):
            browser.element('.ProductHead__name').should(have.text(foreign_name))
        return self


product_name = ProductPage()
