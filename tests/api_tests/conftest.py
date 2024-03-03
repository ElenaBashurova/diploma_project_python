import pytest
from selene import browser
from selenium import webdriver
from configs import config, setting



LOGIN = "e_nikolaevnaya@mail.ru"
PASSWORD = "e_nikolaevnaya"
EMAIL = "e_nikolaevnaya@mail.ru"
API_URL = "ttps://demowebshop.tricentis.com"


@pytest.fixture()
def browser_configs():
    browser.config.base_url = 'https://demowebshop.tricentis.com'

