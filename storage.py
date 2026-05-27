import json
import os

FILE_PATH = "books.json"

def load_books():
    if not os.path.exists(FILE_PATH):
        return []
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_books(books):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

def add_book(book_obj):
    books = load_books()
    for book in books:
        if book['author'].lower() == book_obj.author.lower() and book['title'].lower() == book_obj.title.lower():
            return False, "Эта книга уже есть в трекере!"
    books.append(book_obj.to_dict())
    save_books(books)
    return True, "Книга успешно добавлена."

def delete_book(title):
    books = load_books()
    initial_count = len(books)
    books = [b for b in books if b['title'].lower() != title.lower()]
    if len(books) == initial_count:
        return False
    save_books(books)
    return True
