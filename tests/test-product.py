import pytest


def test_products(add_product):
    assert add_product.name == "Xiaomi Redmi Note 11"
    assert add_product.description == "1024GB, Синий"
    assert add_product.price == 31000.0
    assert add_product.quantity == 14