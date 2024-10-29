

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
        self.__price = price
        self.quantity = quantity


    def product(self):
        """Добавление продукта"""
        return (
            f"Product(name={self.name},"
            f"description={self.description},"
            f"price={self.price},"
            f"quantity={self.quantity})"
        )


if __name__ == "__main__":
    product_1 = Product("Салат", "Салат с помидорами", 310.0, 14)
    print(product_1)

