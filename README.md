# Books API

REST API для управления книгами и категориями на FastAPI + PostgreSQL.

## Установка

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Запуск

```bash
uvicorn main:app --reload
```

## Эндпоинты

- GET /health — проверка сервера
- GET /categories/ — список категорий
- POST /categories/ — создать категорию
- DELETE /categories/{id} — удалить категорию
- GET /books/ — список книг
- POST /books/ — создать книгу
- DELETE /books/{id} — удалить книгу

## Документация

http://127.0.0.1:8000/docs
