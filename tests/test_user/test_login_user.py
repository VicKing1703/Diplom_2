import allure

from data import DataUser, DataResponseText
from endpoints.authorization_endpoints import LoginUser, CreateNewUser


class TestLoginUser:

    @allure.title('Логин пользователя')
    @allure.description('Логин под существующим пользователем')
    def test_login_user(self, create_new_user):
        email, password = create_new_user
        response = LoginUser().login_user(email=email, password=password)
        assert response.status_code == 200, \
            f'Код ответа {response.status_code} и тело ответа {response.text}'

    @allure.title('Логин пользователя с неверным логином и паролем')
    @allure.description('Логин с неверным логином и паролем')
    def test_login_user_wrong_email_and_password(self):
        email = "wrong_email"
        password = "wrong_password"
        response = LoginUser().login_user(email=email, password=password)
        assert response.status_code == 401 and response.json() == DataResponseText.INCORRECT_LOGIN, \
            f'Код ответа {response.status_code} и тело ответа {response.text}'
