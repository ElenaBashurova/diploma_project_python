import allure
import pytest
from diploma_project.pages.select_category import category_name
from diploma_project.pages.main_page import main_page


@allure.tag('web')
@allure.label('layer', 'web')
@allure.label('owner', 'e_bashurova')
@allure.story('Выбор товара по категории')
@allure.link('https://www.officemag.ru', name='Test')
@allure.title('Проверка выбора категории "Деловые аксессуары"')
@pytest.mark.web
def test_check_category_product():
    main_page.open_page()
    main_page.product_category('Деловые аксессуары')


@allure.tag('web')
@allure.label('layer', 'web')
@allure.label('owner', 'e_bashurova')
@pytest.mark.web
@allure.title('Проверка выбора подкатегории "Портфели, сумки, папки из кожи"')
def test_check_subcategory_product():
    main_page.open_page()
    main_page.product_category('Деловые аксессуары')
    category_name.select_subcategory('Портфели, сумки, папки из кожи')


@allure.tag('web')
@allure.label('layer', 'web')
@allure.label('owner', 'e_bashurova')
@pytest.mark.web
@allure.title('Проверка выбора категории через поиск')
def test_check_search_category():
    main_page.open_page()
    main_page.search_product_by_button("Деловые аксессуары")
