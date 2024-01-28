from typing import Union

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):

        if not isinstance(id_, int):
            raise TypeError("Номер ID должен быть типа int")
        if id_ <= 0:
            raise ValueError("Номер ID должен быть положительным числом")

        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")

        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id_}, name={self.name!r}, pages={self.pages})'


# TODO написать класс Library
class Library:
    def __init__(self, books=None):
        if not isinstance(books, Union[list, None]):
            raise TypeError("Книги должен быть типа list")
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        return len(self.books) + 1

    def get_index_by_book_id(self, arg: int) -> int:
        if not isinstance(arg, int):
            raise TypeError("Номер arg должен быть типа int")
        if arg <= 0:
            raise ValueError("Номер arg должен быть положительным числом")

        if arg <= len(self.books):
            return arg - 1
        else:
            raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки
    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
