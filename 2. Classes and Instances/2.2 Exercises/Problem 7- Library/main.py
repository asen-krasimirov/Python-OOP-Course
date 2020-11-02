from project.library import Library
from project.user import User


# TODO: Fix if needed- Users not added and removed from the library can access it

user = User(12, 'Peter')
user2 = User(13, 'Simo')
user3 = User(14, 'Boris')

library = Library()

library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
                                                'The Prisoner of Azkaban',
                                                'The Goblet of Fire',
                                                'The Order of the Phoenix',
                                                'The Half-Blood Prince',
                                                'The Deathly Hallows']})

library.add_user(user)
print(library.remove_user(user))
print(library.remove_user(user))
# print(library.change_username(12, "Asen"))
# print(user.get_book("J.K.Rowling", 'The Chamber of Secrets', 10, library))
# print(user.get_book("J.K.Rowling", 'The Deathly Hallows', 12, library))
# print(user2.get_book("J.K.Rowling", 'The Order of the Phoenix', 14, library))
# print(library.rented_books)
print(user.info())
