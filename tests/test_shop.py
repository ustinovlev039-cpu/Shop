import pytest

from src.shop import Category, Product


def test_price(product1):
    old = product1.price
    with pytest.raises(ValueError):
        product1.price = 0
    assert product1.price == old

    with pytest.raises(ValueError):
        product1.price = -100
    assert product1.price == old


def test_category_product(category2):
    text = category2.products

    assert "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт." in text
    assert "Iphone 15, 210000.0 руб. Остаток: 8 шт." in text
    assert "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт." in text


def test_add_category(category1, category2, product4):
    category1.add_product(product4)
    assert category1.products == category2.products


def test_new_product(product1, product):
    p = product1.new_product(None, product)

    assert p.product_name == "Test"
    assert p.product_description == "Desc"
    assert p.price == 100.0
    assert p.quantity == 2


def test_product_str(conclusion_product_str):
    product = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    assert str(product) == conclusion_product_str


def test_add(product1, product2, conclusion_product_add):
    sum_ = product1 + product2
    assert sum_ == conclusion_product_add


def test_category_str(category1, conclusion_category_str):
    assert str(category1) == conclusion_category_str
