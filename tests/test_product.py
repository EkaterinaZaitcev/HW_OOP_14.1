from src.product import Product
from unittest.mock import patch


def test_products(product1, product2):
    assert product1.name == "Iphone 15"
    assert product1.description == "512GB, Gray space"
    assert product1.price == 310.0
    assert product1.quantity == 14

    assert product2.name == "Xiaomi Redmi Note 11"
    assert product2.description == "1024GB, Синий"
    assert product2.price == 350.0
    assert product2.quantity == 11


def test_new_product(product_dict):
    product6=Product.new_product(product_dict)
    assert product6.name == "Product6"
    assert product6.description == "Description of the product6"
    assert product6.price == 144.75
    assert product6.quantity == 21



def test_product_price_setter(capsys, new_price):
    # Изменяем цену на меньшую чем была (требуется подтверждение)
    """new_price = 0.00"""
    message=capsys.readouterr()
    assert message.out.strip() == "Цена понижается с 120000 до 100. Подтверждаете? (y/n)"


