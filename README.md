# Books API

REST API для управления книгами и категориями на FastAPI + PostgreSQL.

## Структура проекта
app/

├── db/

│   ├── db.py        — подключение к БД, get_db

│   ├── models.py    — модели Category и Book

│   └── crud.py      — CRUD функции

├── api/

│   ├── categories.py — роутер категорий

│   └── books.py      — роутер книг

├── schemas.py        — Pydantic схемы

└── main.py           — сборка приложения, /health
## Установка

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Запуск

```bash
uvicorn app.main:app --reload
```

## Документация

http://127.0.0.1:8000/docs

## Эндпоинты

- GET /health — проверка сервера
- GET /categories/ — список категорий
- GET /categories/{id} — категория по id
- POST /categories/ — создать категорию
- PUT /categories/{id} — обновить категорию
- DELETE /categories/{id} — удалить категорию
- GET /books/ — список книг (фильтр по category_id)
- GET /books/{id} — книга по id
- POST /books/ — создать книгу
- PUT /books/{id} — обновить книгу
- DELETE /books/{id} — удалить книгу