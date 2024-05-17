import allure
import pytest

from data import DataUser, DataResponseText
from endpoints.authorization_endpoints import CreateNewUser


class TestCreateNewUser:

    @allure.title('Создание нового пользователя')
    @allure.description('Создание нового уникального пользователя')
    def test_create_new_user(self):
        response = CreateNewUser().create_new_user(email=DataUser.EMAIL, password=DataUser.PASSWORD, name=DataUser.NAME)
        assert response.status_code == 200, \
            f'Код ответа {response.status_code} и тело ответа {response.text}'

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_new_user_already_registered(self):
        email = DataUser.EMAIL
        CreateNewUser().create_new_user(email=email, password=DataUser.PASSWORD, name=DataUser.NAME)
        response = CreateNewUser().create_new_user(email=email, password=DataUser.PASSWORD, name=DataUser.NAME)
        assert response.status_code == 403 and response.json() == DataResponseText.USER_ALREADY_EXISTS, \
            f'Код ответа {response.status_code} и тело ответа {response.text}'

    @allure.title('Создание пользователя без заполнения обязательного поля')
    @allure.description('Создание пользователя и не заполнить одно из обязательных полей')
    @pytest.mark.parametrize(
        'name, email, password',
        [(DataUser.NAME, None, None),
         (None, DataUser.EMAIL, None),
         (None, None, DataUser.PASSWORD),
         ])
    def test_create_new_user_without_field(self, name, email, password):
        response = CreateNewUser().create_new_user(email=email, password=password, name=name)
        assert response.status_code == 403 and response.json() == DataResponseText.REQUIRED_FIELDS, \
            f'Код ответа {response.status_code} и тело ответа {response.text}'
