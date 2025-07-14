import pytest
from app.aggregate.min_aggeregator import MinAggregate
from app.tests.aggregators.fixtures import number_data, mixed_data

def test_min_with_number_data(number_data):
    aggregator = MinAggregate()
    result = aggregator.aggregated(number_data, "price")
    assert result == 50

def test_min_with_mixed_data(mixed_data):
    aggregator = MinAggregate()
    with pytest.raises(ValueError):
        result = aggregator.aggregated(mixed_data[:2], "price")
        assert result == 100

def test_min_with_invalid_data(mixed_data):
    aggregator = MinAggregate()
    with pytest.raises(ValueError):
        aggregator.aggregated(mixed_data, "price")