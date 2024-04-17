import json
import allure
import pytest
import requests

from helpers import Helpers


class TestCreateOrderEndpoint:
    orders_endpoint = f"{Helpers.BASE_URL}/api/v1/orders"

    @allure.title('Проверка требований: «можно указать один из цветов — BLACK или GREY» и «тело ответа содержит track»')
    @allure.link(f'{Helpers.BASE_URL}/docs/#api-Orders-CreateOrder',
                 name='Ссылка на документацию эндпоинта Создание заказа')
    @pytest.mark.parametrize('colours', ["BLACK", "GREY"])
    def test_create_order_return_201(self, colours):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                colours
            ]
        }

        json_payload = json.dumps(payload)

        response = requests.post(TestCreateOrderEndpoint.orders_endpoint, data=json_payload)

        assert response.status_code == 201 and 'track' in response.text

    @allure.title('Проверка требования: «можно совсем не указывать цвет»')
    @allure.link(f'{Helpers.BASE_URL}/docs/#api-Orders-CreateOrder',
                 name='Ссылка на документацию эндпоинта Создание заказа')
    def test_create_order_without_color_return_201(self):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha"
        }

        response = requests.post(TestCreateOrderEndpoint.orders_endpoint, data=payload)

        assert response.status_code == 201

    @allure.title('Проверка требования: «можно указать оба цвета»')
    @allure.link(f'{Helpers.BASE_URL}/docs/#api-Orders-CreateOrder',
                 name='Ссылка на документацию эндпоинта Создание заказа')
    def test_create_order_with_two_colours_return_201(self):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                "BLACK", "GREY"
            ]
        }

        json_payload = json.dumps(payload)

        response = requests.post(TestCreateOrderEndpoint.orders_endpoint, data=json_payload)

        assert response.status_code == 201
