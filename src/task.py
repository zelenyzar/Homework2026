from typing import List


class Product:
    """класс Product"""

    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name: str, price: float, description: str, quantity: int) -> None:
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity


class Category:
    """класс Category"""

    name: str
    description: str
    products: List[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(self.products) if self.products else 0

