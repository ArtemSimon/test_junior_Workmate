import pytest
from app.filters.smaller_than_filter import SmallerThanFilter
from app.tests.filters.fixtures import number_data,string_data,mixed_data



def test_number_smaller_filter(number_data):
    filter = SmallerThanFilter()
    result = filter.apply(number_data, "price", 150)
    assert len(result) == 2
    assert {item["id"] for item in result} == {1, 3}

def test_string_smaller_filter(string_data):
    filter = SmallerThanFilter()
    filter.apply(string_data, "name", "iPhone")

def test_mixed_data_smaller_filter(mixed_data):
    filter = SmallerThanFilter()
    result = filter.apply(mixed_data[:2], "price", 150)
    assert len(result) == 1
    assert result[0]["id"] == 1
