import allure
import logging
import pytest
import requests
from allure_commons._allure import step
import diploma_project.utils.schema
from tests.api.conftest import LOGIN, PASSWORD, EMAIL
from diploma_project.utils.utils_api import get_cookie
from jsonschema import validate


@pytest.mark.api
@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 'e_bashurova')
@allure.story('Авторизация')
@allure.title('Авторизация на сайте')
def test_page_login():
    with step("Авторизация с API"):
        response = get_cookie("/login", json={"Email": LOGIN, "Password": PASSWORD}, allow_redirects=False)
    cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    logging.info(cookie)
    with allure.step('Статус код=302'):
        assert response.status_code == 302



@pytest.mark.api
@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 'e_bashurova')
@allure.story('Корзина')
@allure.title('Добавить товар в корзину')
def test_add_product_in_cart():
    with step("Добавить продукт в корзину"):
        response = get_cookie("/addproducttocart/catalog/45/1/1", data={
            "addtocart_45.EnteredQuantity": 4}, allow_redirects=False)
    cookie = response.cookies.get("Nop.customer")
    logging.info(cookie)
    with allure.step('Статус код=200'):
        assert response.status_code == 200

    data_user = {'title': 'str', "type": "object"}
    response = requests.post('https://demowebshop.tricentis.com/addproducttocart/catalog/45/1/1', data=data_user,
                             verify=False)
    body = response.json()
    validate(body, schema=diploma_project.utils.schema.item_post)
    with allure.step('Проверка схемы'):
        assert response.status_code == 200



@pytest.mark.api
@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 'e_bashurova')
@allure.story('Корзина')
@allure.title('Неудачное добавление товара в корзину')
def test_add_product_in_cart_fail():
    with step("Добавить продукт в корзину"):
        response = get_cookie("/addproducttocart/details/1/2", data={
            "addtocart_2.EnteredQuantity": 1})
    cookie = response.cookies.get("Nop.customer")
    logging.info(cookie)
    with allure.step('Статус код=200'):
        assert response.status_code == 200

    data_user = {'title': 'str', "type": "object"}
    response = requests.post('https://demowebshop.tricentis.com/addproducttocart/details/1/2', data=data_user,
                             verify=False)
    body = response.json()
    validate(body, schema=diploma_project.utils.schema.item_post_fail)
    with allure.step('Проверка схемы'):
        assert response.status_code == 200



@pytest.mark.api
@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 'e_bashurova')
@allure.story('Поиск')
@allure.title('Найти интересующий товар')
def test_search_product():
    with step("Найти продукт"):
        response = get_cookie("/catalog/searchtermautocomplete", data={
            "term": 'Computer'})
    cookie = response.cookies.get("Nop.customer")
    logging.info(cookie)
    with allure.step('Статус код=200'):
        assert response.status_code == 200



@pytest.mark.api
@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 'e_bashurova')
@allure.story('Email')
@allure.title('Отправить email')
def test_mail_send():
    with step("Отправить письмо на емайл"):
        response = get_cookie("/subscribenewsletter", json={"Email": EMAIL}, allow_redirects=False)
    cookie = response.cookies.get("Nop.customer")
    logging.info(cookie)
    with allure.step('Статус код=200'):
        assert response.status_code == 200

