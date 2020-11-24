

def tags(tag):
    opening_tag = f"<{tag}>"
    closing_tag = f"</{tag}>"

    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return opening_tag + result + closing_tag
        return wrapper

    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


@tags('h1')
def to_upper(text):
    return text.upper()


print(join_strings("Hello", " you!"))
print(to_upper('hello'))
