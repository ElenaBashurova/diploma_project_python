import pytest
from selene import browser
from diploma_project.utils import attach
from configs import config

LOGIN = "e_nikolaevnaya@mail.ru"
PASSWORD = "e_nikolaevnaya"
EMAIL = "e_nikolaevnaya@mail.ru"
API_URL = "ttps://demowebshop.tricentis.com"


@pytest.fixture(scope='function', autouse=True)
def browser_configs_api():
    browser.config.base_url = 'https://demowebshop.tricentis.com'
    browser.config.base_url = config.base_url_2

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()

