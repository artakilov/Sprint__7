import allure
import requests
import data_for_tests as dft


class TestGetListOfOrders:

    # тест 013 - позитивный, проверка возвращения в теле ответа списка заказов
    @allure.title('Проверка ручки получения списка заказов - позитивная')
    @allure.description('Проверяем, что в теле ответа возвращается список заказов, возвращается правивльные код и '
                        'текст ответа')
    def test_get_list_of_orders(self):
        response = requests.get(dft.URL_SCOOTER + dft.api_get_list_of_orders)

        assert 200 == response.status_code and dft.answr_get_list_of_orders_ok in response.text, \
            f'Код ответа - "{response.status_code}", текст ответа - "{response.text}"'
