class Product:
    """
    Класс для представления продукта в магазин
    """

    @property
    def price(self):
        return self._price

    def __init__(
        self, product_name: str, product_description: str, price: int, quantity: int):
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
    def property(self):
        return self._price

    @price.setter
    def price(self, new_price):
        ans_change_price = input("Согласны ли понизить цену или отмены действия соответственно ?")
        if ans_change_price.lower().strip() == "y":
            if new_price.price <= 0:
                return "Цена не должна быть нулевая или отрицательная"
        else:
            self._price = new_price


    @classmethod
    def new_product(cls, product_data, product_list):
        new_prod =  cls(**product_data)

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
            line = f"{product.product_name}, {product.price}. Остаток: {product.quantity}"
            product_list_output.append(line)

        return "\n".join(product_list_output)



if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.products)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.count_products)

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)