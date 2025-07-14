import pytest
from app.aggregate.avg_aggregator import AvgAggregator
from app.tests.aggregators.fixtures import number_data, mixed_data

def test_avg_with_number_data(number_data):
    aggregator = AvgAggregator()
    result = aggregator.aggregated(number_data, "price")
    assert result == pytest.approx(116.6666667)

def test_avg_with_string_numbers(mixed_data):
    aggregator = AvgAggregator()
    with pytest.raises(ValueError):
        result = aggregator.aggregated(mixed_data[:2], "price")  # только валидные
        assert result == 150

def test_avg_with_invalid_data(mixed_data):
    aggregator = AvgAggregator()
    with pytest.raises(ValueError):
        aggregator.aggregated(mixed_data, "price")

