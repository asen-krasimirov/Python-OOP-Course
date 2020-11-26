from pprint import pprint
import time


def timer(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Time to execute the function: {end_time-start_time}')
        return result
    return wrapper


def cache(func):

    def wrapper(arg):
        if arg not in wrapper.log:
            result = func(arg)
            wrapper.log[arg] = result
            return result

        return wrapper.log[arg]

    wrapper.log = {}
    return wrapper


@cache
# @timer
def fibonacci(n):

    if n < 2:

        return n

    else:

        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(100)
pprint(fibonacci.log)
