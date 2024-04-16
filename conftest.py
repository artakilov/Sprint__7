import pytest
import requests
import helpers as hlprs


@pytest.fixture(scope='function')
def payload_for_test_courier_create():
    data_courier = hlprs.register_new_courier_and_return_login_password()
    payload_for_test = {
        "login": data_courier[0] + '1',
        "password": data_courier[1] + '1',
        "firstName": data_courier[2] + '1'
    }
    payload_for_delete_one = {
        "login": data_courier[0],
        "password": data_courier[1]
    }
    payload_for_delete_two = {
        "login": data_courier[0] + '1',
        "password": data_courier[1] + '1'
    }
    yield payload_for_test
    hlprs.delete_courier(payload_for_delete_one)
    hlprs.delete_courier(payload_for_delete_two)


@pytest.fixture(scope='function')
def payload_for_other_tests():
    data_courier = hlprs.register_new_courier_and_return_login_password()
    payload = {
        "login": data_courier[0],
        "password": data_courier[1],
        "firstName": data_courier[2]
    }
    payload_without_login = {
        "login": '',
        "password": data_courier[1],
        "firstName": data_courier[2]
    }
    payload_for_delete = {
        "login": data_courier[0],
        "password": data_courier[1]
    }
    yield payload, payload_without_login
    hlprs.delete_courier(payload_for_delete)
