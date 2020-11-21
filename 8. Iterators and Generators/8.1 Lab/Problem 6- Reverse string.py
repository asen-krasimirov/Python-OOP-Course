

# def reverse_text(string):
#     index = len(string)
#     while True:
#         index -= 1
#         if index < 0:
#             break
#         yield string[index]


reverse_text = lambda string: (string[i] for i in range(len(string)-1, -1, -1))


for char in reverse_text("step"):
    print(char, end='')
