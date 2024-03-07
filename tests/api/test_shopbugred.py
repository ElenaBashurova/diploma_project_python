import json

import allure
import logging
import pytest
import requests
from allure_commons._allure import step
from diploma_project.utils.schema_api import product_create_post, product_create_post_fail, product_info_get, \
    product_info_get_fail, product_update_put, product_delete
from jsonschema import validate
from diploma_project.utils.utils_api import request_api



@pytest.mark.api
@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 'e_bashurova')
@allure.story('Создание товара')
@allure.title('Проверка создания товара')
def test_create_product():
    response = request_api('/create/', data={
        "name": "Джинсы",
        "section": "Брюки",
        "description": "Джинсы прямого кроя",
        "color": "BLUE",
        "size": 44
    })

    with allure.step('Статус код=200'):
        assert response.status_code == 200
    with allure.step('Проверка схемы удачное создание товара'):
        schema = response.json()
        validate(schema, product_create_post)
        assert response.json()
    with allure.step('Проверка статуса создания'):
        assert str(response.json()['status']) == 'ok'
    with allure.step('Проверка названия товара'):
        assert str(response.json()['result']['name']) == 'Джинсы'
    with allure.step('Проверка группы товара'):
        assert str(response.json()['result']['section']) == 'Брюки'
    with allure.step('Проверка описания товара'):
        assert str(response.json()['result']['description']) == 'Джинсы прямого кроя'
    with allure.step('Проверка цвета товара'):
        assert str(response.json()['result']['color']) == 'BLUE'
    with allure.step('Проверка размера товара'):
        assert str(response.json()['result']['size']) == '44'
    print()


@pytest.mark.api
@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 'e_bashurova')
@allure.story('Создание товара')
@allure.title('Проверка неудачного создания товара')
def test_fail_create_product():
    response = request_api('/create/', data={
        "name": "Джинсы",
        "section": "Брюки",
        "description": "",
        "color": "BLUE",
        "size": 44
    })
    with allure.step('Статус код=200'):
        assert response.status_code == 200
    with allure.step('Проверка схемы, неудачное создание товара'):
        schema = response.json()
        validate(schema, product_create_post_fail)
        assert response.json()
    with allure.step('Проверка статуса создания'):
        assert str(response.json()['status']) == 'error'
    with allure.step('Проверка сообщения ошибки'):
        assert str(response.json()['message']) == 'Описание товара не заполнено!'


@pytest.mark.api
@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 'e_bashurova')
@allure.story('Инфо о товаре')
@allure.title('Проверка информации о товаре')
def test_get_info_product():
    response = request_api('/get/', data={
        "id": 158,
        "name": "Брюки"
    })

    with allure.step('Статус код=200'):
        assert response.status_code == 200
    with allure.step('Проверка схемы инфо о товаре'):
        schema = response.json()
        validate(schema, product_info_get)
        assert response.json()
    with allure.step('Проверка статуса создания'):
        assert str(response.json()['status']) == 'ok'
    with allure.step('Проверка размера товара'):
        assert str(response.json()['result']['id']) == '158'
    with allure.step('Проверка названия товара'):
        assert str(response.json()['result']['name']) == 'Брюки'
    with allure.step('Проверка группы товара'):
        assert str(response.json()['result']['section']) == 'Брюки'
    with allure.step('Проверка описания товара'):
        assert str(response.json()['result']['description']) == 'Брюки прямые!'
    with allure.step('Проверка цвета товара'):
        assert str(response.json()['result']['color']) == 'BLUE'


@pytest.mark.api
@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 'e_bashurova')
@allure.story('Инфо о товаре')
@allure.title('Проверка неудачного получения информации о товаре')
def test_get_info_product_fail():
    response = request_api('/get/', data={
        "id": "",
        "name": "Брюки"
    })

    with allure.step('Статус код=200'):
        assert response.status_code == 200
    with allure.step('Проверка схемы, с неудачным получением информации о товаре'):
        schema = response.json()
        validate(schema, product_info_get_fail)
        assert response.json()
    with allure.step('Проверка статуса создания'):
        assert str(response.json()['status']) == 'error'
    with allure.step('Проверка сообщения ошибки'):
        assert str(response.json()['message']) == 'Поле ID товара  не заполнено'


@pytest.mark.api
@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 'e_bashurova')
@allure.story('Обновление товара на сайте')
@allure.title('Проверка обновления информации о товаре')
def test_put_update_product():
    response = request_api('/update/', data={
        "id": 158
    })

    with allure.step('Статус код=200'):
        assert response.status_code == 200
    with allure.step('Проверка схемы инфо о товаре'):
        schema = response.json()
        validate(schema, product_update_put)
        assert response.json()
    with allure.step('Проверка статуса создания'):
        assert str(response.json()['status']) == 'ok'
    with allure.step('Проверка сообщения от системы'):
        assert str(response.json()['result']) == 'Товар обновлен!'


@pytest.mark.api
@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 'e_bashurova')
@allure.story('Удаление товара на сайта')
@allure.title('Проверка удаления товара')
def test_delete_product():
    response = request_api('/delete/', data={
        "id": 174
    })

    with allure.step('Статус код=200'):
        assert response.status_code == 200
    with allure.step('Проверка схемы, удаления товара'):
        schema = response.json()
        validate(schema, product_delete)
        assert response.json()
    with allure.step('Проверка статуса удаления'):
        assert str(response.json()['status']) == 'error'
