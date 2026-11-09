from app.db.models import Category, Book

def create_category(db, **data):
    category = Category(**data)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def get_category(db, category_id):
    return db.query(Category).filter(Category.id == category_id).first()

def get_all_categories(db):
    return db.query(Category).all()

def update_category(db, category_id, **data):
    category = get_category(db, category_id)
    if not category:
        return None
    for key, value in data.items():
        if value is not None:
            setattr(category, key, value)
    db.commit()
    db.refresh(category)
    return category

def delete_category(db, category_id):
    category = get_category(db, category_id)
    if not category:
        return None
    db.delete(category)
    db.commit()
    return category

def create_book(db, **data):
    book = Book(**data)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_book(db, book_id):
    return db.query(Book).filter(Book.id == book_id).first()

def get_all_books(db, category_id=None):
    query = db.query(Book)
    if category_id is not None:
        query = query.filter(Book.category_id == category_id)
    return query.all()

def update_book(db, book_id, **kwargs):
    book = get_book(db, book_id)
    if not book:
        return None
    for key, value in kwargs.items():
        if value is not None:
            setattr(book, key, value)
    db.commit()
    db.refresh(book)
    return book

def delete_book(db, book_id):
    book = get_book(db, book_id)
    if not book:
        return None
    db.delete(book)
    db.commit()
    return book
