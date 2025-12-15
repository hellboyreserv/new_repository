from app.db import db, models, crud

def init_db():
    models.Base.metadata.create_all(bind=db.engine)
    database = db.SessionLocal()

    # Добавляем категории
    cat1 = crud.create_category(database, "Фантастика")
    cat2 = crud.create_category(database, "Наука")

    # Добавляем книги
    crud.create_book(database, "Книга 1", "Описание 1", 10.5, cat1.id)
    crud.create_book(database, "Книга 2", "Описание 2", 15.0, cat1.id)
    crud.create_book(database, "Книга 3", "Описание 3", 20.0, cat2.id)
    crud.create_book(database, "Книга 4", "Описание 4", 25.0, cat2.id)

    database.close()

if __name__ == "__main__":
    init_db()