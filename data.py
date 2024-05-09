from mimesis import Field


class BaseData:

    BASE_URL = "https://stellarburgers.nomoreparties.site"


class DataUser:

    f = Field()

    EMAIL = f("email")
    PASSWORD = f("password")
    NAME = f("name")


class DataResponseText:

    UNAUTHORIZED = {"success": False, "message": "You should be authorised"}
    USER_ALREADY_EXISTS = {"success": False, "message": "User already exists"}
    REQUIRED_FIELDS = {"success": False, "message": "Email, password and name are required fields"}
    INCORRECT_LOGIN = {"success": False, "message": "email or password are incorrect"}
