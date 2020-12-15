from abc import ABC, abstractmethod


class Formatter(ABC):

    @abstractmethod
    def format(self, book: 'Book'):
        pass


class Printer(ABC):

    @staticmethod
    @abstractmethod
    def get_item(book: 'Book', formatter):
        pass


class Book:
    def __init__(self, author: str, content: str):
        self.author = author
        self.content = content


class FormatByContent(Formatter):

    def format(self, book: 'Book') -> str:
        return book.content


class FormatByAuthor(Formatter):

    def format(self, book: 'Book'):
        return book.author


class BookPrinter(Printer):

    @staticmethod
    def get_item(book: 'Book', formatter):
        formatter = formatter()
        formatted_book = formatter.format(book)
        return formatted_book


book_one = Book('Ronald', 'Hello, I am Ronald')
printer = BookPrinter()
print(printer.get_item(book_one, FormatByContent))
print(printer.get_item(book_one, FormatByAuthor))
