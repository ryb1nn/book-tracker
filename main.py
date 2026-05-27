from models import Book
import storage
import stats

def main():
    while True:
        print("\n--- Трекер прочитанных книг ---")
        print("1. Добавить книгу", "2. Показать все книги", "3. Показать среднюю оценку", "4. Статистика по авторам", "5. Удалить книгу", "6. Выход", sep="\n")
        choice = input("Выберите действие (1-6): ").strip()
        if choice == "1":
            author = input("Введите автора: ").strip()
            title = input("Введите название книги: ").strip()
            while True:
                try:
                    rating = int(input("Введите оценку (1-5): "))
                    if 1 <= rating <= 5: break
                    print("Оценка должна быть от 1 до 5!")
                except ValueError: print("Введите целое число!")
            read_date = input("Введите дату прочтения (ГГГГ-ММ-ДД): ").strip()
            new_book = Book(author, title, rating, read_date)
            success, message = storage.add_book(new_book)
            print(message)
        elif choice == "2":
            books = storage.load_books()
            if not books: print("Ваш список книг пока пуст.")
            else:
                print("\nСписок прочитанных книг:")
                for idx, book in enumerate(books, 1):
                    print(f"{idx}. {book['title']} — {book['author']} | Оценка: {book['rating']} | Дата: {book['read_date']}")
        elif choice == "3":
            books = storage.load_books()
            print(f"Средняя оценка всех прочитанных книг: {stats.get_average_rating(books)}")
        elif choice == "4":
            books = storage.load_books()
            author_stats = stats.get_author_statistics(books)
            if not author_stats: print("Нет данных для статистики.")
            else:
                print("\nСтатистика по авторам:")
                for author, info in author_stats.items():
                    print(f"Автор: {author} | Книг: {info['count']} | Средний балл: {info['avg_rating']}")
        elif choice == "5":
            title = input("Введите название книги для удаления: ").strip()
            if storage.delete_book(title): print("Книга успешно удалена.")
            else: print("Книга с таким названием не найдена.")
        elif choice == "6":
            print("Выход из программы. Приятного чтения!")
            break
        else: print("Неверный пункт меню, попробуйте снова.")

if __name__ == "__main__":
    main()
