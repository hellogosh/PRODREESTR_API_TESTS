markdown
# Product Registry API Tests

Автоматизированные API тесты для сервиса «Реестр Продуктов» с использованием `requests` и `pytest`.

## 🚀 Быстрый старт

### 1. Клонирование и настройка

Клонируйте репозиторий:
```bash
git clone https://github.com/hellogosh/PRODREESTR_API_TESTS.git
```
Перейдите в директорию проекта:

```bash
cd PRODREESTR_API_TESTS
```
Создайте виртуальное окружение:

```bash
python -m venv venv
```
Активируйте виртуальное окружение:
```bash
source venv/bin/activate #если macOS/Linux:
```
```bash
venv\Scripts\activate # если Windows:
```
Установите зависимости:

```bash
pip install -r requirements.txt
```
### 2. Настройка окружения
Скопируйте файл окружения:

```bash
cp .env.example .env
```
Отредактируйте файл .env и укажите ваши учетные данные:

env
### Обязательные поля
BASE_URL=https://product-registry-test.emias.ru

TOKEN=your_jwt_token_here

### Опциональные поля (для автоматического получения токена)
CLIENT_ID=dit

CLIENT_SECRET=your_client_secret

USERNAME=test_user

PASSWORD=test_pass

### 3. Запуск тестов
Запустите все тесты:

```bash
pytest -v
```
Запустите конкретный тест:

```bash
pytest tests/test_section.py -v
```
### Структура проекта
```
PRODREESTR_API_TESTS/
├── src/
│   ├── api_client.py      # Базовый API клиент (requests)
│   ├── models/            # Pydantic модели для валидации
│   ├── utils/             # Утилиты (helpers, payload_factory)
│   └── auth.py            # Авторизация и получение токена
├── tests/                 # Тесты
│   ├── conftest.py        # Фикстуры pytest
│   ├── test_sections.py
│   ├── test_product_types.py
│   └── test_products.py
├── .env                   # Переменные окружения (игнорируется git)
├── .env.example           # Шаблон переменных окружения
├── requirements.txt       # Зависимости
└── README.md
```
### Технологии и библиотеки
Python 3.9+ – основной язык программирования

Pytest – фреймворк для организации и запуска тестов

Requests – работа с HTTP-запросами для API-тестирования

Pydantic – валидация данных и моделирование ответов API

Faker – генерация тестовых данных

python-dotenv – управление переменными окружения

### Покрытие тестирования
#### Разделы (Sections):

✅ Создание раздела

✅ Получение списка разделов

✅ Обновление раздела

✅ Удаление раздела

#### Типы продуктов (Product Types)

✅ Создание типа

✅ Получение типов по разделу

✅ Обновление типа

✅ Удаление типа

✅ Проверка дублей (разные разделы – разрешено)

#### Продукты (Products)

✅ Получение списка продуктов

✅ Создание продукта

✅ Обновление продукта

✅ Удаление продукта


### Особенности реализации
API клиент: Инкапсулирует всю логику HTTP-запросов, управление сессией и заголовками

Pydantic модели: Обеспечивают валидацию ответов API и удобную работу с данными

Фикстуры: Автоматическое создание и удаление тестовых данных (разделы, типы, продукты)

Payload фабрики: Централизованное формирование тестовых данных для запросов
