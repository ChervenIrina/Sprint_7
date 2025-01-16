import allure
import pytest

from conftest import courier
from src.data.courier import login_courier
from src.data.constants import Message


class TestLoginCourier:

    @allure.title('Проверка успешной авторизации курьера')
    def test_courier_login_success(self, courier):
        response_create, login_pass = courier
        response_login = login_courier(login_pass[0], login_pass[1])

        assert response_login.status_code == 200 and response_login.json()["id"] > 0

    @allure.title('Проверка ошибки авторизации при неверном пароле')
    def test_courier_login_invalid_password(self, courier):
        response_create, login_pass = courier
        response_login = login_courier(login_pass[0], "aaa")

        assert response_login.status_code == 404 and response_login.json()["message"] == Message.MESSAGE_COURIER_DOES_NOT_EXIST

    @allure.title('Проверка ошибки авторизации при незаполненных обязательных полей')
    @pytest.mark.parametrize('login_pass', [['', '123'], ['gor', '']])
    def test_login_courier_without_required_fields(self, login_pass):
        response_login = login_courier(login_pass[0], login_pass[1])

        assert response_login.status_code == 400 and response_login.json()["message"] == Message.MESSAGE_WITHOUT_REQUIRED_FIELDS_LOGIN_COURIER

    @allure.title('Проверка ошибки авторизации несуществующего курьера')
    def test_login_courier_does_not_exist(self, login="aaa", password="aaa"):
        response_login = login_courier(login, password)

        assert response_login.status_code == 404 and response_login.json()["message"] == Message.MESSAGE_COURIER_DOES_NOT_EXIST
