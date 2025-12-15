from app.db import db, crud

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
