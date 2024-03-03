import pytest
from selene import browser
from utils import attach

LOGIN = "e_nikolaevnaya@mail.ru"
PASSWORD = "e_nikolaevnaya"
EMAIL = "e_nikolaevnaya@mail.ru"
API_URL = "ttps://demowebshop.tricentis.com"


@pytest.fixture()
def browser_configs():
    browser.config.base_url = 'https://demowebshop.tricentis.com'

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
