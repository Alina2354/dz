import pytest
from dz55 import filter_orders_by_status

@pytest.fixture
def sample_orders():
    return [
        {"id": 1, "status": "new"},
        {"id": 2, "status": "shipped"},
        {"id": 3, "status": "new"},
    ]

@pytest.fixture
def empty_orders_list():
    return []

def test_filter_orders_by_status(sample_orders):
    orders = sample_orders
    filtered_orders = filter_orders_by_status(orders, "new")
    assert len(filtered_orders) == 2
    assert {"id": 1, "status": "new"} in filtered_orders
    assert {"id": 3, "status": "new"} in filtered_orders

def test_filter_orders_by_status_empty_list(empty_orders_list):
    orders = empty_orders_list
    filtered_orders = filter_orders_by_status(orders, "new")
    assert len(filtered_orders) == 0