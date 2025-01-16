import allure
import pytest
from src.data.order import create_order, order_list


class TestCreate_Order:

    @allure.title('Проверка успешного создания заказа')
    @pytest.mark.parametrize('color', ['["BLACK"]', '["GREY"]', '["BLACK", "GREY"]', '[]'])
    def test_create_order(self, color):
        response_create = create_order()
        assert response_create.status_code == 201 and "track" in response_create.text

    @allure.title('Проверка выгрузки заказов (метро Сокольники)')
    # если сделать обычный гет, то всегда падает 504 ошибка
    # поэтому запрашиваю список через query-параметр (Станция: Сокольники)
    def test_order_list(self):
        response_order = order_list()

        assert response_order.status_code == 200 and len(response_order.json()["orders"]) > 0
