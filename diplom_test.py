# Анастасия Куваева, 6-я когорта — Финальный проект. Инженер по тестированию плюс
import diplom_request
import data

# создание заказа для получения track
response = diplom_request.post_create_order(data.create_order_body)
track = response.json()["track"]


# метод позитивной проверки создания и получения заказа
def test_positive_create_get_order_assert():
    response = diplom_request.get_get_order(track)
    assert response.status_code == 200
    assert response.json()["order"]["track"] == track
