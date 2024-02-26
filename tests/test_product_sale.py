import allure
import pytest
from pages.stock_product import stock_page
from pages.main_page import main_page



@allure.tag('web')
@allure.label('layer', 'web')
@allure.label('owner', 'e_bashurova')
@allure.story('Выбор товара по акции')
@allure.link('https://www.officemag.ru', name='Test')
@allure.title('Выбор товара, по низкой цене')
def test_product_stock(browser_configs):
    main_page.open_page()
    stock_page.catalog_stock()


@allure.title('Выбор товара из категории "Распродажи"')
def test_product_recommendation(browser_configs):
    stock_page.open_page_stock()
    stock_page.select_stock_products('Кресло компьютерное')


@allure.title('Проверить продукт на странице')
def test_product_recommendation(browser_configs):
    stock_page.open_page_stock()
    stock_page.select_stock_products('Кресло компьютерное')
    stock_page.check_name_product()