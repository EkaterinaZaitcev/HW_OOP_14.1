

class Product:
    """Класс для добавления продукта"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации продукта"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def add_product(self):
        """Добавление продукта"""
        return (
            f"Product(name={self.name},"
            f"description={self.description},"
            f"price={self.price},"
            f"quantity={self.quantity}"
        )


"""if __name__ == "__main__":
    product_1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product_2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product_3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    print(product_1)
    print(product_2)
    print(product_3)"""
