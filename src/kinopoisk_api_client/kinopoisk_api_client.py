import apischema

from src.kinopoisk_api_client.client.films_api_client import FilmsApiClient
from src.kinopoisk_api_client.client.http_client import HttpClient


class KinopoiskApiClient:
    __base_url: str = 'https://kinopoiskapiunofficial.tech'
    __films: FilmsApiClient

    def __init__(self, token: str) -> None:
        http_client = HttpClient(self.__base_url)
        apischema.settings.camel_case = True
        self.__films = FilmsApiClient(http_client, apischema, token)

    @property
    def films(self) -> FilmsApiClient:
        return self.__films
