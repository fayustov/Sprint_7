class Urls:

    BASE_URL = 'https://qa-scooter.praktikum-services.ru'  # Основной адрес тестируемого приложения
    create_endpoint_url = f"{BASE_URL}/api/v1/courier"  # Эндпоинт создания курьера
    login_endpoint_url = f"{BASE_URL}/api/v1/courier/login"  # Эндпоинт для логина в системе
    orders_endpoint_url = f"{BASE_URL}/api/v1/orders"  # Эндпоинт для работы с заказами
