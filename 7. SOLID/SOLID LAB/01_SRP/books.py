from typing import List


class Book:
    def __init__(self, title: str, author: str, pages: int = 99):
        self.title = title
        self.author = author
        self.__pages = pages

    # def turn_page(self, page):
    #     self.page = page

    @property
    def final_page(self):
        return self.__pages

    def __eq__(self, other: 'Book'):
        return self.title == other.title

    def __str__(self):
        return self.title


class Library:
    location: str
    __books_available: List[Book]  # Note: might trow an exception

    def __init__(self, location: str, books_available: list):
        self.__location = location
        self.__books_available = books_available

    @property
    def location(self):
        return self.__location

    def register_book(self, book: Book):
        for item in self.__books_available:
            if item == book:
                return 'book already registered'

        self.__books_available.append(book)
        return f'successfully registered {book}'

    def get_all_books(self):
        return ', '.join([str(b) for b in self.__books_available])

    def find_book(self, book: Book):
        for item in self.__books_available:
            if item == book:
                return 'book found'
        return 'book not in library'


class Reader:
    name: str
    cur_reading: Book

    def __init__(self, name: str, cur_reading: Book = None):
        self.name = name
        self.cur_reading = cur_reading
        self.page = 0

    def turn_page(self, page):
        if self.cur_reading is None:
            return 'not currently reading'
        if self.cur_reading.final_page < page:
            return 'too big page'

        self.page = page
        return f'turned to page {page} of {self.cur_reading}'

    def read(self, book: Book):
        if self.cur_reading is not None:
            return f'currently reading {self.cur_reading}'

        self.cur_reading = book
        return f'started to read {self.cur_reading}'


def test_one():
    book1 = Book('Title of book1', 'Alexander The First')
    book2 = Book('Title of book2', 'Alexander The Second')

    library = Library('Bobov Dol', [book1])
    print(library.register_book(book1))
    print(library.register_book(book2))
    print(library.get_all_books())


def test_two():
    book1 = Book('Title of book1', 'Alexander The First')
    reader_one = Reader("Boris", book1)
    print(reader_one.turn_page(100))


def test_three():
    book1 = Book('Title of book1', 'Alexander The First')
    book2 = Book('Title of book2', 'Alexander The Second')

    library = Library('Bobov Dol', [book1])

    print(library.find_book(book1))
    print(library.find_book(book2))


test_three()
