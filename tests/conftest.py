import pytest

from src.category import Category
from src.category_iterator import CategoryIterator
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture()
def product1():
    return Product(
        "Iphone 15",
        "512GB, Gray space",
        310.0,
        14
    )


@pytest.fixture()
def product2():
    return Product(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        350.0,
        11
    )


@pytest.fixture()
def category1():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство.",
        [
            Product(
                name="product1",
                description="Description of product1",
                price=100.0,
                quantity=2,
            ),
            Product(
                name="product2",
                description="Description of product2",
                price=90.0,
                quantity=17,
            ),
        ],
    )


@pytest.fixture()
def category2():
    return Category(
        "Телевизоры",
        "Телевизор плоский.",
        [
            Product(
                name="product3",
                description="Description of product3",
                price=400.00,
                quantity=5,
            ),
            Product(
                name="product4",
                description="Description of product4",
                price=560.00,
                quantity=14,
            ),
            Product(
                name="product5",
                description="Description of product5",
                price=570.00,
                quantity=13,
            ),
        ],
    )


@pytest.fixture
def product_dict():
    return {
        "name": "Product6",
        "description": "Description of the product6",
        "price": 144.75,
        "quantity": 21,
    }


@pytest.fixture
def new_price():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 100.0, 11)


@pytest.fixture
def category_iterator(category1):
    return CategoryIterator(category1)


@pytest.fixture
def smartphone1():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                      "S23 Ultra", 256, "Серый")


@pytest.fixture
def smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def grass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def grass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
