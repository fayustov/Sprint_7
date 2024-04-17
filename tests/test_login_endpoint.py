import allure
import pytest
import requests

from urls import Urls
from helpers import Helpers


class TestLoginEndpoint:

    @allure.title('Проверка требований: «курьер может авторизоваться» и «успешный запрос возвращает id»')
    @allure.link(f'{Urls.BASE_URL}/docs/#api-Courier-Login',
                 name='Ссылка на документацию эндпоинта Логин курьера в системе')
    def test_courier_login_positive_return_200(self):

        response = requests.post(Urls.login_endpoint_url, data=Helpers.correct_test_user_payload)

        assert response.status_code == 200 and 'id' in response.text, \
            f'response status code is {response.status_code}, response text is {response.text}'

    @allure.title(
        'Проверка требований: «если авторизоваться под несуществующим пользователем, запрос возвращает ошибку» '
        'и «система вернёт ошибку, если неправильно указать логин или пароль»')
    @allure.link(f'{Urls.BASE_URL}/docs/#api-Courier-Login',
                 name='Ссылка на документацию эндпоинта Логин курьера в системе')
    def test_courier_login_with_incorrect_data_return_404(self):

        response = requests.post(Urls.login_endpoint_url, data=Helpers.incorrect_test_user_payload)

        assert response.status_code == 404 and response.text == '{"code":404,"message":"Учетная запись не найдена"}', \
            f'status code is {response.status_code}, response text is {response.text}'

    @allure.title(
        'Проверка требований: «для авторизации нужно передать все обязательные поля» '
        'и «система вернёт ошибку, если неправильно указать логин или пароль»')
    @allure.description(
        'Согласно документации, ожидается что тест должен вернуть 400-й код ответа и соответствующее сообщение о'
        ' недостаточном наборе данных, однако метод багованный, поэтому используется метка xfail и ограничение по '
        'таймауту подключения в 1 секунду')
    @allure.link(f'{Urls.BASE_URL}/docs/#api-Courier-Login',
                 name='Ссылка на документацию эндпоинта Логин курьера в системе')
    @pytest.mark.parametrize('field', [f'"login": {Helpers.login}', f'"password": {Helpers.password}'])
    @pytest.mark.xfail(reason='Too long timeout and 504 response', strict=True)
    def test_login_without_required_fild(self, field):

        payload = {
            field
        }
        response = requests.post(Urls.login_endpoint_url, data=payload, timeout=1)

        assert response.status_code == 400 and response.text == '{"message":"Недостаточно данных для входа"}'
