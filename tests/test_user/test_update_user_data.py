import allure
import pytest

from data import DataResponseText, DataUser
from endpoints.authorization_endpoints import UpdateUser
from conftest import authorization_user


class TestUpdateUserData:

    @allure.title('Изменение данных авторизованного пользователя')
    @allure.description('Изменение данных пользователя с передачей токена в хедере')
    @pytest.mark.parametrize(
        'name, email, password',
        [(DataUser.NAME, None, None),
         (None, DataUser.EMAIL, None),
         (None, None, DataUser.PASSWORD),
         ])
    def test_update_user_data(self, authorization_user, name, email, password):
        token = authorization_user

        response = UpdateUser().update_user(token=token, name=name, email=email, password=password)

        assert response.status_code == 200, f"Код ответа {response.status_code} и текст ответа {response.text}"

    @allure.title('Изменение данных пользователя без токена')
    @allure.description('Изменение данных пользователя без передачи токена в хедере')
    @pytest.mark.parametrize(
        'name, email, password',
        [(DataUser.NAME, None, None),
         (None, DataUser.EMAIL, None),
         (None, None, DataUser.PASSWORD),
         ])
    def test_update_user_data_without_token(self, name, email, password):

        response = UpdateUser().update_user(token=None,name=name, email=email, password=password)

        assert response.status_code == 401 and response.json() == DataResponseText.UNAUTHORIZED, \
            f"Код ответа {response.status_code} и текст ответа: {response.text}"
