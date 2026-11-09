from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from app.db.db import get_db
from app.db import crud
from app.schemas import BookCreate, BookUpdate, BookResponse

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/", response_model=list[BookResponse])
def list_books(category_id: Optional[int] = None, db: Session = Depends(get_db)):
    return crud.get_all_books(db, category_id=category_id)

@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book

@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    if not crud.get_category(db, book.category_id):
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return crud.create_book(db, **book.model_dump())

@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    data = book.model_dump(exclude_unset=True)
    if data.get("category_id") is not None and not crud.get_category(db, data["category_id"]):
        raise HTTPException(status_code=404, detail="Категория не найдена")
    updated = crud.update_book(db, book_id, **data)
    if not updated:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return updated

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_book(db, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return {"message": "Книга удалена"}
