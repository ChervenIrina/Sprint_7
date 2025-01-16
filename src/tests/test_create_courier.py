import allure
import pytest

from conftest import courier
from src.data.courier import create_courier
from src.data.constants import Message


class TestCreateCourier:

    @allure.title('Проверка успешного создания курьера')
    def test_create_courier_success(self, courier):
        response_create, login_pass = courier
        assert response_create.status_code == 201 and response_create.text == Message.MESSAGE_SUCCESS_RESPONSE

    @allure.title('Проверка ошибки при создании дубль курьера')
    def test_create_double_courier(self, courier):
        response_create, login_pass = courier
        response_create_two = create_courier(login_pass[0], login_pass[1], login_pass[2])

        assert response_create_two.status_code == 409 and response_create_two.json()["message"] == Message.MESSAGE_CREATE_TWO_COURIER

    @allure.title('Проверка ошибки на заполненность обязательных полей')
    @pytest.mark.parametrize('login_pass', [['', '123', 'Irina'], ['gor', '', 'Irina']])
    def test_create_courier_without_required_fields(self, login_pass):
        response_create = create_courier(login_pass[0], login_pass[1], login_pass[2])

        assert response_create.status_code == 400 and response_create.json()["message"] == Message.MESSAGE_WITHOUT_REQUIRED_FIELDS_CREATION_COURIER
