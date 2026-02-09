from src.shop import Product


def test_miksim(conclusion_miksim_product_1, conclusion_miksim_product_2):
    new_product_1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    new_product_2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert new_product_1.__dict__ == conclusion_miksim_product_1.__dict__
    assert new_product_2.__dict__ == conclusion_miksim_product_2.__dict__
