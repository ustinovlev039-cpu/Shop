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

    def __str__(self):
        return f"{self.product_name}, {self._price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self._price * self.quantity + other._price * other.quantity

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

    def __str__(self):
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.category_name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.count_products += 1

    @property
    def products(self):
        return "\n".join(str(p) for p in self.__products)


class Iterator:

    def __init__(self, user):
        self.user = user

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.user.products):
            product = self.user[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
