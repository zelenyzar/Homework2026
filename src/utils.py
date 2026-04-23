import json
import os
from fileinput import filename
from typing import Any

from src.task import Category, Product


def read_json(filename: str) -> dict[str, Any]:
    """Функция чтения json-файла"""
    full_path = os.path.join(os.path.dirname(__file__), "..", "data", filename)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: dict[str, Any]) -> dict[str, Any]:
    """Функция, которая создаёт объекты из файла json"""
    categories = []
    for category in data:
        products_new = []
        for product in category["products"]:
            products_new.append(Product(**product))
        category["products"] = products_new
        categories.append(Category(**category))
    return categories
