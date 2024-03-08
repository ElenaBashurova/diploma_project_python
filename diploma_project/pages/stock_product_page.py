import allure
from selene import browser, have


class ProductStock:
    def open_page_stock(self):
        with allure.step('Открыть страницу Распродажи'):
            browser.open('/promo/sale/index.php?SORT=SORT&COUNT=60')
            browser.element('#fancybox-close').click()
            browser.element('.js-cityDetector').click()
            browser.element('#fancybox-close').click()
        return self

    def select_stock_products(self, product):
        with allure.step(f'Выбрать товар по акции: "{product}"'):
            browser.element('#bx_2973280320_8059059').click()
        return self

    def catalog_stock(self):
        with allure.step('Открыть страницу акции'):
            browser.element('.js-tipTipActions').click()
        return self

    def check_name_product(self):
        with allure.step('Проверить продукт на странице'):
            browser.element(".js-productDetailCode").should(have.text('Код 531581'))
        return self



stock_page = ProductStock()
