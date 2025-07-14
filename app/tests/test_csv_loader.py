import pytest
from app.csv_loader import CSVLoader
from unittest.mock import mock_open,patch

@pytest.fixture
def sample_csv_data():
    return "name,price\napple,100\norange,50"

@pytest.fixture
def csv_loader():
    return CSVLoader()


def test_csv_loader(sample_csv_data):
    with patch('builtins.open', mock_open(read_data=sample_csv_data)):
        loader = CSVLoader()
        result = loader.load_file('products.csv')
        assert len(result) == 2
        assert result[0]['name'] == 'apple'    


def test_load_file_none_file(csv_loader):
    with pytest.raises(ValueError):
        csv_loader.load_file("none.csv")


def test_parse_row_numbers(csv_loader):
    row = {"price": "100", "rating": "4.5"}
    result = csv_loader._parse_row(row)
    assert result["price"] == 100
    assert result["rating"] == 4.5

def test_parse_row_mixed(csv_loader):
    row = {"id": "1", "price": "999.99", "available": "True"}
    result = csv_loader._parse_row(row)
    assert result["id"] == 1
    assert result["price"] == 999.99
    assert result["available"] == "True"