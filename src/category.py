from typing import List


class Category:
    """Класс для создания категории"""
    name: str
    description: str
    product: List
    category_count = 0
    product_count = 0

    def __init__(self, name, description, product):
        """Метод для инициализации категории"""
        Category.category_count += 1
        Category.product_count = len(product)
        self.name = name
        self.description = description
        self.product = product

    def category(self):
        """Добавление категорий"""
        return f"Category(name={self.name}," f"description={self.description}," f"product={self.product})"


"""if __name__ == "__main__":
    category_1 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         "[product_1]")
    print(category_1)"""