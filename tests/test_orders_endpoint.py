import allure
import requests

from helpers import Helpers


class TestOrdersEndpoint:

    orders_endpoint_url = f"{Helpers.BASE_URL}/api/v1/orders"

    @allure.title('Проверка требования: «в тело ответа возвращается список заказов»')
    @allure.link(f'{Helpers.BASE_URL}/docs/#api-Orders-GetOrdersPageByPage',
                 name='Ссылка на документацию эндпоинта Получение списка заказов')
    def test_getting_orders_list_return_orders(self):

        response = requests.get(TestOrdersEndpoint.orders_endpoint_url)

        assert 'orders' in response.json()
