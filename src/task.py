from typing import Any, List, Self


class Product:
    """класс Product"""

    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name: str, price: float, description: str, quantity: int) -> None:
        self.name = name
        self.__price = price
        self.description = description
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Product) -> float | int | str:
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        else:
            return "Допускается складывать только продукты"

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        try:
            if price <= 0:
                raise ValueError("Цена не должна быть нулевая или отрицательная")
        except ValueError as e:
            print(e)
        else:
            self.__price = price

    @classmethod
    def new_product(cls, product: dict[str, Any]) -> Self:
        return cls(product["name"], product["price"], product["description"], product["quantity"])


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
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products) if self.__products else 0

    def __str__(self):
        result = 0
        for product in self.__products:
            result += product.quantity
        return f"{self.name}, количество продуктов: {result} шт."

    @property
    def products(self) -> List[Product]:
        prod_list = []
        for product in self.__products:
            prod_list.append(str(product))
        return prod_list

    def add_product(self, product: Product) -> None:
        """Создает новый продукт"""
        if isinstance(product, Product):
            self.__products.append(product)
