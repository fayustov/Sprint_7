import allure
import requests

from urls import Urls
from helpers import Helpers


class TestOrdersEndpoint:

    @allure.title('Проверка требования: «в тело ответа возвращается список заказов»')
    @allure.link(f'{Urls.BASE_URL}/docs/#api-Orders-GetOrdersPageByPage',
                 name='Ссылка на документацию эндпоинта Получение списка заказов')
    def test_getting_orders_list_return_orders(self):

        response = requests.get(Urls.orders_endpoint_url)

        assert response.status_code == 200 and 'orders' in response.json()
