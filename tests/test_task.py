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


def test_product_1(capsys):
    prod_1 = Product(name="milk", price=10.0, description="diary product", quantity=2)
    prod_1.price = 5
    assert prod_1.price == 5
    prod_1.price = -10
    message = capsys.readouterr()
    assert message.out == "Цена не должна быть нулевая или отрицательная\n"


def test_add_product(product_1, category_1):
    category_1.add_product(product_1)
    assert len(category_1.products) == 3


def test_category_products(category_1):
    assert category_1.products == ["milk, 22.0 руб. Остаток: 3 шт.", "ice cream, 33.0 руб. Остаток: 4 шт."]


def test_new_product():
    prod = {"name": "beef", "price": 11.0, "description": "meat", "quantity": 2}
    prod1 = Product.new_product(prod)
    assert prod1.name == "beef"
