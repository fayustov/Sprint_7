import pytest
import requests
import allure

from helpers import Helpers


class TestCreateCourierEndpoint:

    create_endpoint_url = f"{Helpers.BASE_URL}/api/v1/courier"

    @allure.title('Проверка требований: «курьера можно создать», «запрос возвращает правильный код ответа», '
                  '«успешный запрос возвращает {"ok":true}», метод Создание курьера')
    @allure.link(f'{Helpers.BASE_URL}/docs/#api-Courier-CreateCourier',
                 name='Ссылка на документацию эндпоинта Создание курьера')
    def test_create_courier_with_correct_payload_return_ok_and_201(self, correct_payload_for_creating_courier):

        response = requests.post(TestCreateCourierEndpoint.create_endpoint_url,
                                 data=correct_payload_for_creating_courier)

        assert response.status_code == 201 and response.text == '{"ok":true}', \
            f"status code is {response.status_code}, response text is {response.text}"

    @allure.title('Проверка требований: «нельзя создать двух одинаковых курьеров» и '
                  '«если создать пользователя с логином, который уже есть, возвращается ошибка»')
    @allure.link(f'{Helpers.BASE_URL}/docs/#api-Courier-CreateCourier',
                 name='Ссылка на документацию эндпоинта Создание курьера')
    def test_create_two_alike_couriers_return_409(self, correct_payload_for_creating_courier):

        # Создаём первого курьера
        response1 = requests.post(TestCreateCourierEndpoint.create_endpoint_url,
                                  data=correct_payload_for_creating_courier)

        # Создаём второго курьера с теми же данными
        response2 = requests.post(TestCreateCourierEndpoint.create_endpoint_url,
                                  data=correct_payload_for_creating_courier)

        error_text = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'

        # Проверяем, что первый курьер корректно создался и попытка создать второго курьера вернёт 409-й статус-код
        # и текст с ошибкой
        assert response1.status_code == 201 and response2.status_code == 409 and response2.text == error_text, \
            f"response1 status code is {response1.status_code}, response2 status_code is {response2.status_code}, " \
            f"response2 text is {response2.text}"

    @allure.title('Проверка требований: «чтобы создать курьера, нужно передать в ручку все обязательные поля» и '
                  '«если одного из полей нет, запрос возвращает ошибку»')
    @allure.link(f'{Helpers.BASE_URL}/docs/#api-Courier-CreateCourier',
                 name='Ссылка на документацию эндпоинта Создание курьера')
    @pytest.mark.parametrize('first_field', [f'"firstName": {Helpers.first_name}', f'"password": {Helpers.password}'])
    @pytest.mark.parametrize('second_field', [f'"login": {Helpers.login}', f'"password": {Helpers.password}'])
    def test_courier_without_required_fields_return_400(self, first_field, second_field):

        payload = {
            first_field,
            second_field
        }

        response = requests.post(TestCreateCourierEndpoint.create_endpoint_url, data=payload)
        error_text = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'

        assert response.status_code == 400 and response.text == error_text, \
            f'response status code is {response.status_code}, response text is {response.text}'
