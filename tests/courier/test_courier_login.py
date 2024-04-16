import allure
import pytest
import requests
import data_for_tests as dft


class TestCourierLogin:

    # тест 004 - позитивный, проверка авторизации курьера (курьер может авторизоваться, нужно передать все обязательные
    # поля, успешный запрос возвращает id)
    @allure.title('Проверка ручки авторизации курьера - позитивная')
    @allure.description('Проверяем, что курьер может авторизоваться, когда передаются все обязательные поля, '
                        'возвращаются правивльные код и текст (id) ответа')
    def test_courier_login(self, payload_for_other_tests):
        response = requests.post(dft.URL_SCOOTER + dft.api_login_courier, data=payload_for_other_tests[0])

        assert (200 == response.status_code and
                dft.answr_post_login_courier_ok in response.text), \
            f'Код ответа - "{response.status_code}", текст ответа - "{response.text}"'

    # тесты 005-006 - негативный, проверка возвращения ошибки, если какого-то поля нет (1 - логин, 2 - пароль)
    @allure.title('Проверка ручки авторизации курьера - негативная, авторизация курьера с пустым полем')
    @allure.description('Проверяем, что при авторизации курьера с пустым полем {n} возвращается ошибка, '
                        'возвращаются правильные код и текст ответа')
    @pytest.mark.parametrize('n', ['login', 'password'])
    def test_courier_login_without_data(self, payload_for_other_tests, n):
        data_m = payload_for_other_tests[0][n]
        payload_for_other_tests[0][n] = ''
        response = requests.post(dft.URL_SCOOTER + dft.api_login_courier, data=payload_for_other_tests[0])
        payload_for_other_tests[0][n] = data_m

        assert (400 == response.status_code and
                dft.answr_post_login_courier_without_data == response.json()["message"]), \
            f'Код ответа - "{response.status_code}", текст ответа - "{response.json()["message"]}"'

    # тест 007-008 - негативный, проверка возвращения ошибки, если неправельно указаны данные для какого-нибудь поля
    # (1 - логин, 2 - пароль)
    @allure.title('Проверка ручки авторизации курьера - негативная, авторизация курьера с неправильными данными')
    @allure.description('Проверяем, что при авторизации курьера с неправильными данными в поле {n} возвращается ошибка,'
                        ' возвращаются правильные код и текст ответа')
    @pytest.mark.parametrize('n', ['login', 'password'])
    def test_courier_login_with_incorrect_data(self, payload_for_other_tests, n):
        data_m = payload_for_other_tests[0][n]
        payload_for_other_tests[0][n] += '1'
        response = requests.post(dft.URL_SCOOTER + dft.api_login_courier, data=payload_for_other_tests[0])
        payload_for_other_tests[0][n] = data_m

        assert (404 == response.status_code and
                dft.answr_post_login_courier_with_incorrect_data == response.json()["message"]), \
            f'Код ответа - "{response.status_code}", текст ответа - "{response.json()["message"]}"'
