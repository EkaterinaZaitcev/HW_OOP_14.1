from typing import List


class Category:
    """Класс для создания категории"""
    name: str
    description: str
    products: List
    category_count = 0
    product_count = 0


    def __init__(self, name, description, products):
        """Метод для инициализации категории"""
        Category.category_count += 1
        Category.product_count = len(products)
        self.name = name
        self.description = description
        self.products = products


    def add_category(self):
        """Добавление категорий"""
        return f"Category(name={self.name}," f"description={self.description}," f"products={self.products})"


