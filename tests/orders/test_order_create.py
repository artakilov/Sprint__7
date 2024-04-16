import json
import allure
import pytest
import requests
import data_for_tests as dft


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
        response = requests.post(dft.URL_SCOOTER + dft.api_create_order, data=json.dumps(payload))
        requests.put(dft.URL_SCOOTER + dft.api_cancel_order, data={"track": response.json()["track"]})

        assert 201 == response.status_code and dft.answr_post_create_order_ok in response.text, \
            f'Код ответа - "{response.status_code}", текст ответа - "{response.text}"'
