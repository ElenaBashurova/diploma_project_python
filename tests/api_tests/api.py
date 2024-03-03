import allure
import logging
import pytest
import requests
from allure_commons._allure import step
import utils.schema
from tests.api_tests.conftest import LOGIN, PASSWORD, EMAIL
from selene import browser, have
from utils.utils_api import post_reqres
from jsonschema import validate


@pytest.mark.api
@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 'e_bashurova')
@allure.story('Авторизация на сайте')
def test_page_login(browser_configs):
    with step("Авторизация с API"):
        response = post_reqres("/login", json={"Email": LOGIN, "Password": PASSWORD}, allow_redirects=False)
    cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    logging.info(cookie)
    with allure.step('Статус код=302'):
        assert response.status_code == 302
    with step("Открыть главную страницу авторизации UI"):
        browser.open('/')
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        browser.element('.ico-login').click()
        browser.element(".page-title").should(have.text('Welcome, Please Sign In!'))


@pytest.mark.api
@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 'e_bashurova')
@allure.story('Добавить товар в корзину')
def test_add_product_in_cart(browser_configs):
    with step("Добавить продукт в корзину"):
        response = post_reqres("/addproducttocart/catalog/45/1/1", data={
            "addtocart_45.EnteredQuantity": 4}, allow_redirects=False)
    cookie = response.cookies.get("Nop.customer")
    logging.info(cookie)
    with allure.step('Статус код=200'):
        assert response.status_code == 200

    data_user = {'title': 'str', "type": "object"}
    response = requests.post('https://demowebshop.tricentis.com/addproducttocart/catalog/45/1/1', data=data_user,
                             verify=False)
    body = response.json()
    validate(body, schema=utils.schema.item_post)
    with allure.step('Проверка схемы'):
        assert response.status_code == 200
    with step("Открыть главную страницу, забрать кукки"):
        browser.open('/')
        browser.driver.add_cookie({"name": "Nop.customer", "value": cookie})

    with step("Открыть карточку товара"):
        browser.open('/books')

    with step("Проверить продукт"):
        browser.element('.product-title').should(have.text('Computing and Internet'))


@pytest.mark.api
@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 'e_bashurova')
@allure.story('Неудачное добавление товара в корзину')
def test_add_product_in_cart_fail(browser_configs):
    with step("Добавить продукт в корзину"):
        response = post_reqres("/addproducttocart/details/1/2", data={
            "addtocart_2.EnteredQuantity": 1})
    cookie = response.cookies.get("Nop.customer")
    logging.info(cookie)
    with allure.step('Статус код=200'):
        assert response.status_code == 200

    data_user = {'title': 'str', "type": "object"}
    response = requests.post('https://demowebshop.tricentis.com/addproducttocart/details/1/2', data=data_user,
                             verify=False)
    body = response.json()
    validate(body, schema=utils.schema.item_post_fail)
    with allure.step('Проверка схемы'):
        assert response.status_code == 200
    with step("Открыть главную страницу, забрать кукки"):
        browser.open('/')
        browser.driver.add_cookie({"name": "Nop.customer", "value": cookie})

    with step("Открыть карточку товара"):
        browser.open('/5-virtual-gift-card')

    with step("Добавить товар"):
        browser.element('#add-to-cart-button-1').click()

    with step("Неудачное добавление товара"):
        browser.element('#bar-notification').should(have.text('Enter valid recipient email'))


@pytest.mark.api
@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 'e_bashurova')
@allure.story('Найти интересующий товар')
def test_search_product(browser_configs):
    with step("Найти продукт"):
        response = post_reqres("/catalog/searchtermautocomplete?term=Computer", data={
            "term": 'Computer'})
    cookie = response.cookies.get("Nop.customer")
    logging.info(cookie)
    with allure.step('Статус код=200'):
        assert response.status_code == 200

    with step("Открыть главную страницу, забрать кукки"):
        browser.open('/')
        browser.driver.add_cookie({"name": "Nop.customer", "value": cookie})
    with step("В поиске ввести товар"):
        browser.element('#small-searchterms').type("Computer")
    with step("Найти товар"):
        browser.element('.search-box-button').click()


@pytest.mark.api
@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 'e_bashurova')
@allure.story('Отправить email')
def test_mail_send(browser_configs):
    with step("Отправить письмо на емайл"):
        response = post_reqres("/subscribenewsletter", json={"Email": EMAIL}, allow_redirects=False)
    cookie = response.cookies.get("Nop.customer")
    logging.info(cookie)
    with allure.step('Статус код=200'):
        assert response.status_code == 200
    with step("Открыть главную страницу авторизации UI"):
        browser.open('/')
        browser.driver.add_cookie({"name": "Nop.customer", "value": cookie})
    with step("Отправить письмо"):
        browser.element('#newsletter-email').type("e_nikolaevnaya@mail.ru")
        browser.element('#newsletter-subscribe-button').click()
    with step("Проверка, что письмо отправлено"):
        browser.element("#newsletter-result-block").should(have.text('Thank you for signing up! A verification '
                                                                     'email has been sent. We appreciate your '
                                                                     'interest.'))
