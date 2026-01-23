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
        self._price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")

        elif new_price < self._price:
            ans_change_price = input(
                "Согласны ли понизить цену или отмены действия соответственно ?"
            )
            if ans_change_price.lower().strip() == "y":
                self._price = new_price
            else:
                return

        else:
            self._price = new_price

    @classmethod
    def new_product(cls, product_list, product_data):
        new_prod = cls(**product_data)

        if product_list is None:
            return new_prod

        for prod in product_list:
            if prod.product_name == new_prod.product_name:
                prod.quantity += new_prod.quantity
                prod.price = max(prod.price, new_prod.price)
                return prod

        return new_prod


class Category:
    """
    хранение + инициализация продуктов
    """

    count_products = 0
    count_category = 0

    def __init__(self, category_name: str, category_description: str, products: list):
        self.category_name = category_name
        self.category_description = category_description
        self.__products = products

        Category.count_products += len(products)

        Category.count_category += 1

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.count_products += 1

    @property
    def products(self):
        product_list_output = list()
        for product in self.__products:
            line = (
                f"{product.product_name}, {product.price}. Остаток: {product.quantity}"
            )
            product_list_output.append(line)

        return "\n".join(product_list_output)
