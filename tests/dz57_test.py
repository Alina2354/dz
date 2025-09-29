import pytest
from dz57 import get_max_price

@pytest.fixture
def products_fixture():
    return [
        {"name": "A", "price": 100},
        {"name": "B", "price": 250},
        {"name": "C", "price": 180},
    ]

def test_get_max_price_with_fixture(products_fixture):
    assert get_max_price(products_fixture) == 250

def test_get_max_price_empty_list():
    assert get_max_price([]) is None

def test_get_max_price_same_price():
    products = [
        {"name": "A", "price": 100},
        {"name": "B", "price": 100},
        {"name": "C", "price": 100},
    ]
    assert get_max_price(products) == 100

def test_get_max_price_negative_prices():
    products = [
        {"name": "A", "price": -100},
        {"name": "B", "price": -250},
        {"name": "C", "price": -180},
    ]
    assert get_max_price(products) == -100

def test_get_max_price_missing_price():
    products = [
        {"name": "A"},
        {"name": "B", "price": 250},
        {"name": "C", "price": 180},
    ]
    assert get_max_price(products) == 250

def test_get_max_price_none_price():
    products = [
        {"name": "A", "price": None},
        {"name": "B", "price": 250},
        {"name": "C", "price": 180},
    ]
    assert get_max_price(products) == 250