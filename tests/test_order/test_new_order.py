import allure

from endpoints.orders_endpoints import CreateOrder
from conftest import authorization_user, get_random_hash_ingredients


class TestNewOrder:

    @allure.title('Создание заказа с авторизацией и ингредиентами')
    @allure.description('Создание нового заказа с авторизацией и передачей верного хэша ингредиентов')
    def test_new_order_with_auth_and_ingredients(self, authorization_user, get_random_hash_ingredients):

        token = authorization_user
        ingredients_hash = get_random_hash_ingredients

        response = CreateOrder().create_order(ingredients=ingredients_hash, token=token)
        assert response.status_code == 200 and "true" in response.text, \
            f"Код ответа: {response.status_code}, тело ответа: {response.text}"

    @allure.title('Создание заказа с авторизацией и без ингредиентов')
    @allure.description('Создание нового заказа с авторизацией и без передачи хэша ингредиентов')
    def test_new_order_with_auth_and_no_ingredients(self, authorization_user):

        token = authorization_user
        ingredients_hash = []
        response = CreateOrder().create_order(ingredients=ingredients_hash, token=token)
        assert response.status_code == 400 and "Ingredient ids must be provided" in response.text, \
            f"Код ответа: {response.status_code}, тело ответа: {response.text}"

    # Тут вопрос к описанию API - указано что переадресовывается на логин, что намекает, вероятно,
    # на код 301 и перенаправление на логин
    # (страница 5 в документации к API "Только авторизованные пользователи могут делать заказы"))
    @allure.title('Создание заказа без авторизации и ингредиентами')
    @allure.description('Создание нового заказа без авторизации и передачей верного хэша ингредиентов')
    def test_new_order_without_auth(self, get_random_hash_ingredients):

        ingredients_hash = get_random_hash_ingredients
        response = CreateOrder().create_order(ingredients=ingredients_hash, token='')
        assert response.status_code == 301, \
            f"Код ответа: {response.status_code}, тело ответа: {response.text}"

    @allure.title('Создание заказа с неправильным хэшом ингредиентов')
    @allure.description('Создание нового заказа авторизованного пользователя с неправильным хэшом ингредиентов')
    def test_new_order_wit_wrong_hash_ingredients(self, authorization_user):

        token = authorization_user
        ingredients_hash = [1, 2, 3]
        response = CreateOrder().create_order(ingredients=ingredients_hash, token=token)
        assert response.status_code == 500, \
            f"Код ответа: {response.status_code}, тело ответа: {response.text}"
