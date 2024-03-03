import pytest
from selene import browser
from selenium import webdriver
from utils import attach
from configs import config, setting

LOGIN = "e_nikolaevnaya@mail.ru"
PASSWORD = "e_nikolaevnaya"
EMAIL = "e_nikolaevnaya@mail.ru"
API_URL = "ttps://demowebshop.tricentis.com"


@pytest.fixture()
def browser_configs_api():
    browser.config.base_url = 'https://demowebshop.tricentis.com'
    browser.config.base_url = config.base_url_2
    browser.config.timeout = config.timeout
    browser.config.window_height = config.window_height
    browser.config.window_width = config.window_width
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = config.load_strategy
    browser.config.driver_options = driver_options

    if config.environment == 'remote':
        selenoid_capabilities = {
            "browserName": config.driver_name,
            "browserVersion": config.remote_version,
            "selenoid:options": {
                "enableVNC": config.remote_enableVNC,
                "enableVideo": config.remote_enableVideo
            }
        }

        driver_options.capabilities.update(selenoid_capabilities)

        driver = webdriver.Remote(
            command_executor=setting(),
            options=driver_options
        )

        browser.config.driver = driver

    else:
        browser.config.driver_name = config.driver_name

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()

