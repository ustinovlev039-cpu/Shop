# Проект: E-commerce Shop 

Учебный проект на Python, моделирующий базовую структуру бэкенда для интернет-магазина.
Проект включает в себя реализацию классов для работы с товарами и категориями, а также систему автоматического подсчета количества объектов.

## Функционал

* **Класс Product**: описывает товар (название, описание, цена, количество).
* **Класс Category**: группирует товары. Хранит список товаров, название категории и описание.
* **Подсчет статистики**: автоматический подсчет общего количества категорий и продуктов при их создании.

## Технологии

* **Python** 3.11+
* **Poetry** — инструмент для управления зависимостями и сборки.
* **Pytest** — фреймворк для тестирования.
* **Pytest-cov** — плагин для проверки покрытия кода тестами.

## Установка и настройка

**Клонируйте репозиторий:**
   ```bash
   git clone [https://github.com/ustinovlev039-cpu/Pet_project.git](https://github.com/ustinovlev039-cpu/Pet_project.git)
   cd Pet_project
   ```
   
# Пример использования
~~~python 
from src.shop import Product, Category

tv = Product("Samsung", "Smart TV", 50000, 10)
phone = Product("iPhone", "Apple Smartphone", 100000, 5)

electronics = Category("Электроника", "Техника для дома", [tv, phone])

print(electronics.category_name)       
print(len(electronics.products))       
print(Category.count_category)         
~~~


