from password_generator import PasswordGenerator
from os import system


password_repository_file_name = 'password_repository.txt'
generator = PasswordGenerator(password_repository_file_name)


def command_list():

    show_commands = [
        'Control Commands: ',
        'exit -> exits the program',
        'new password -> generates and saves a new password by a key',
        'del password -> deletes a password by key',
        'find password -> finds saved password by key',
        'show all keys -> shows all saved keys'
    ]
    return '\n'.join(show_commands)


def new_password():
    key = input('Enter a key: ')
    length = int(input('Password length: '))
    generator.generate_password(key, length)


def del_password():
    key = input('Enter a key: ')
    delete_bool = input(f'Are sure you want to delete {key}? (yes/no): ')
    if delete_bool == 'yes':
        generator.delete_password(key)
        print(f'No {key} saved anymore.')


def find_password():
    key = input('Enter a key: ')
    password = generator.find_password(key)
    if password:
        print(f'Password of {key}: {password}')
    else:
        print(f'Password not found!')


def show_all_passwords():
    keys = generator.show_all_keys()
    print(f'All Password Keys: \n{keys}\n')


def login():
    print('Welcome to your personal Password Manager')
    for _ in range(3):
        cur_try = input('Enter your password here: ')
        if cur_try == login_password:
            print('Your successfully entered your Password Manager!')
            return
        else:
            print('Wrong password! Try again.')
    system('cls')
    print('Too many wrong answers! Try again later.')
    input()
    exit()


commands = {
    'exit': exit,
    'new password': new_password,
    'del password': del_password,
    'find password': find_password,
    'show all keys': lambda *args: args
}


with open(password_repository_file_name) as file:
    login_password = file.readlines()[0].rstrip('\n').split('<-username - password->')[1]
