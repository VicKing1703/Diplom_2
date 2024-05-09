import allure
import requests

from data import BaseData


ingredients_url = f'{BaseData.BASE_URL}/api/ingredients'


class GetIngredients:

    @allure.step('Получение списка ингредиентов')
    def get_ingredients(self):
        response = requests.get(ingredients_url, timeout=10)
        return response.json()
