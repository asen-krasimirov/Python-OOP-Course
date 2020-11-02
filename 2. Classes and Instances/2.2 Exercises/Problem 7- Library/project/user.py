from project.library import Library
from typing import Union


class User:
    user_id: int
    username: str
    books: list

    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library: Library) -> Union[str, None]:

        # TODO: check if book is not in library
        if book_name in library.books_available[author]:
            library.books_available[author].remove(book_name)
            if self.username not in library.rented_books:
                library.rented_books[self.username] = {}

            library.rented_books[self.username][book_name] = days_to_return
            library.book_return_days[book_name] = days_to_return
            self.books.append(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"


        searched_days = library.book_return_days[book_name]
        return f'The book "{book_name}" is already rented and will be available in {searched_days} days!'

    def return_book(self, author: str, book_name: str, library: Library) -> Union[str, None]:
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"

        # TODO: Check if a user has 0 rented books has to be removed

        library.rented_books[self.username].pop(book_name)
        library.book_return_days.pop(book_name)

        self.books.remove(book_name)
        if len(self.books) == 0:
            library.rented_books.pop(self.username)

        library.books_available[author].append(book_name)

    # TODO: Test the method- call from rented_books dict'
    def info(self) -> str:
        return ', '.join(sorted(self.books))

    # TODO: Test the method- the book formatting
    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
