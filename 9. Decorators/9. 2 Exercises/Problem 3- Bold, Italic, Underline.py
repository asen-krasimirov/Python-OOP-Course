

def make_bold(func):
    opening_tag = '<b>'
    closing_tag = '</b>'

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return opening_tag + result +  closing_tag

    return wrapper


def make_italic(func):
    opening_tag = '<i>'
    closing_tag = '</i>'

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return opening_tag + result + closing_tag

    return wrapper


def make_underline(func):
    opening_tag = '<u>'
    closing_tag = '</u>'

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return opening_tag + result + closing_tag

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet("Peter"))
print(greet_all("Peter", "George"))
