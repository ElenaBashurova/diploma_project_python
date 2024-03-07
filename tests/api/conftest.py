import pytest
from dotenv import load_dotenv

LOGIN = "e_nikolaevnaya@mail.ru"
PASSWORD = "e_nikolaevnaya"
EMAIL = "e_nikolaevnaya@mail.ru"
API_URL = "http://shop.bugred.ru"


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


