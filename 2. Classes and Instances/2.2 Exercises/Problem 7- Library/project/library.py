from typing import Dict, Union, ClassVar
from collections import defaultdict


class Library:
    user_records: ClassVar[list] = []
    books_available: ClassVar[Dict[str, list]] = {}
    rented_books: ClassVar[Dict[str, Dict[str, int]]] = {}
    book_return_days: ClassVar[Dict[str, int]] = {}

    def add_user(self, user) -> Union[str, None]:
        for member in self.user_records:
            if member.user_id == user.user_id:
                return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)
        # self.rented_books[user.username] = {}

    def remove_user(self, user) -> Union[str, None]:
        for member in self.user_records:
            if member.user_id == user.user_id:
                self.user_records.remove(user)
                return None
        return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str) -> str:
        for member in self.user_records:
            if member.user_id == user_id:
                if member.username == new_username:
                    return "Please check again the provided username - it should be different than the username used so far!"

                new_rented_books = {(name if name != member.username else new_username):data  for name, data in self.rented_books.items()}
                member.username = new_username
                self.rented_books = new_rented_books

                # rented_data = self.rented_books[member.username]
                # self.rented_books.pop(member.username)
                # self.rented_books[new_username] = rented_data

                return f"Username successfully changed to: {new_username} for userid: {user_id}"
        return f"There is no user with id = {user_id}!"
