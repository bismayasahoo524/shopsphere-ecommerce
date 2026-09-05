from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_service_is_running():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Product Service is running"}


def test_create_product():
    product_data = {
        "name": "Test Laptop",
        "description": "Laptop created by PyTest",
        "price": 75000.0,
        "quantity": 10,
        "category": "Electronics",
        "image_url": "https://example.com/laptop.jpg"
    }

    response = client.post("/products/", json=product_data)

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == product_data["name"]
    assert data["price"] == product_data["price"]
    assert data["quantity"] == product_data["quantity"]


def test_get_all_products():
    response = client.get("/products/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)