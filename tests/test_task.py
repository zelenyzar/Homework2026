from src.task import Category


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

