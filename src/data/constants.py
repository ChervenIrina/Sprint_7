class Url:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"
    COURIER_URL = BASE_URL + "/api/v1/courier"
    LOGIN_COURIER_URL = BASE_URL + "/api/v1/courier/login"
    ORDER_URL = BASE_URL + "/api/v1/orders"
    STATION_URL = BASE_URL + '/api/v1/orders?nearestStation=["4"]'



class Message:
    MESSAGE_CREATE_TWO_COURIER = "Этот логин уже используется. Попробуйте другой."
    MESSAGE_SUCCESS_RESPONSE = '{"ok":true}'
    MESSAGE_WITHOUT_REQUIRED_FIELDS_CREATION_COURIER = "Недостаточно данных для создания учетной записи"
    MESSAGE_WITHOUT_REQUIRED_FIELDS_LOGIN_COURIER = "Недостаточно данных для входа"
    MESSAGE_COURIER_DOES_NOT_EXIST = "Учетная запись не найдена"

class dataTest:
    DATA_ORDER = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-06-06",
        "comment": "Saske, come back to Konoha",
        "color": []
    }
