

class Product:

    def __init__(self, product_name: str, product_description: str, price: int, quantity: int):
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


if __name__ == "__main__":
    prod1 = Product("LG", "Телевизор", 50_000, 5)
    prod2 = Product("Samsung", "Монитор", 100_000, 15)
    prod3 = Product("Apple", "Ipad", 78_000, 45)

    cat1 = Category("Электроника", "Техника для дома", [prod1, prod2])

    print(Category.count_category)
    print(Category.count_product)

    cat2 = Category("Телефоны", "Личного пользования", [prod3])

    print()
    print(Category.count_category)
    print(Category.count_product)



