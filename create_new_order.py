import configuration
import requests
import data

# Шмуляев Виталий 11-когорта  — Финальный проект. Инженер по тестированию плюс

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)


response = post_new_order(data.user_body);
print(response.status_code)
print(response.json())

track = response.json()['track']
query_track = {
    "t": track
}


def get_order_by_track():
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_BY_TRACK, params=query_track)


response = get_order_by_track();
print(response.status_code)
print(response.json())


def test_status_code():
    assert response.status_code == 200
