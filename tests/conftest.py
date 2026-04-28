import pytest

from src.subproducts import LawnGrass, Smartphone
from src.task import Category, Product


@pytest.fixture
def category_1():
    return Category(
        name="diary product",
        description="diary products",
        products=[
            Product(name="milk", price=22.0, description="diary product", quantity=3),
            Product(name="ice cream", price=33.0, description="diary product", quantity=4),
        ],
    )


@pytest.fixture
def category_2():
    return Category(
        name="meat",
        description="meat",
        products=[
            Product(name="beef", price=11.0, description="meat", quantity=1),
            Product(name="eggs", price=44, description="meat", quantity=2),
            Product(name="eggs", price=44, description="meat", quantity=2),
        ],
    )


@pytest.fixture
def product_1():
    return Product(name="milk", price=150.05, description="diary product", quantity=3)


@pytest.fixture
def product_2():
    return Product(name="beef", price=11.0, description="meat", quantity=1)


@pytest.fixture
def sub_smartphone():
    return Smartphone(
        name="Iphone",
        price=20000.0,
        description="cell phone",
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
        price=2000000000000,
        description="elite sort",
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
