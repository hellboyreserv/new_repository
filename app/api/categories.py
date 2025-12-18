from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.db import crud
from app.schemas import CategoryBase, CategoryOut


router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=list[CategoryOut])
def get_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)


@router.post("/", response_model=CategoryOut)
def create_category(category: CategoryBase, db: Session = Depends(get_db)):
    return crud.create_category(db, category.title)
