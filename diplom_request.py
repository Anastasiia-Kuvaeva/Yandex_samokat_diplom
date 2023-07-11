import configuration
import requests
import data


# создание заказа
def post_create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)


# получение заказа по track
def get_get_order(track):
    payload = {'t': track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                        params=payload,
                        headers=data.headers)
