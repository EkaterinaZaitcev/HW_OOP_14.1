def test_category(category):
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство."
    assert category.products == "[product_1]"
    assert category.category_count == 1
    assert category.product == 1