from src.abstaracts import BaseOrder


class Orders(BaseOrder):
    """
    Класс ссылается на какой товар был куплен, количество товара и его стоимость
    """

    def __init__(self, name_order, quantity_orders, price_order):
        self.name_order = name_order
        self.quantity_orders = quantity_orders
        self.price_order = price_order

    def __str__(self):
        return f"Было куплено: {self.name_order}, {self.quantity_orders}. Стоимость: {self.quantity_orders * self.price_order} "


class Category_orders:
    """
    хранение + инициализация
    """

    def __init__(self, category_order_name, category_order_description, order_products):
        self.category_order_name = category_order_name
        self.category_order_description = category_order_description
        self.order_products = order_products
