import pytest
import requests
import data_for_tests as dft


@pytest.fixture(scope='function')
def payload_for_test_courier_create():
    data_courier = dft.register_new_courier_and_return_login_password()
    payload_for_test = {
        "login": data_courier[0] + '1',
        "password": data_courier[1] + '1',
        "firstName": data_courier[2] + '1'
    }
    payload_for_delete_one = {
        "login": data_courier[0] + '1',
        "password": data_courier[1] + '1'
    }
    payload_for_delete_two = {
        "login": data_courier[0],
        "password": data_courier[1]
    }
    yield payload_for_test
    id_courier = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                               data=payload_for_delete_one).json()['id']
    requests.delete('https://qa-scooter.praktikum-services.ru/api/v1/courier/'+str(id_courier))
    id_courier = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                               data=payload_for_delete_two).json()['id']
    requests.delete('https://qa-scooter.praktikum-services.ru/api/v1/courier/'+str(id_courier))


@pytest.fixture(scope='function')
def payload_for_test_courier_create_without_login():
    data_courier = dft.register_new_courier_and_return_login_password()
    payload_for_test = {
        "login": '',
        "password": data_courier[1],
        "firstName": data_courier[2]
    }
    payload_for_delete = {
        "login": data_courier[0],
        "password": data_courier[1]
    }
    yield payload_for_test
    id_courier = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                               data=payload_for_delete).json()['id']
    requests.delete('https://qa-scooter.praktikum-services.ru/api/v1/courier/'+str(id_courier))


@pytest.fixture(scope='function')
def payload_for_other_tests():
    data_courier = dft.register_new_courier_and_return_login_password()
    payload = {
        "login": data_courier[0],
        "password": data_courier[1],
        "firstName": data_courier[2]
    }
    yield payload
    payload_for_delete_courier = {
        "login": data_courier[0],
        "password": data_courier[1]
    }
    id_courier = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                               data=payload_for_delete_courier).json()['id']
    requests.delete('https://qa-scooter.praktikum-services.ru/api/v1/courier/'+str(id_courier))
