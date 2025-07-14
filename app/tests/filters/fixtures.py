import pytest

@pytest.fixture
def number_data():
    return [
        {"id": 1, "price": 100, "rating": 4.5},
        {"id": 2, "price": 200, "rating": 4.8},
        {"id": 3, "price": 50, "rating": 3.9}
    ]

@pytest.fixture
def string_data():
    return [
        {"id": 1, "name": "iPhone", "status": "new"},
        {"id": 2, "name": "Galaxy", "status": "used"},
        {"id": 3, "name": "Pixel", "status": "new"}
    ]

@pytest.fixture
def mixed_data():
    return [
        {"id": 1, "price": "100", "name": "iPhone"},
        {"id": 2, "price": 200, "name": "Galaxy"},
        {"id": 3, "price": "invalid", "name": "Pixel"}
    ]