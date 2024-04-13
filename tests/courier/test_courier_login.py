import allure
import pytest
import requests


class TestCourierLogin:

    # тест 004 - позитивный, проверка авторизации курьера (курьер может авторизоваться, нужно передать все обязательные
    # поля, успешный запрос возвращает id)
    @allure.title('Проверка ручки авторизации курьера - позитивная')
    @allure.description('Проверяем, что курьер может авторизоваться, когда передаются все обязательные поля, '
                        'возвращаются правивльные код и текст (id) ответа')
    def test_courier_login(self, payload_for_other_tests):
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                                 data=payload_for_other_tests)

        assert (200 == response.status_code and
                'id' in response.text), \
            f'Код ответа - "{response.status_code}", текст ответа - "{response.text}"'

    # тесты 005-006 - негативный, проверка возвращения ошибки, если какого-то поля нет (1 - логин, 2 - пароль)
    @allure.title('Проверка ручки авторизации курьера - негативная, авторизация курьера с пустым полем')
    @allure.description('Проверяем, что при авторизации курьера с пустым полем {n} возвращается ошибка, '
                        'возвращаются правильные код и текст ответа')
    @pytest.mark.parametrize('n', ['login', 'password'])
    def test_courier_login_without_data(self, payload_for_other_tests, n):
        data_m = payload_for_other_tests[n]
        payload_for_other_tests[n] = ''
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                                 data=payload_for_other_tests)
        payload_for_other_tests[n] = data_m

        assert (400 == response.status_code and
                'Недостаточно данных для входа' == response.json()["message"]), \
            f'Код ответа - "{response.status_code}", текст ответа - "{response.json()["message"]}"'

    # тест 007-008 - негативный, проверка возвращения ошибки, если неправельно указаны данные для какого-нибудь поля
    # (1 - логин, 2 - пароль)
    @allure.title('Проверка ручки авторизации курьера - негативная, авторизация курьера с неправильными данными')
    @allure.description('Проверяем, что при авторизации курьера с неправильными данными в поле {n} возвращается ошибка,'
                        ' возвращаются правильные код и текст ответа')
    @pytest.mark.parametrize('n', ['login', 'password'])
    def test_courier_login_with_incorrect_data(self, payload_for_other_tests, n):
        data_m = payload_for_other_tests[n]
        payload_for_other_tests[n] += '1'
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                                 data=payload_for_other_tests)
        payload_for_other_tests[n] = data_m

        assert (404 == response.status_code and
                'Учетная запись не найдена' == response.json()["message"]), \
            f'Код ответа - "{response.status_code}", текст ответа - "{response.json()["message"]}"'
