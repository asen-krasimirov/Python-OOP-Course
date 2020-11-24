

class store_results:

    def __init__(self, func):
        self.function = func
        self.func_name = f"'{func.__name__}'"

    def __call__(self, *args, **kwargs):
        result = self.function(*args, **kwargs)
        with open('results.txt', 'a') as file:
            file.write(f"Function {self.func_name} was add called. Result: {result}" + '\n')
        return result


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
