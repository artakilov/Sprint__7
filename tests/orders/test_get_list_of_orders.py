import allure
import requests


class TestGetListOfOrders:

    # тест 013 - позитивный, проверка возвращения в теле ответа списка заказов
    @allure.title('Проверка ручки получения списка заказов - позитивная')
    @allure.description('Проверяем, что в теле ответа возвращается список заказов, возвращается правивльные код и '
                        'текст ответа')
    def test_get_list_of_orders(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')

        print(response.text)
        assert 200 == response.status_code and 'orders' in response.text, \
            f'Код ответа - "{response.status_code}", текст ответа - "{response.text}"'
