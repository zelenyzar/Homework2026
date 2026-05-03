import pytest


def test_init_subproducts(sub_smartphone, sub_lawngrass):
    assert sub_smartphone.name == "Iphone"
    assert sub_smartphone.efficiency == "fast"
    assert sub_smartphone.memory == "512GB"
    assert sub_lawngrass.name == "grass"
    assert sub_lawngrass.germination_period == "2 years"
    assert sub_lawngrass.color == "yellow"
    assert sub_lawngrass.price == 2000000000000


def test_add_subproducts(sub_smartphone, sub_lawngrass):
    with pytest.raises(TypeError):
        sub_lawngrass + sub_smartphone
