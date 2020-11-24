

def logged(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        parameters = args+tuple(kwargs.keys())
        result = func(*parameters)
        information = f"you called {func_name}{parameters}\nit returned {result}"

        return information
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


@logged
def sum_func(a, b):
    return a + b


print(func(4, 4, 4))
print(sum_func(1, 4))
