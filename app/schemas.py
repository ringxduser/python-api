from pydantic import BaseModel
from typing import Optional

class CategoryCreate(BaseModel):
    name: str

class CategoryResponse(BaseModel):
    id: int
    name: str
    class Config:
        from_attributes = True

class BookCreate(BaseModel):
    title: str
    author: str
    category_id: int

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    category_id: int
    class Config:
        from_attributes = True
