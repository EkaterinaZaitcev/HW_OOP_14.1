
def test_add_products(product):
    assert product.name == "Xiaomi"
    assert product.description == "1024GB"
    assert product.price == 31000.0
    assert product.quantity == 14