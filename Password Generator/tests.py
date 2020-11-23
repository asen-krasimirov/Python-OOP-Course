from password_generator import PasswordGenerator


def tests():
    generator = PasswordGenerator('password_repository.txt')

    def generate_and_save_password_test():
        generator.generate_password('facebook password', 20)
        generator.generate_password('whatsup', 6)

    def delete_passwords_test():
        generator.delete_password('facebook password')

    def find_password_test():
        print(generator.find_password('whatsup'))

    def show_all_passwords_test():
        print(generator.show_all_keys())

    # generate_and_save_password_test()
    # delete_passwords_test()
    # find_password_test()
    # show_all_passwords_test()


if __name__ == '__main__':
    tests()
