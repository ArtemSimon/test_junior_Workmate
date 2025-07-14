import pytest

@pytest.fixture
def number_data():
    return [
        {"price": 100, "rating": 4.5},
        {"price": 200, "rating": 4.8},
        {"price": 50, "rating": 3.9}
    ]

@pytest.fixture
def mixed_data():
    return [
        {"price": "100", "rating": "4.5"},  # строки с числами
        {"price": 200, "rating": 4.8},      # числа
        {"price": "invalid", "rating": "high"}  # невалидные
    ]