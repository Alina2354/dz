import pytest
from dz54 import unique_products

@pytest.fixture
def sample_products_with_duplicates():
    return [
        {"name": "Товар1", "sku": "A001"},
        {"name": "Товар2", "sku": "A002"},
        {"name": "Товар1", "sku": "A001"},
        {"name": "Товар3", "sku": "A003"},
    ]

@pytest.fixture
def empty_products_list():
    return []

def test_unique_products_with_duplicates(sample_products_with_duplicates):
    products = sample_products_with_duplicates
    unique_products_list = unique_products(products)
    assert len(unique_products_list) == 3
    assert {"name": "Товар1", "sku": "A001"} in unique_products_list
    assert {"name": "Товар2", "sku": "A002"} in unique_products_list
    assert {"name": "Товар3", "sku": "A003"} in unique_products_list

def test_unique_products_with_empty_list(empty_products_list):
    products = empty_products_list
    unique_products_list = unique_products(products)
    assert len(unique_products_list) == 0