from pydantic import BaseModel
from typing import Optional

class CategoryCreate(BaseModel):
    title: str

class CategoryUpdate(BaseModel):
    title: Optional[str] = None

class CategoryResponse(BaseModel):
    id: int
    title: str
    class Config:
        from_attributes = True

class BookCreate(BaseModel):
    title: str
    description: Optional[str] = None
    price: Optional[float] = None
    url: Optional[str] = None
    category_id: int

class BookUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    url: Optional[str] = None
    category_id: Optional[int] = None

class BookResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    price: Optional[float] = None
    url: Optional[str] = None
    category_id: int
    class Config:
        from_attributes = True
