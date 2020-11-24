#
#
# def even_parameters(func):
#
#     def wrapper(*args, **kwargs):
#         for arg in args + tuple(kwargs):
#             if not (isinstance(arg, int) and arg % 2 == 0):
#                 return "Please use only even numbers!"
#
#         result = func(*args, **kwargs)
#         return result
#
#     return wrapper
#
#
# @even_parameters
# def add(a, b):
#     return a + b
#
#
# @even_parameters
# def multiply(*nums):
#     result = 1
#     for num in nums:
#         result *= num
#     return result
#
#
# print(add(2, 4))
# print(add("Peter", 1))
# print(multiply(2, 4, 6, 8))
# print(multiply(2, 4, 9, 8))
#
#

#
# # decorator snippet
#
# # def $decorator_name$($decorator_values$):
# #
# #     def decorator(func):
# #         def wrapper(*args, **kwargs):
# #             $END$

# #         return wrapper
# #     return decorator


def type_checker(type_):

    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args + tuple(kwargs.keys()):
                if not isinstance(arg, type_):
                    return 'Bad Type'

            return func(*args, **kwargs)

        return wrapper
    return decorator
