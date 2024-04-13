import allure
import requests


class TestCourierCreate:

    # тест 001 - позитивный, проверка создания курьера (курьера можно создать, нужно передать все обязательные поля,
    # возвращаются правильные код и текст ответа)
    @allure.title('Проверка ручки создания курьера - позитивная')
    @allure.description('Проверяем, что курьера можно создать, когда передаются все обязательные поля, возвращаются '
                        'правивльные код и текст ответа')
    def test_courier_create(self, payload_for_test_courier_create):
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier',
                                 data=payload_for_test_courier_create)

        assert (201 == response.status_code and
                '{"ok":true}' == response.text), \
            f'Код ответа - "{response.status_code}", текст ответа - "{response.text}"'

    # тест 002 - негативный, проверка создания курьера с существующим именем (нельзя создать двух одинаковых курьеров,
    # при этом возвращается ошибка)
    @allure.title('Проверка ручки создания курьера - негативная, создание курьера с существующим именем')
    @allure.description('Проверяем, что нельзя создать двух одинаковых курьеров, и что при этом возвращается ошибка, '
                        'возвращаются правильные код и текст ответа')
    def test_courier_create_same_data(self, payload_for_test_courier_create):
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier',
                      data=payload_for_test_courier_create)
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier',
                                 data=payload_for_test_courier_create)

        assert (409 == response.status_code and
                'Этот логин уже используется' == response.json()["message"]), \
            f'Код ответа - "{response.status_code}", текст ответа - "{response.json()["message"]}"'

    # тест 003 - негативный, проверка создания курьера без логина
    @allure.title('Проверка ручки создания курьера - негативная, создание курьера без логина')
    @allure.description('Проверяем, что нельзя создать курьера без логина, и что при этом возвращается ошибка, '
                        'возвращаются правильные код и текст ответа')
    def test_courier_create_without_login(self, payload_for_test_courier_create_without_login):
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier',
                                 data=payload_for_test_courier_create_without_login)

        assert (400 == response.status_code and
                'Недостаточно данных для создания учетной записи' == response.json()["message"]), \
            f'Код ответа - {response.status_code}, текст ответа - {response.json()["message"]}'
