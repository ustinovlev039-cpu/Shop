import pytest


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

    assert "Samsung Galaxy S23 Ultra, 180000.0. Остаток: 5" in text
    assert "Iphone 15, 210000.0. Остаток: 8" in text
    assert "Xiaomi Redmi Note 11, 31000.0. Остаток: 14" in text
    assert "55 QLED 4K, 123000.0. Остаток: 7" in text


def test_add_category(category1, category2, product4):
    category1.add_product(product4)
    assert category1.products == category2.products


def test_new_product(product1, product):
    p = product1.new_product(None, product)

    assert p.product_name == "Test"
    assert p.product_description == "Desc"
    assert p.price == 100.0
    assert p.quantity == 2
