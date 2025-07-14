import pytest
from app.aggregate.max_aggregator import MaxAggregator
from app.tests.aggregators.fixtures import number_data, mixed_data


def test_max_with_number_data(number_data):
    aggregator = MaxAggregator()
    result = aggregator.aggregated(number_data, "price")
    assert result == 200

def test_max_with_mixed_types(mixed_data):
    aggregator = MaxAggregator()
    with pytest.raises(ValueError):
        result = aggregator.aggregated(mixed_data[:2], "rating")
        assert result == pytest.approx(4.8)

def test_max_with_all_invalid():
    aggregator = MaxAggregator()
    with pytest.raises(ValueError):
        aggregator.aggregated([{"price": "N/A"}], "price")