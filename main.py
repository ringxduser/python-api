from fastapi import FastAPI
from app.db import Base, engine
from app.routers_categories import router as categories_router
from app.routers_books import router as books_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Books API")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(categories_router)
app.include_router(books_router)
