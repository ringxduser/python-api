from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional
from app.db import get_db
from app.models import Book
from app.schemas import BookCreate, BookResponse

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/", response_model=list[BookResponse])
def get_books(category_id: Optional[int] = None, db: Session = Depends(get_db)):
    query = db.query(Book)
    if category_id:
        query = query.filter(Book.category_id == category_id)
    return query.all()

@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = Book(title=book.title, author=book.author, category_id=book.category_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    db.delete(book)
    db.commit()
    return {"message": "Книга удалена"}
