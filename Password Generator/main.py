from main_functionality import *


def main():

    login()

    while True:
        print('-' * 10)
        print(command_list())
        command = input("Your command: ")
        system('cls')

        if command in commands:
            show_all_passwords()
            commands[command]()
        else:
            print('Incorrect command!')


if __name__ == "__main__":
    main()
