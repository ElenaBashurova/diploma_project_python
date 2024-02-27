import allure
from pages.configs_helper import Helpers
from selene import browser, have


class ProductStock(Helpers):
    def open_page_stock(self):
        with allure.step('Открыть страницу Распродажи'):
            browser.open('/promo/sale/index.php?SORT=SORT&COUNT=60')
            self.click_element('#fancybox-close')
            self.click_element('.js-cityDetector')
            self.click_element('#fancybox-close')
        return self

    def select_stock_products(self, product):
        with allure.step(f'Выбрать товар по акции: "{product}"'):
            self.click_element('#bx_2973280320_8059059')
        return self

    def catalog_stock(self):
        with allure.step('Открыть страницу акции'):
            self.click_element('.js-tipTipActions')
        return self

    def check_name_product(self):
        with allure.step('Проверить продукт на странице'):
            self.elements(".js-productDetailCode").should(have.text('Код 531581'))
        return self



stock_page = ProductStock()
