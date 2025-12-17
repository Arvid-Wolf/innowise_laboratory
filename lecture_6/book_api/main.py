from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

import models
from database import SessionLocal, engine, Base
import schemas

# create tabel
Base.metadata.create_all(bind=engine)

# create FastAPI app
app = FastAPI(title="Book Collection API")

# get db sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# endpoint for lecture_6 Docker
@app.get("/healthcheck")
async def healthcheck() -> dict:
    return {"status": "ok"}

# create new book
@app.post("/books/", response_model=schemas.BookOut, status_code=201)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(title=book.title, author=book.author, year=book.year)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# get all books
@app.get("/books/", response_model=List[schemas.BookOut])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Book).offset(skip).limit(limit).all()

# delete book by ID
@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return

# update existing book
@app.put("/books/{book_id}", response_model=schemas.BookOut)
def update_book(book_id: int, book_in: schemas.BookUpdate, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    if book_in.title is not None:
        book.title = book_in.title
    if book_in.author is not None:
        book.author = book_in.author
    if book_in.year is not None:
        book.year = book_in.year
    db.commit()
    db.refresh(book)
    return book

# search book
@app.get("/books/search/", response_model=List[schemas.BookOut])
def search_books(q: Optional[str] = Query(None, description="search by title or author"),
                 year: Optional[int] = Query(None, description="filter by year"),
                 db: Session = Depends(get_db)):
    query = db.query(models.Book)
    if q:
        pattern = f"%{q}%"
        query = query.filter((models.Book.title.contains(q)) | (models.Book.author.contains(q)))
    if year is not None:
        query = query.filter(models.Book.year == year)
    return query.all()
