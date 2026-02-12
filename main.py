from fastapi import FastAPI, Header, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List
import models
from database import Base, SessionLocal, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Asi's Book API")

class BookCreate(BaseModel):
    title: str
    author: str

class BookRead(BookCreate):
    id: int

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


API_KEY = "aS1iS2iP3hO-1a0b8c9e-9c3b-4d5e-8f2b-123456789012"

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")


@app.get("/")
def home():
    return {"message": "Welcome to Asi's Book API!"}

@app.get("/books", response_model=List[BookRead], dependencies=[Depends(verify_api_key)])
def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()


@app.post("/books", response_model=BookRead, dependencies=[Depends(verify_api_key)])
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(title=book.title, author=book.author)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.put("/books/{book_id}", response_model=BookRead, dependencies=[Depends(verify_api_key)])
def update_book(book_id: int, updated_book: BookCreate, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db_book.title = updated_book.title
    db_book.author = updated_book.author
    db.commit()
    db.refresh(db_book)
    return db_book

@app.patch("/books/{book_id}", response_model=BookRead, dependencies=[Depends(verify_api_key)])
def partial_update_book(book_id: int, updated_fields: BookCreate, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    if updated_fields.title is not None:
        db_book.title = updated_fields.title
    if updated_fields.author is not None:
        db_book.author = updated_fields.author
    db.commit()
    db.refresh(db_book)
    return db_book

@app.delete("/books/{book_id}", dependencies=[Depends(verify_api_key)])
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return {"message": "Book deleted successfully"}
