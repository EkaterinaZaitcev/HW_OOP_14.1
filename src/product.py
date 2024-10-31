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

    def __str__(self):
        """Магический метод который возвращает строку"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."


    def __add__(self, other):
        """Метод сложения"""
        if type(other) is Product:
            return self.__price * self.quantity + other.price * other.quantity
        raise TypeError


    @classmethod
    def new_product(cls, new_product: Dict):
        """Добавление продукта"""
        name = new_product["name"]
        description = new_product["description"]
        price = new_product["price"]
        quantity = new_product["quantity"]
        return cls(name, description, price, quantity)


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if self.__price > new_price:
            user_input = input("Изменять цену? Введите y если да,и n если нет")
            if user_input != "y":
                return
            else:
                self.__price = self.__price
