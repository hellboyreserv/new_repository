from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.db import crud
from app.schemas import BookBase, BookOut

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[BookOut])
def get_books(db: Session = Depends(get_db)):
    return crud.get_books(db)


@router.post("/", response_model=BookOut)
def create_book(book: BookBase, db: Session = Depends(get_db)):
    return crud.create_book(
        db,
        title=book.title,
        description=book.description,
        price=book.price,
        category_id=book.category_id,
        url=book.url
    )
