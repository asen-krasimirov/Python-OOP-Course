

# def genrange(start, end):
#
#     while True:
#         if start > end:
#             break
#         yield start
#         start += 1


# Overpowered range generator
def op_genrange(start: int, end: int, custom_func: 'func'):
    while True:
        if start > end:
            break
        yield custom_func(start)
        start += 1


def speed(num: int):
    return f'the speed is {num}'


genrange = lambda start, end: (val for val in range(start, end+1))


# print(list(op_genrange(1, 10, speed)))
for item in op_genrange(1, 10, speed):
    print(item)
