import allure
import requests
from src.data.constants import Url, dataTest

@allure.step('Создаем заказ')
def create_order():
    return requests.post(Url.ORDER_URL, json=dataTest.DATA_ORDER)

@allure.step('Выгружаем заказы')
def order_list():
    return requests.get(Url.STATION_URL)

