# Проект: E-commerce Shop 

Учебный проект на Python, моделирующий базовую структуру бэкенда для интернет-магазина.
Проект включает в себя реализацию классов для работы с товарами и категориями, а также систему автоматического подсчета количества объектов.

## Функционал

* **Класс Product**: описывает товар (название, описание, цена, количество).
* **Класс Category**: группирует товары. Хранит список товаров, название категории и описание.
* **Подсчет статистики**: автоматический подсчет общего количества категорий и продуктов при их создании.
* **Класс Smartphone**: наследует `Product`, добавляет специфические атрибуты для смартфонов, такие как производительность, модель, объем памяти и цвет.
* **Класс LawnGrass**: наследует `Product`, добавляет атрибуты для газонной травы, такие как страна происхождения, срок прорастания и цвет.
* **Метод add_product**: добавление продуктов в категорию с проверкой типа.
* **Метод new_product**: создание нового продукта или обновление существующего.

## Технологии

* **Python** 3.11+
* **Poetry** — инструмент для управления зависимостями и сборки.
* **Pytest** — фреймворк для тестирования.
* **Pytest-cov** — плагин для проверки покрытия кода тестами.

## Установка и настройка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ustinovlev039-cpu/Pet_project.git
   cd Pet_project


## Установка и настройка

**Клонируйте репозиторий:**
   ```bash
   git clone [https://github.com/ustinovlev039-cpu/Pet_project.git](https://github.com/ustinovlev039-cpu/Pet_project.git)
   cd Pet_project
   ```
   
# Пример использования
~~~python 
from src.shop import Product, Category, Smartphone, LawnGrass

tv = Product("Samsung", "Smart TV", 50000, 10)
phone = Product("iPhone", "Apple Smartphone", 100000, 5)

electronics = Category("Электроника", "Техника для дома", [tv, phone])

print(electronics.category_name)       
print(len(electronics.products))       
print(Category.count_category)         

smartphone = Smartphone("Samsung Galaxy S23", "256GB, Серый цвет", 180000, 5, 95.5, "S23 Ultra", 256, "Серый")
electronics.add_product(smartphone)

grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
electronics.add_product(grass)
         
~~~


