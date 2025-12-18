from app.db import db, crud
from fastapi import FastAPI
from app.api import books, categories
app = FastAPI(title="Books API")

app.include_router(categories.router)
app.include_router(books.router)
def main():
    database = db.SessionLocal()
    categories = crud.get_categories(database)
    books = crud.get_books(database)

    print("Категории:")
    for cat in categories:
        print(f"{cat.id}: {cat.title}")

    print("\nКниги:")
    for book in books:
        print(f"{book.id}: {book.title}, Категория: {book.category.title}, Цена: {book.price}")

    database.close()

if __name__ == "__main__":
    main()
