import allure
import requests
import random
import string
from src.data.constants import Url

@allure.step('Создаем курьера (рандомные данные)')
# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(Url.COURIER_URL, data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return response, login_pass

@allure.step('Создаем курьера (переданные данные)')
def create_courier(login, password, first_name):
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post(Url.COURIER_URL, data=payload)
    return response

@allure.step('Удалем курьера')
def delete_courier(id_courier):
    response = requests.delete(f"{Url.COURIER_URL}{id_courier}")
    return response

@allure.step('Авторизация курьера')
def login_courier(login, password):
    data = {
        "login": login,
        "password": password
    }
    response = requests.post(Url.LOGIN_COURIER_URL, json=data)
    return response
