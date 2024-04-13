import json

import allure
import pytest
import requests


class TestOrderCreate:

    # тест 009-012 - позитивный, проверка создания заказа с разными цветами самоката
    # (1 - черный, 2 - серый, 3 - серый или черный, 4 - без указания цвета)
    color = [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ]

    @allure.title('Проверка ручки создания заказа - позитивная')
    @allure.description('Проверяем, что заказ можно создать с разными цветами самоката, возвращаются правивльные код и '
                        'текст ответа')
    @pytest.mark.parametrize('color', color)
    def test_order_create(self, color):
        payload = {
            "firstName": "Михаил",
            "lastName": "Федотов",
            "address": "Заозерная,15/8-43",
            "metroStation": 13,
            "phone": "+79988776655",
            "rentTime": 3,
            "deliveryDate": "2024-04-20",
            "comment": "Хочу кататься!",
            "color": color
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=json.dumps(payload))
        requests.put('https://qa-scooter.praktikum-services.ru/api/v1/orders/cancel',
                     data={"track": response.json()["track"]})

        assert 201 == response.status_code and 'track' in response.text, \
            f'Код ответа - "{response.status_code}", текст ответа - "{response.text}"'
