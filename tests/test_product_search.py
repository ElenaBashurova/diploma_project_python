import allure
import pytest

from pages.product_pages import product_name
from pages.product_select import search_name


@allure.tag('web')
@allure.label('layer', 'web')
@allure.label('owner', 'e_bashurova')
@allure.story('Поиск товара')
@pytest.mark.xfail(reason='Этот тест не стабилен')
@allure.link('https://www.officemag.ru', name='Test')
@allure.title('Поиск товара "Кресло компьютерное"')
def test_furniture_category(browser_configs):
    search_name.open_page()
    search_name.search_product_enter("Кресло компьютерное")
    product_name.page_name_product("Кресло BRABIX «Fly MG-396», с подлокотниками, сетка, черное, 532083")


@allure.title('Поиск товара "Шкаф"')
def test_search_by_part_of_name(browser_configs):
    search_name.open_page()
    search_name.search_part_product('Шк')


@allure.title('Поиск товара "Кофе"')
def test_search_by_foreign_name(browser_configs):
    search_name.open_page()
    search_name.search_foreign_product('Кофе в зернах Якобс')
    product_name.foreign_name_product('Кофе в зернах JACOBS «Crema» 1 кг')


@pytest.mark.xfail(reason='Этот тест не стабилен')
@allure.title('Поиск товара "Чай"')
def test_search_by_foreign_keyboard_layout(browser_configs):
    search_name.open_page()
    search_name.search_keyboard_layout_product('Tea green')
