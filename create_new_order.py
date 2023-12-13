import configuration
import requests
import data


# Шмуляев Виталий 11-когорта  — Финальный проект. Инженер по тестированию плюс

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)


track = str(post_new_order(data.order_body).json()['track'])


def get_order_by_track(track_id):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_BY_TRACK + track_id)


def test_status_code():
    response = get_order_by_track(track)
    assert response.status_code == 200
