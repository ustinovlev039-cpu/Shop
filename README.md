# Shop (E-commerce, учебный проект)

Учебный проект на **Python**, в котором реализована упрощённая “бэкенд-логика” интернет-магазина на уровне **ООП-модели**: товары, категории, наследование, валидация данных, счётчики объектов и тесты.


---

## Что внутри

### Основные сущности
- **Product** — товар: имя, описание, цена, количество, строковое представление, сложение товаров (по суммарной стоимости остатков).
- **Category** — категория: имя, описание, список товаров, добавление товара с проверкой типа, вывод состава категории.
- **Smartphone** — наследник `Product` (доп. поля: эффективность/производительность, модель, память, цвет).
- **LawnGrass** — наследник `Product` (доп. поля: страна, срок прорастания, цвет).

Также:
- **BaseTask (ABC)** — абстрактный базовый класс (контракт для `Product`).
- **MixsimLog** — миксин для логирования/`repr` при создании объектов.

:contentReference[oaicite:1]{index=1}

---

## Технологии

- Python **3.11+**
- **Poetry** (зависимости/окружение)
- **Pytest** + **pytest-cov**
- инструменты качества кода: **flake8 / black / isort / mypy**

:contentReference[oaicite:2]{index=2}

---

## Структура проекта

```text
├─ src/
│ ├─ shop.py # Product, Category, Smartphone, LawnGrass
│ ├─ abstaracts.py # ABC-контракты (BaseTask, BaseOrder)
│ └─ micsim.py # MixsimLog (repr/logging)
├─ tests/
│ ├─ conftest.py # фикстуры
│ └─ test_shop.py # тесты
├─ main.py # пример запуска
├─ pyproject.toml
└─ README.md
```

--- 

## Установка и запуск

### 1) Клонирование
```bash
git clone https://github.com/ustinovlev039-cpu/Shop.git
cd Shop
```

### 2) Установка зависимостей (Poetry)
```bash
poetry install
```

3) Запуск примера
```bash
poetry run python main.py
```

### Пример использования
```python
from src.shop import Product, Category, Smartphone, LawnGrass

tv = Product("Samsung", "Smart TV", 50000, 10)
phone = Product("iPhone", "Apple Smartphone", 100000, 5)

electronics = Category("Электроника", "Техника для дома", [tv, phone])

print(electronics.category_name)
print(electronics.products)  # выводит список товаров (строками)

smartphone = Smartphone(
    "Samsung Galaxy S23 Ultra",
    "256GB, Серый цвет, 200MP камера",
    180000.0,
    5,
    95.5,
    "S23 Ultra",
    256,
    "Серый",
)
electronics.add_product(smartphone)

grass = LawnGrass(
    "Газонная трава",
    "Элитная трава для газона",
    500.0,
    20,
    "Россия",
    "7 дней",
    "Зеленый",
)
electronics.add_product(grass)
```

## Тесты

### Запуск тестов:
```bash
poetry run pytest
```

### Покрытие:
```bash
poetry run pytest --cov
```

Тестами проверяются:

- валидация цены (ошибка при <= 0)
- строковые представления
- сложение товаров
- добавление товара в категорию и проверка типа
- корректность полей у Smartphone и LawnGrass


### Качество кода
```bash
poetry run black .
poetry run isort .
poetry run flake8
poetry run mypy .
```
