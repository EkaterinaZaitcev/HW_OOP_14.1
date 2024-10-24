
def test_products(product):
    assert product.name == "Салат"
    assert product.description == "Салат с помидорами"
    assert product.price == 310.0
    assert product.quantity == 14