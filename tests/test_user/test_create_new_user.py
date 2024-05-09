import allure

from data import DataUser, DataResponseText
from endpoints.authorization_endpoints import CreateNewUser


class TestCreateNewUser:

    @allure.title('Создание уникального пользователя')
    @allure.description('Создание нового уникального пользователя')
    def test_create_new_user(self):
        response = CreateNewUser().create_new_user(email=DataUser.EMAIL, password=DataUser.PASSWORD, name=DataUser.NAME)
        assert response.status_code == 200, \
            f'Код ответа {response.status_code} и тело ответа {response.text}'

    @allure.title('Создание пользователя, который уже зарегистрирован')
    @allure.description('Создание пользователя, который уже зарегистрирован')
    def test_create_new_user_already_registered(self):
        email = DataUser.EMAIL
        CreateNewUser().create_new_user(email=email, password=DataUser.PASSWORD, name=DataUser.NAME)
        response = CreateNewUser().create_new_user(email=email, password=DataUser.PASSWORD, name=DataUser.NAME)
        assert response.status_code == 403 and response.json() == DataResponseText.USER_ALREADY_EXISTS, \
            f'Код ответа {response.status_code} и тело ответа {response.text}'

    @allure.title('Создание пользователя и не заполнить одно из обязательных полей')
    @allure.description('Создание пользователя и не заполнить одно из обязательных полей')
    def test_create_new_user_without_field(self):
        response = CreateNewUser().create_new_user(email=DataUser.EMAIL, password=DataUser.PASSWORD, name="")
        assert response.status_code == 403 and response.json() == DataResponseText.REQUIRED_FIELDS, \
            f'Код ответа {response.status_code} и тело ответа {response.text}'
