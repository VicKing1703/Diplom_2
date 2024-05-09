import pytest
import random


from data import DataUser
from endpoints.authorization_endpoints import CreateNewUser, LoginUser, DeleteUser
from endpoints.ingredients_endpoints import GetIngredients


# фикстура сделана с отдачей токена через авторизацию (user flow), т.к. это логичнее чем токен тольеко через регистрацию
@pytest.fixture
def authorization_user():
    CreateNewUser().create_new_user(email=DataUser.EMAIL, password=DataUser.PASSWORD, name=DataUser.NAME)
    response = LoginUser().login_user(email=DataUser.EMAIL, password=DataUser.PASSWORD)
    yield response.json()['accessToken']
    DeleteUser().delete_user(token=response.json()['accessToken'])


@pytest.fixture
def get_random_hash_ingredients():
    response = GetIngredients().get_ingredients()
    ingredient_list = response['data']
    random_ingredients = random.sample(ingredient_list, 3)  # выбираем 3 случайных ингредиента
    random_ingredients_hash = [ingredient['_id'] for ingredient in random_ingredients]  # создаем список ингредиентов
    return random_ingredients_hash
