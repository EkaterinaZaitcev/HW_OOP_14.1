import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def test_product():
    return Product("Салат", "Салат с помидорами", 310.0, 14)


@pytest.fixture()
def test_category():
    return Category("Смартфоны", "Смартфоны, как средство.", "[product_1]")
