import requests
import random
import string
import pytest

from helpers import Helpers


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
@pytest.fixture(scope='function')
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return login_pass


@pytest.fixture(scope='function')
def correct_payload_for_creating_courier():

    payload_for_create = {
        "login": Helpers.login,
        "password": Helpers.password,
        "firstName": Helpers.first_name
    }

    yield payload_for_create

    payload_for_login = {
        "login": Helpers.login,
        "password": Helpers.password
    }

    login_response = requests.post(f'{Helpers.BASE_URL}/api/v1/courier/login', data=payload_for_login)
    courier_id = login_response.json()["id"]
    requests.delete(f'{Helpers.BASE_URL}/api/v1/courier/{courier_id}')
