import os
from typing import Literal, Optional
from pydantic_settings import BaseSettings
from diploma_project.utils import path
from dotenv import load_dotenv



def setting():
    load_dotenv()
    login: str = os.getenv("LOGIN")
    password: str = os.getenv("PASSWORD")
    url: str = os.getenv("URL")
    remote_url = f'{url}'
    return remote_url


class Config(BaseSettings):
    context: Literal['stage', 'local'] = 'local'
    environment: Literal['remote', 'local'] = 'local'

    base_url: str = 'https://www.officemag.ru'
    base_url_2: str = 'https://demowebshop.tricentis.com'
    driver_name: str = 'chrome'
    load_strategy: str = 'eager'
    window_width: int = 1920
    window_height: int = 1080
    timeout: float = 10.0

    remote_version: Optional[str] = '121.0'
    remote_enableVNC: bool = True
    remote_enableVideo: bool = True


config = Config(_env_file=path.relative_from_root(f'.env.{Config().context}'))
