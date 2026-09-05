import requests


PRODUCT_SERVICE_URL = "http://127.0.0.1:8002"


def test_product_service_communication():

    response = requests.get(
        f"{PRODUCT_SERVICE_URL}/products"
    )

    assert response.status_code == 200

    products = response.json()

    assert isinstance(products, list)