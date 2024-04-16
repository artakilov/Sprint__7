# адреса серверов
URL_SCOOTER = 'https://qa-scooter.praktikum-services.ru'

# ручки API
# создание курьера
api_create_courier = '/api/v1/courier'
# авторизация курьера
api_login_courier = '/api/v1/courier/login'
# создание заказа
api_create_order = '/api/v1/orders'
# отмена заказа
api_cancel_order = '/api/v1/orders/cancel'
# получение списка заказов
api_get_list_of_orders = '/api/v1/orders'
# удаление курьера
api_delete_courier = '/api/v1/courier/'

# ответы на запросы
# ответ на post создание курьера
answr_post_create_courier_ok = '{"ok":true}'
# ответ на post создание курьера с существующим логином
answr_post_create_courier_same_data = 'Этот логин уже используется'
# ответ на post создание курьера без задания логина
answr_post_create_courier_without_login = 'Недостаточно данных для создания учетной записи'
# ответ на post авторизация курьера
answr_post_login_courier_ok = 'id'
# ответ на post авторизация курьера без логина
answr_post_login_courier_without_data = 'Недостаточно данных для входа'
# ответ на post авторизация курьера с несуществующим логином
answr_post_login_courier_with_incorrect_data = 'Учетная запись не найдена'
# ответ на post создание заказа
answr_post_create_order_ok = 'track'
# ответ на get получение списка заказов
answr_get_list_of_orders_ok = 'orders'
