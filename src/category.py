from typing import List, Any

import self

from src.product import Product


class Category:
    """Класс для создания категории"""
    name: str
    description: str
    product: List
    category_count = 0
    products_count = 0

    def __init__(self, name, description, product):
        """Метод для инициализации категории"""
        self.name = name
        self.description = description
        self.__product = product
        Category.category_count += 1
        Category.products_count = len(product)


    def category(self):
        """Добавление категорий"""
        return f"Category(name={self.name}," f"description={self.description}," f"product={self.product})"


    def add_product(self, product: Product) -> Any:
        """Добавление продукта"""
        self.__product.append(Product)
        Category.product +=1

    @property
    def get_product_list(self) -> str:
        """Вывод списка продуктов"""
        product_list = ""
        for product in self.__product:
            product_list += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_list

"""if __name__ == "__main__":
    category_1 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         "[product1]")
    print(category_1)"""