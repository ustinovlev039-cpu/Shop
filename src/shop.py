class Product:

    def __init__(
        self, product_name: str, product_description: str, price: int, quantity: int
    ):
        self.product_name = product_name
        self.product_description = product_description
        self.price = price
        self.quantity = quantity


class Category:

    count_product = 0
    count_category = 0

    def __init__(self, category_name: str, category_description: str, product: list):
        self.category_name = category_name
        self.category_description = category_description
        self.product = product

        Category.count_product += len(product)

        Category.count_category += 1


