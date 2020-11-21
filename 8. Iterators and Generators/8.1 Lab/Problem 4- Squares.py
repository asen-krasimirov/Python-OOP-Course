

# def squares(end_num):
#     for num in range(1, end_num+1):
#         yield num ** 2


def squares(end_num):
    cur_num = 0
    while True:
        cur_num += 1

        if cur_num > end_num:
            break
        yield cur_num ** 2


print(list(squares(5)))
