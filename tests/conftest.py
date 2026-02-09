import pytest

from src.shop import Category, LawnGrass, Product, Smartphone


@pytest.fixture
def product1():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
def product2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product3():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def category1(product1, product2, product3):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )


@pytest.fixture
def product4():
    return Product("55 QLED 4K", "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def category2(product1, product2, product3, product4):
    return Category(
        "Телефоны", "Личного пользования", [product1, product2, product3, product4]
    )


@pytest.fixture
def product():
    data = {
        "product_name": "Test",
        "product_description": "Desc",
        "price": 100.0,
        "quantity": 2,
    }
    return data


@pytest.fixture(autouse=True)
def reset_count():
    Category.count_category = 0
    Category.count_products = 0


@pytest.fixture
def conclusion_product_str():
    return "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


@pytest.fixture
def conclusion_product_add():
    return 2580000.0


@pytest.fixture
def conclusion_category_str():
    return "Смартфоны, количество продуктов: 27 шт."


@pytest.fixture
def smartphone_1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


@pytest.fixture
def smartphone_2():
    return Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )


@pytest.fixture
def grass_1():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


@pytest.fixture
def grass_2():
    return LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )


@pytest.fixture
def category_smartphone(smartphone_1, smartphone_2):
    return Category(
        "Смартфоны", "Высокотехнологичные смартфоны", [smartphone_1, smartphone_2]
    )


@pytest.fixture
def category_grass(grass_1, grass_2):
    return Category(
        "Газонная трава", "Различные виды газонной травы", [grass_1, grass_2]
    )


@pytest.fixture
def conclusion_miksim_product_1():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
def conclusion_miksim_product_2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
