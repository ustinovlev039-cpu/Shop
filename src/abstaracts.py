from abc import ABC, abstractmethod


class BaseTask(ABC):
    """
    Абстракция для класса Product
    """

    @abstractmethod
    def __init__(self, product_name, product_description, price, quantity):
        """Инициализация наших продуктов"""
        pass

    @abstractmethod
    def __str__(self):
        """Вывод имя продукта, цену, и остаток в шт"""
        pass

    @abstractmethod
    def __add__(self, other):
        """Суммирование разных товаров + проверка на ошибку"""
        pass

    @property
    @abstractmethod
    def price(self):
        """Получение цены"""
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        """Проверка цены, что он <= 0 и спрос про изменение цены"""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_list, product_data):
        """добавление нового продукта и сравнение и нахождение наибольшей цены"""
        pass


class BaseOrder(ABC):

    @abstractmethod
    def __init__(self, name_order, quantity_order, price_order):
        pass
