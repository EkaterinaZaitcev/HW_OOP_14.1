import pytest


def test_category(category1, category2):
    assert category1.name == "Смартфоны"
    assert category1.description == "Смартфоны, как средство."
    assert (
            category1.get_product_list == "product1, 100.0 руб. Остаток: 2 шт.\nproduct2, 90.0 руб. Остаток: 17 шт.\n"
    )
    assert category1.category_count == 2
    assert category2.category_count == 2

    assert category1.product_count == 5
    assert category2.product_count == 5


def test_get_product_list(category1, category2):
    with pytest.raises(AttributeError):
        print(category1.__products)
        assert (
            category1.get_product_list == "product1, 100.0 руб. Остаток: 2 шт.\nproduct2, 90.0 руб. Остаток: 17 шт.\n"
        )
        assert (
            category2.get_product_list == "product3, 400.0 руб. Остаток: 5 шт.\nproduct4, 560.0 руб. Остаток: 14 шт."
                                          "\nproduct5, 570.0 руб. Остаток: 13 шт."
        )


def test_category_str(category1):
    assert str(category1) == "Смартфоны, количество продуктов: 19 шт."


def test_category_iterator(category_iterator):
    iter(category_iterator)
    assert category_iterator.index == 0
    assert next(category_iterator).name == 'product1'
    assert next(category_iterator).name == 'product2'

    with pytest.raises(StopIteration):
        next(category_iterator)
