import logging
import allure
import curlify
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType


def request_api(url, **kwargs):
    base_url = "http://shop.bugred.ru/api/items"
    with step(f"POST {url}"):
        result = requests.post(base_url + url, **kwargs)
        curl = curlify.to_curl(result.request)
        allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
        logging.info(curlify.to_curl(result.request))
    return result
