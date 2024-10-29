import json
import os
from typing import Any

from src.product import Product
from src.category import Category

def read_json_file(path:str) -> Any:
    """Преобразует файл JSON в словарь"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


result = read_json_file("..//data/products.json")


def create_object_from_json(data: dict) -> Any:
    """Преобразует данные из словаря в объекты класса"""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
            name = category["name"]
            description = category["description"]
            category_instance = Category(name, description, products)
            categories.append(category_instance)
        return categories


result_2 = create_object_from_json(result)
print(result_2)