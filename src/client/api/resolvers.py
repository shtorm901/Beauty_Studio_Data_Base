import requests
import settings
from src.server.database.pydantic_models import LoginData, User


def server_available(func):
    def need_it(*args, **kwargs):
        try:
            requests.get(url=settings.URL)
            return func(*args, **kwargs)
        except requests.exceptions.ConnectionError:
            return {'code': 400, 'msg': 'Server is not available', 'result': None}
    
    return need_it


@server_available
def check_connection():
    return True


@server_available
def login(password: str, login: str) -> dict:
    return requests.post(url=f'{settings.URL}/users/login', data=f'{{"login": "{login}", "password": "{password}"}}').json()


@server_available
def register(data: User) -> dict:
    return requests.post(url=f'{settings.URL}/users/', data=f'{{"id": 0, "position": "{data.position}", "login": "{data.login}", "password": "{data.password}", "power_level": {data.power_level}}}').json()


@server_available
def update_password(id: int, password: str) -> dict:
    return requests.put(url=f'{settings.URL}/users/change_password/{id}', data=f'{{"password": "{password}"}}').json()


def delete_account(id: int) -> dict:
    return requests.delete(url=f'{settings.URL}/users/{id}').json()