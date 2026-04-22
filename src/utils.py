import json
import os
from typing import Any

from src.task import Category, Product


def read_json(path: str) -> dict[str, Any]:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: dict[str, Any]) -> dict[str, Any]:
    categories = []
    for category in data:
        products_new = []
        for product in category["products"]:
            products_new.append(Product(**product))
        category["products"] = products_new
        categories.append(Category(**category))
    return categories



