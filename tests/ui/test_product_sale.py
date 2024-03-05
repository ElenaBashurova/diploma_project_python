import allure
import pytest

from diploma_project.pages.stock_product import stock_page
from diploma_project.pages.main_page import main_page


@allure.tag('web')
@allure.label('layer', 'web')
@allure.label('owner', 'e_bashurova')
@allure.story('Выбор товара по акции')
@allure.link('https://www.officemag.ru', name='Test')
@allure.title('Проверка выбора товара')
@pytest.mark.web
def test_check_choice_product():
    main_page.open_page()
    stock_page.catalog_stock()


@allure.tag('web')
@allure.label('layer', 'web')
@allure.label('owner', 'e_bashurova')
@pytest.mark.web
@allure.title('Проверка выбора товара из категории "Распродажи"')
def test_check_product_stock():
    stock_page.open_page_stock()
    stock_page.select_stock_products('Кресло компьютерное')


@allure.tag('web')
@allure.label('layer', 'web')
@allure.label('owner', 'e_bashurova')
@pytest.mark.web
@allure.title('Проверка продукта на странице')
def test_check_product():
    stock_page.open_page_stock()
    stock_page.select_stock_products('Кресло компьютерное')
    stock_page.check_name_product()
