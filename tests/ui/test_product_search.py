import allure
import pytest
from diploma_project.pages.product_pages import product_name
from diploma_project.pages.product_select_page import search_name


@allure.tag('web')
@allure.label('layer', 'web')
@allure.label('owner', 'e_bashurova')
@allure.story('Поиск товара')
@pytest.mark.xfail(reason='Этот тест не стабилен')
@allure.link('https://www.officemag.ru', name='Test')
@allure.title('Проверка поиска товара "Кресло компьютерное"')
@pytest.mark.web
def test_check_search_product():
    search_name.open_page()
    search_name.search_product_enter("Кресло компьютерное")
    product_name.page_name_product("Кресло BRABIX «Tender MG-330», с подлокотниками, хром, черное, 531845")


@allure.tag('web')
@allure.label('layer', 'web')
@allure.label('owner', 'e_bashurova')
@pytest.mark.web
@allure.title('Проверка поиска товара "Шкаф(Стеллаж)"')
def test_check_search_closet():
    search_name.open_page()
    search_name.search_part_product('Шкаф(Стеллаж)')


@allure.tag('web')
@allure.label('layer', 'web')
@allure.label('owner', 'e_bashurova')
@pytest.mark.web
@allure.title('Проверка поиска категории товара "Кофе"')
def test_check_search_coffee():
    search_name.open_page()
    search_name.search_foreign_product('Кофе в зернах Якобс')
    product_name.foreign_name_product('Кофе в зернах JACOBS «Crema» 1 кг')


@allure.tag('web')
@allure.label('layer', 'web')
@allure.label('owner', 'e_bashurova')
@pytest.mark.web
@allure.title('Проверка поиска категории товара "Чай"')
def test_check_search_tea():
    search_name.open_page()
    search_name.search_keyboard_layout_product('Tea green')

