def test_category(category):
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство."
    assert category.product == "[product1]"
    assert category.category_count == 1
    assert category.products_count == 10