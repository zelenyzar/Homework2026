import pytest

from src.task import Product


def test_product_init(product_1):
    assert product_1.name == "milk"
    assert product_1.price == 150.05
    assert product_1.description == "diary product"
    assert product_1.quantity == 3


def test_category_init(category_1, category_2):
    assert category_1.name == "diary product"
    assert category_1.category_count == 2
    assert category_2.name == "meat"
    assert len(category_1.products) == 2
    assert category_2.product_count == 5


def test_product_1(product_1, capsys):
    product_1.price = 5
    assert product_1.price == 5
    product_1.price = -10
    message = capsys.readouterr()
    assert message.out == "Цена не должна быть нулевая или отрицательная\n"


def test_product_2():
    with pytest.raises(ValueError):
        Product(name="beef", description="meat", price=11.0, quantity=0)


def test_add_product(product_1, category_1):
    category_1.add_product(product_1)
    assert len(category_1.products) == 3


def test_category_products(category_1):
    assert category_1.products == ["milk, 22.0 руб. Остаток: 3 шт.", "ice cream, 33.0 руб. Остаток: 4 шт."]


def test_new_product():
    prod = {"name": "beef", "description": "meat", "price": 11.0, "quantity": 2}
    prod1 = Product.new_product(prod)
    assert prod1.name == "beef"


def test_add_product_1(product_1, product_2, category_1):
    assert round(product_1 + product_2, 1) == 461.2
    with pytest.raises(TypeError):
        product_1 + category_1


def test_str(product_1, category_2):
    assert str(product_1) == "milk, 150.05 руб. Остаток: 3 шт."
    assert str(category_2) == "meat, количество продуктов: 5 шт."


def test_add_product_2(sub_smartphone, sub_lawngrass, category_1, capsys):
    category_1.add_product(sub_smartphone)
    assert category_1.products == [
        "milk, 22.0 руб. Остаток: 3 шт.",
        "ice cream, 33.0 руб. Остаток: 4 шт.",
        "Iphone, 20000.0 руб. Остаток: 8 шт.",
    ]
    category_1.add_product(sub_lawngrass)
    assert category_1.products == [
        "milk, 22.0 руб. Остаток: 3 шт.",
        "ice cream, 33.0 руб. Остаток: 4 шт.",
        "Iphone, 20000.0 руб. Остаток: 8 шт.",
        "grass, 2000000000000 руб. Остаток: 525 шт.",
    ]
    category_1.add_product("море волнуется раз")
    message = capsys.readouterr().out
    assert message == "Добавлять можно только продукт!\n"


def test_middle_price(category_1, category_3):
    assert category_1.middle_price() == 27.5
    assert category_3.middle_price() == 0
