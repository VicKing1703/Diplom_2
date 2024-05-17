import allure
import requests

from data import BaseData


auth_base_url = f'{BaseData.BASE_URL}/api/auth'

registration_url = f'{auth_base_url}/register'
login_url = f'{auth_base_url}/login'
update_user_url = f'{auth_base_url}/user'


class CreateNewUser:

    @allure.step('Создание нового пользователя')
    def create_new_user(self, **kwargs):
        payload = {}
        params = ["email", "password", "name"]

        for param in params:
            if param in kwargs:
                payload[param] = kwargs[param]

        response = requests.post(registration_url, data=payload, timeout=10)
        return response


class LoginUser:

    @allure.step('Логин пользователя')
    def login_user(self, **kwargs):
        payload = {}
        params = ["email", "password"]

        for param in params:
            if param in kwargs:
                payload[param] = kwargs[param]

        response = requests.post(login_url, data=payload, timeout=10)
        return response


class UpdateUser:

    # Тут не уверен что туда добавлен токен, но по описанию он передаётся в теле запроса а не в хедере.
    # Плюсом не совсем понял как должно выглядеть тело запроса. Так много вопросов и так мало ответов
    @allure.step('Изменение данных пользователя')
    def update_user(self, token, **kwargs):
        payload = {}
        params = ["email", "password", "name"]

        for param in params:
            if param in kwargs:
                payload[param] = kwargs[param]

        response = requests.patch(update_user_url,
                                data=payload,
                                headers={"Authorization": token},
                                timeout=10)
        return response


class DeleteUser:

    @allure.step('Удаление пользователя')
    def delete_user(self, token=None):
        response = requests.delete(update_user_url, headers={"Authorization": token}, timeout=10)
        return response
