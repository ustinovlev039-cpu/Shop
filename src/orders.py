from src.abstaracts import BaseOrder

class ValueOrderError(Exception):
    """
    Класс, вызова ошибки товара на его кол-во
    """
    pass


class Orders(BaseOrder):
    """
    Класс ссылается на какой товар был куплен, количество товара и его стоимость
    """

    def __init__(self, name_order, quantity_orders, price_order):
            self.name_order = name_order
            self.quantity_orders = quantity_orders
            self.price_order = price_order
            self.items = []

    def add_order(self, new_quantity, product):
        try:
            if new_quantity == 0:
                raise ValueOrderError("Товар с не нулевым кол-во не может быть добавлен")
            self.items.append(new_quantity)

        except ValueOrderError as e:
            print(e)
            raise
        else:
            print("Успешное добавление товара")
        finally:
            print("Обработка добавление товара завершена")


    def total_cost(self) -> float:
        return sum(qty * price for _, qty, price in self.items)

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
