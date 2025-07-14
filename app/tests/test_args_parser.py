import pytest
from unittest.mock import patch, MagicMock
from app.args_parser import ArgsParser

@pytest.fixture
def basic_parser():
    return ArgsParser()

@pytest.fixture
def parser_with_columns():
    return ArgsParser(csv_column=["price", "name", "rating"])

@pytest.fixture
def temp_csv(tmp_path):
    csv_file = tmp_path / "test.csv"
    csv_file.write_text("name,price\ntest,100")
    return str(csv_file)

def test_parse_condition(basic_parser):
    assert basic_parser._parse_condition("price>100") == ("price", ">", "100")
    assert basic_parser._parse_condition("name=iPhone") == ("name", "=", "iPhone")
    assert basic_parser._parse_condition("rating<4.5") == ("rating", "<", "4.5")

def test_parse_condition_invalid(basic_parser):
    with pytest.raises(ValueError):
        basic_parser._parse_condition("price!100")

def test_parse_aggregate(basic_parser):
    assert basic_parser._parse_aggregate("price=avg") == ("price", "avg")
    assert basic_parser._parse_aggregate("rating=min") == ("rating", "min")
    assert basic_parser._parse_aggregate("price=max") == ("price", "max")

def test_parse_aggregate_invalid(basic_parser):
    with pytest.raises(ValueError):
        basic_parser._parse_aggregate("price:avg")
    with pytest.raises(ValueError):
        basic_parser._parse_aggregate("price=sum")

def test_validate_args_file_exists(basic_parser, temp_csv):
    args = MagicMock(file=temp_csv, where=None, aggregate=None)
    basic_parser._validate_args(args)  # Не должно вызывать исключений

def test_validate_args_file_not_exists(basic_parser):
    args = MagicMock(file="nonexistent.csv", where=None, aggregate=None)
    with pytest.raises(FileExistsError):
        basic_parser._validate_args(args)


def test_validate_args_column_validation(parser_with_columns):
    valid_args = MagicMock(file="products.csv", where="price>100", aggregate="name=avg")
    parser_with_columns._validate_args(valid_args)  # Не должно вызывать исключений

    invalid_args = MagicMock(file="products.csv", where="invalid>100", aggregate=None)
    with pytest.raises(ValueError):
        parser_with_columns._validate_args(invalid_args)

def test_full_parse_with_mocks(basic_parser):
    with patch('argparse.ArgumentParser.parse_args') as mock_parse:
        test_args = MagicMock(file="products.csv", where="price>100", aggregate="rating=avg")
        mock_parse.return_value = test_args
        
        result = basic_parser.parse()
        assert result == test_args
        mock_parse.assert_called_once()

