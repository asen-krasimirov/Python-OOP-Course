

def fibonacci():
    number_one = 0
    number_two = 1
    while True:
        yield number_one
        number_one, number_two = number_two, number_one + number_two


generator = fibonacci()
for i in range(5):
    print(next(generator))
