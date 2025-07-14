import pytest
from app.filters.equals_filter import EqualsFilter
from app.tests.filters.fixtures import number_data,string_data,mixed_data



def test_number_equals(number_data):
    filter = EqualsFilter()
    result = filter.apply(number_data, "price", 200)
    assert len(result) == 1
    assert result[0]["id"] == 2

def test_string_equals(string_data):
    filter = EqualsFilter()
    result = filter.apply(string_data, "status", "new")
    assert len(result) == 2
    assert {item["id"] for item in result} == {1, 3}

def test_mixed_data_equals(mixed_data):
    filter = EqualsFilter()
    result = filter.apply(mixed_data, "name", "iPhone")
    assert len(result) == 1
    assert result[0]["id"] == 1

def test_string_vs_number_equals(mixed_data):
    filter = EqualsFilter()
    result = filter.apply(mixed_data[:2], "price", "200")  # строка vs число
    assert len(result) == 1
    assert result[0]["id"] == 2