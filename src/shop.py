class Product:
    """
    Класс для представления продукта в магазин
    """

    def __init__(
        self, product_name: str, product_description: str, price: int, quantity: int
    ):
        """
        Инициализация продукта
        :param product_name:
        :param product_description:
        :param price:
        :param quantity:
        """
        self.product_name = product_name
        self.product_description = product_description
        self.price = price
        self.quantity = quantity


class Category:
    """
    хранение + инициализация продуктов
    """

    count_products = 0
    count_category = 0

    def __init__(self, category_name: str, category_description: str, products: list):
        self.category_name = category_name
        self.category_description = category_description
        self.products = products

        Category.count_products += len(products)

        Category.count_category += 1
