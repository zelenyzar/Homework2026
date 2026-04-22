import pytest

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
