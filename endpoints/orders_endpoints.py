import allure
import requests

from data import BaseData


orders_url = f'{BaseData.BASE_URL}/api/orders'


class CreateOrder:

    @allure.step('Создание заказа')
    def create_order(self, ingredients, token):
        payloads = {"ingredients": [ingredients]}
        response = requests.post(orders_url, data=payloads,
                                 headers={"Authorization": token},
                                 timeout=10)
        return response


class GetOrders:

    @allure.step('Получение заказов конкретного пользователя')
    def get_orders(self, token):
        response = requests.get(orders_url,
                                headers={"Authorization": token},
                                timeout=10)
        return response
