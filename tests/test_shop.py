from src.shop import Category, Product


def test_prod1(product1):
    assert product1.product_name == "LG"
    assert product1.product_description == "Телевизор"
    assert product1.quantity == 5
    assert product1.price == 50_000


def test_prod2(product2):
    assert product2.product_name == "Samsung"
    assert product2.product_description == "Монитор"
    assert product2.price == 100_000
    assert product2.quantity == 15


def test_prod3(product3):
    assert product3.product_name == "Apple"
    assert product3.product_description == "Ipad"
    assert product3.price == 78_000
    assert product3.quantity == 45


def test_category1(category1, product1, product2):
    assert category1.product[1] == product2
    assert category1.product[0] == product1
    assert len(category1.product) == 2


def test_category2(category2, product3):
    assert category2.product[0] == product3


def test_count(category1, category2):
    assert Category.count_category == 2
    assert Category.count_product == 3
