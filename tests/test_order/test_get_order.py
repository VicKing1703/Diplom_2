import allure

from endpoints.orders_endpoints import GetOrders
from conftest import authorization_user
from data import DataResponseText


class TestGetOrder:

    @allure.title('Получение заказа конкретного пользователя с авторизацией')
    @allure.description('Получение заказа конкретного пользователя с авторизацией')
    def test_get_order_specific_user_with_token(self, authorization_user):
        token = authorization_user
        response = GetOrders().get_orders(token=token)
        assert response.status_code == 200, f"Код ответа: {response.status_code}, тело ответа: {response.text}"

    @allure.title('Получение заказа конкретного пользователя без авторизации')
    @allure.description('Получение заказа конкретного пользователя без авторизации')
    def test_get_order_specific_user_without_token(self):
        token = ''
        response = GetOrders().get_orders(token=token)
        assert response.status_code == 401 and response.json() == DataResponseText.UNAUTHORIZED, \
            f"Код ответа: {response.status_code}, тело ответа: {response.text}"
