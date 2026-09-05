import requests


PRODUCT_SERVICE_URL = "http://127.0.0.1:8002"


def get_product(product_id: int):

    try:

        response = requests.get(
            f"{PRODUCT_SERVICE_URL}/products/{product_id}"
        )

        if response.status_code == 200:
            return response.json()

        return None

    except requests.RequestException:
        return None