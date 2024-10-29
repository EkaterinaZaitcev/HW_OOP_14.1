from typing import List, Any

from src.product import Product


class Category:
    """Класс для создания категории"""
    name: str
    description: str
    products: List
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Метод для инициализации категории"""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count = len(products)


    def category(self):
        """Добавление категорий"""
        return f"Category(name={self.name}," f"description={self.description}," f"product={self.products})"


    def add_product(self) -> Any:
        """Добавление продукта"""
        self.__products.append(Product)
        Category.products +=1

    @property
    def get_product_list(self) -> str:
        """Вывод списка продуктов"""
        product_list = ""
        for product in self.__products:
            product_list += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_list
