from pydantic import BaseModel


# -------- Categories --------
class CategoryBase(BaseModel):
    title: str


class CategoryOut(CategoryBase):
    id: int

    class Config:
        from_attributes = True


# -------- Books --------
class BookBase(BaseModel):
    title: str
    description: str | None = None
    price: float
    url: str | None = ""
    category_id: int


class BookOut(BookBase):
    id: int

    class Config:
        from_attributes = True
