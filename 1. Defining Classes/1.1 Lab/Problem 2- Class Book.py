from dataclasses import dataclass


class Book:
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages


book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)


# Second Method

@dataclass
class Book:
    name: str
    author: str
    pages: int


book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)