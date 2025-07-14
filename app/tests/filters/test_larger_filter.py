import pytest
from app.filters.larger_than_filter import LargerThanFilter
from app.tests.filters.fixtures import number_data,string_data,mixed_data


def test_number_larger_filter(number_data):
    filter = LargerThanFilter()
    result = filter.apply(number_data, "price", 150)
    assert len(result) == 1
    assert result[0]["id"] == 2

def test_string_larger_filter(string_data):
    filter = LargerThanFilter()
    filter.apply(string_data, "name", "Galaxy")

def test_mixed_data_larger_filter(mixed_data):
    filter = LargerThanFilter()
    result = filter.apply(mixed_data[:2], "price", 150)  # только валидные
    assert len(result) == 1
    assert result[0]["id"] == 2

def test_missing_column(number_data):
    filter = LargerThanFilter()
    with pytest.raises(KeyError):
        filter.apply(number_data, "missing_column", 100)