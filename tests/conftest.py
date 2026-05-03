import pytest

from src.subproducts import LawnGrass, Smartphone
from src.task import Category, Product


@pytest.fixture
def category_1():
    return Category(
        name="diary product",
        description="diary products",
        products=[
            Product(name="milk", description="diary product", price=22.0, quantity=3),
            Product(name="ice cream", description="diary product", price=33.0, quantity=4),
        ],
    )


@pytest.fixture
def category_2():
    return Category(
        name="meat",
        description="meat",
        products=[
            Product(name="beef", description="meat", price=11.0, quantity=1),
            Product(name="eggs", description="meat", price=44, quantity=2),
            Product(name="eggs", description="meat", price=44, quantity=2),
        ],
    )


@pytest.fixture
def product_1():
    return Product(name="milk", description="diary product", price=150.05, quantity=3)


@pytest.fixture
def product_2():
    return Product(name="beef", description="meat", price=11.0, quantity=1)


@pytest.fixture
def sub_smartphone():
    return Smartphone(
        name="Iphone",
        description="cell phone",
        price=20000.0,
        quantity=8,
        efficiency="fast",
        model="15",
        memory="512GB",
        color="Gray space",
    )


@pytest.fixture
def sub_lawngrass():
    return LawnGrass(
        name="grass",
        description="elite sort",
        price=2000000000000,
        quantity=525,
        country="Holland",
        germination_period="2 years",
        color="yellow",
    )


@pytest.fixture
def json_test():
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство для коммуникации",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        }
    ]
