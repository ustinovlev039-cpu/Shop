import pytest

from src.shop import Category, Product


@pytest.fixture
def product1():
    return Product("LG", "Телевизор", 50_000, 5)


@pytest.fixture
def product2():
    return Product("Samsung", "Монитор", 100_000, 15)


@pytest.fixture
def product3():
    return Product("Apple", "Ipad", 78_000, 45)


@pytest.fixture
def category1(product1, product2):
    return Category("Электроника", "Техника для дома", [product1, product2])


@pytest.fixture
def category2(product3):
    return Category("Телефоны", "Личного пользования", [product3])


@pytest.fixture(autouse=True)
def reset_count():
    Category.count_category = 0
    Category.count_product = 0
