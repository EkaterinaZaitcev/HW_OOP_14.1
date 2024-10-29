from typing import Dict

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

    @classmethod
    def new_product(cls, new_product: Dict):
        """Добавление продукта"""
        name = new_product["name"]
        description = new_product["decription"]
        price = new_product["price"]
        quantity = new_product["quantity"]
        return cls(name, description, price, quantity)


    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value
