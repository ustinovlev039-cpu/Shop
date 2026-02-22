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


def test_smartphone_1(smartphone_1):
    text = smartphone_1
    assert text.product_name == "Samsung Galaxy S23 Ultra"
    assert text.product_description == "256GB, Серый цвет, 200MP камера"
    assert text.price == 180000.0
    assert text.quantity == 5
    assert text.efficiency == 95.5
    assert text.model == "S23 Ultra"
    assert text.memory == 256
    assert text.color == "Серый"


def test_smartphone_2(smartphone_2):
    text = smartphone_2
    assert text.product_name == "Iphone 15"
    assert text.product_description == "512GB, Gray space"
    assert text.price == 210000.0
    assert text.quantity == 8
    assert text.efficiency == 98.2
    assert text.model == "15"
    assert text.memory == 512
    assert text.color == "Gray space"


def test_grass_1(grass_1):
    text = grass_1
    assert text.product_name == "Газонная трава"
    assert text.product_description == "Элитная трава для газона"
    assert text.price == 500.0
    assert text.quantity == 20
    assert text.country == "Россия"
    assert text.germination_period == "7 дней"
    assert text.color == "Зеленый"


def test_grass_2(grass_2):
    text = grass_2
    assert text.product_name == "Газонная трава 2"
    assert text.product_description == "Выносливая трава"
    assert text.price == 450.0
    assert text.quantity == 15
    assert text.country == "США"
    assert text.germination_period == "5 дней"
    assert text.color == "Темно-зеленый"


def test_category_smartphone(category_smartphone):
    text = category_smartphone
    assert text.category_name == "Смартфоны"
    assert text.category_description == "Высокотехнологичные смартфоны"


def test_category_grass(category_grass):
    text = category_grass
    assert text.category_name == "Газонная трава"
    assert text.category_description == "Различные виды газонной травы"


def test_error(category_smartphone):
    with pytest.raises(TypeError):
        category_smartphone.add_product("Не то добавление еееееееее!!!!!")


def test_error_product():
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_error_category():
    category = Category("Пустая категория", "Категория без продуктов", [])
    assert category.middle_price() == 0
