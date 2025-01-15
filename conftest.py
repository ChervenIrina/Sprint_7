import pytest

from src.data.courier import register_new_courier_and_return_login_password, login_courier, delete_courier


@pytest.fixture
def courier():
    response, login_pass = register_new_courier_and_return_login_password()
    courier_id = login_courier(login_pass[0], login_pass[1]).json()["id"]
    yield response, login_pass
    delete_courier(courier_id)

